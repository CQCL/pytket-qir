# Copyright 2019-2022 Cambridge Quantum Computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains all functionality to parse and generate QIR files
to and from pytket circuits.
"""

import functools
import inspect
import json
import os
import re
from typing import cast, Callable, Dict, List, Optional, Tuple, Union


from pytket import Circuit, OpType  # type: ignore
from pytket.wasm import WasmFileHandler  # type: ignore
from pytket.circuit import (  # type: ignore
    BitRegister,
    CircBox,
    Op,
)
from pytket.circuit.logic_exp import (  # type: ignore
    RegAdd,
    RegAnd,
    RegSub,
    RegMul,
    RegOr,
    RegDiv,
    RegLsh,
    RegRsh,
    RegXor,
    reg_eq,
    reg_neq,
    reg_leq,
    reg_geq,
    reg_lt,
    reg_gt,
    RegNeg,
)

from pyqir.generator import ir_to_bitcode  # type: ignore
from pyqir.parser import (  # type: ignore
    QirBlock,
    QirBrTerminator,
    QirCondBrTerminator,
    QirModule,
    QirInstr,
    QirResultConstant,
    QirRtCallInstr,
    QirSelectInstr,
)
from pyqir.parser._native import PyQirInstruction  # type: ignore
from pyqir.generator import ir_to_bitcode, types  # type: ignore
from pyqir.parser._native import PyQirInstruction  # type: ignore
from pyqir.parser._parser import QirIntConstant, QirICmpInstr, QirCallInstr, QirOpInstr, QirOperand, QirLocalOperand  # type: ignore
from pyqir.generator import ir_to_bitcode, types  # type: ignore


from pytket_qir.gatesets.base import (
    CustomGateSet,
    OpNat,
    OpName,
    OpSpec,
    QirGate,
)

from pytket_qir.gatesets.pyqir.pyqir import PYQIR_GATES  # type: ignore
from pytket_qir.utils import InstructionError, WASMError


_PYQIR_TO_TK_CLOPS: Dict[str, Union[type, Dict[str, Callable]]] = {
    "is_add": RegAdd,
    "is_sub": RegSub,
    "is_mul": RegMul,
    "is_sdiv": RegDiv,
    "is_shl": RegLsh,
    "is_lshr": RegRsh,
    "is_icmp": {
        "eq": reg_eq,
        "ne": reg_neq,
        "ule": reg_leq,
        "uge": reg_geq,
        "ult": reg_lt,
        "ugt": reg_gt,
    },
    "is_and": RegAnd,
    "is_or": RegOr,
    "is_xor": RegXor,
}


class QirParser:
    """A parser class to return a pytket circuit from a QIR file."""

    def __init__(
        self,
        file_path: str,
        gateset: Optional[CustomGateSet] = None,
        wasm_handler: Optional[WasmFileHandler] = None,
        wasm_int_type: types.Int = types.Int(32),
        qir_int_type: types.Int = types.Int(64),
    ) -> None:
        self.module = QirModule(file_path)
        self.gateset: CustomGateSet = gateset if gateset is not None else PYQIR_GATES
        self.wasm_handler = wasm_handler
        self.wasm_int_type = wasm_int_type
        self.qir_int_type = qir_int_type
        self.qubits = self.get_required_qubits()
        self.bits = self.get_required_results()
        entry_block = self.module.functions[0].get_block_by_name("entry")
        if entry_block is None:
            raise NotImplementedError("The QIR file does not contain an entry block.")
        self.circuit = self.block_to_circuit(
            entry_block, Circuit(self.qubits, self.bits)
        )

    def get_required_qubits(self) -> int:
        interop_funcs = self.module.get_funcs_by_attr("EntryPoint")
        qubits = interop_funcs[0].get_attribute_value("requiredQubits")
        if qubits is not None:
            return int(qubits)
        return 0

    def get_required_results(self) -> int:
        interop_funcs = self.module.get_funcs_by_attr("EntryPoint")
        results = interop_funcs[0].get_attribute_value("requiredResults")
        if results is not None:
            return int(results)
        return 0

    def get_optype(self, instr: PyQirInstruction) -> OpType:
        if instr.is_call:
            call_func_name = cast(str, instr.call_func_name)
            matched_str = re.search("__quantum__(.+?)__(.+?)__(.+)", call_func_name)
            if not matched_str:
                raise WASMError("The WASM function call name is not properly defined.")
            opnat = OpNat(matched_str.group(1))
            opname = OpName(matched_str.group(2))
            opspec = OpSpec(matched_str.group(3))
            pyqir_gate = QirGate(opnat=opnat, opname=opname, opspec=opspec)
            return self.gateset.gateset_to_tk(pyqir_gate)

    def get_params(self, instr: PyQirInstruction) -> List[float]:
        params: List = []
        call_func_params = cast(List, instr.call_func_params)
        for param in call_func_params:
            if param.is_constant:
                if param.constant.is_float:
                    params.append(param.constant.float_double_value)
        return params

    def get_operation(self, instr: QirInstr) -> Op:
        optype = self.get_optype(instr.instr)
        params = self.get_params(instr.instr)
        return Op.create(optype, params)

    def get_qubit_indices(self, instr: PyQirInstruction) -> List[int]:
        params: List = []
        call_func_params = cast(List, instr.call_func_params)
        for param in call_func_params:
            if param.is_constant:
                if param.constant.is_qubit:
                    params.append(param.constant.qubit_static_id)
                elif param.constant.is_result:
                    params.append(param.constant.result_static_id)
        return params

    def get_arg_and_tag(self, instr: QirRtCallInstr) -> Tuple[int, Optional[str]]:
        args = cast(List, instr.func_args)

        @functools.singledispatch
        def convert_argument(arg):
            pass

        @convert_argument.register
        def _(arg: QirLocalOperand):
            return "%" + arg.name

        @convert_argument.register
        def _(arg: QirResultConstant):
            return arg.value

        arg_value = convert_argument(args[0])
        try:
            tag = args[1]
            tag_value = cast(bytes, self.module.get_global_bytes_value(tag))
            tag_str = tag_value.decode("utf-8")
        except IndexError:
            tag_str = None
        return arg_value, tag_str

    def add_classical_op(
        self,
        classical_op: str,
        instr: Union[QirInstr, QirOpInstr],
        circuit: Circuit,
        c_reg_map: Dict,
    ) -> None:
        def add_classical_register(
            operands: Union[List, QirOperand], circuit: Circuit
        ) -> Union[Tuple, BitRegister]:
            c_regs: List[BitRegister] = []

            def add_register(operands: List) -> List:
                for index, operand in enumerate(operands):

                    if isinstance(operand, QirIntConstant):
                        c_reg = c_reg_map[index + 1]
                        circuit.add_c_setreg(operand.value, c_reg)
                        c_regs.append(c_reg)
                    else:
                        register_name = "%" + operand.name  # Keep QIR syntax.
                        c_reg = circuit.get_c_register(register_name)
                        c_regs.append(c_reg)
                return c_regs

            if isinstance(operands, QirIntConstant):
                return add_register([operands])[0]
            elif isinstance(operands, List):
                return tuple(add_register(list(operands)))
            return None

        instr = cast(QirOpInstr, instr)
        operands = instr.target_operands
        c_op: Callable
        if classical_op == "is_icmp":
            instr = cast(QirICmpInstr, instr)
            c_reg1 = add_classical_register(operands[0], circuit)
            c_op_dict = cast(Dict, _PYQIR_TO_TK_CLOPS[classical_op])
            c_op = c_op_dict[instr.predicate]
            operand1 = cast(QirIntConstant, operands[1])
            circuit.add_classicalexpbox_register(
                c_op(c_reg1, operand1.value),  # Comparaison with constants.
                c_reg_map[3],
            )
        else:
            c_op = cast(Callable, _PYQIR_TO_TK_CLOPS[classical_op])
            # Integer negation is represented as a substraction from 0.
            if isinstance(operands[0], QirIntConstant):
                operand1 = cast(QirIntConstant, operands[1])
                if operands[0].value == 0:
                    circuit.add_classicalexpbox_register(
                        RegNeg(operand1.value), c_reg_map[3]
                    )
            c_reg1, c_reg2 = add_classical_register(operands, circuit)
            circuit.add_classicalexpbox_register(c_op(c_reg1, c_reg2), c_reg_map[3])

    def _create_register_map(self, circuit: Circuit) -> Dict:
        # Generate two reusable registers to hold temporary constants.
        c_reg1 = BitRegister("c_reg_1", self.qir_int_type.width)
        c_reg2 = BitRegister("c_reg_2", self.qir_int_type.width)
        if all(reg in circuit.c_registers for reg in [c_reg1, c_reg2]):
            c_reg1 = circuit.get_c_register("c_reg_1")
            c_reg2 = circuit.get_c_register("c_reg_2")
            return {1: c_reg1, 2: c_reg2}
        else:
            c_reg1 = circuit.add_c_register(c_reg1)
            c_reg2 = circuit.add_c_register(c_reg2)
            return {1: c_reg1, 2: c_reg2}

    def block_to_circuit(self, block: QirBlock, circuit: Circuit) -> Circuit:
        instrs = block.instructions
        term = block.terminator

        for instr in instrs:
            if instr.instr.is_qis_call:  # Quantum gates.
                op = self.get_operation(instr)
                unitids = self.get_qubit_indices(instr.instr)
                circuit.add_gate(op, unitids)
            elif instr.instr.is_qir_call:  # Setting the conditional bit for branching.
                params = cast(List, instr.instr.call_func_params)
                param = params[0]
                assert param.constant is not None
                c_reg_index = param.constant.result_static_id
            elif instr.instr.is_rt_call:  # Runtime function call.
                instr = cast(QirRtCallInstr, instr)
                bits = self.get_qubit_indices(instr.instr)
                arg, tag = self.get_arg_and_tag(instr)
                # Create a JSON object for the data to be passed.
                data = {"name": cast(str, instr.func_name), "arg": arg}
                if tag is not None:
                    data["tag"] = tag
                if bits:
                    circuit.add_barrier(qubits=[], bits=bits, data=json.dumps(data))
                else:
                    bits = circuit.get_c_register(arg)
                    circuit.add_barrier(units=bits, data=json.dumps(data))
            elif instr.instr.is_select:
                instr = cast(QirSelectInstr, instr)
                output_name = "%" + str(instr.output_name)
                true_value = cast(QirIntConstant, instr.true_value)
                false_value = cast(QirIntConstant, instr.false_value)
                output_reg = circuit.add_c_register(output_name, true_value.width)
                condition = cast(QirLocalOperand, instr.condition)
                condition_name = "%" + str(condition.name)
                condition_reg = circuit.get_c_register(condition_name)
                circuit.add_c_setreg(
                    true_value.value,
                    output_reg,
                    condition_bits=[condition_reg[0]],
                    condition_value=1,
                )
                circuit.add_c_setreg(
                    false_value.value,
                    output_reg,
                    condition_bits=[condition_reg[0]],
                    condition_value=0,
                )
            elif instr.instr.is_zext:
                output_name = "%" + str(instr.output_name)
                output_reg = circuit.add_c_register(
                    output_name, self.qir_int_type.width
                )
                data = {"name": "zext"}
                circuit.add_barrier(units=output_reg, data=json.dumps(data))
            elif instr.instr.is_call:  # WASM external call.
                instr = cast(QirCallInstr, instr)
                if self.wasm_handler is None:
                    raise WASMError("A WASM file handler must be provided.")
                func_name = cast(str, instr.func_name)
                if func_name is None:
                    raise WASMError("The WASM function call is not defined.")
                matched_str = re.search("__quantum__(.+?)__(.+?)__(.+)", func_name)
                if matched_str is None:
                    raise WASMError(
                        "The WASM function call name is not properly defined."
                    )
                # WASM function call parameters.
                param_regs = []
                for c_reg_index in range(len(instr.func_args)):
                    c_reg_name = "c_reg_wasm" + str(c_reg_index)
                    param_regs.append(
                        circuit.add_c_register(c_reg_name, self.wasm_int_type.width)
                    )

                # WASM function return  type.
                output_name = cast(str, instr.output_name)
                c_reg_output_name = "%" + output_name
                c_reg_output = circuit.add_c_register(
                    c_reg_output_name, self.wasm_int_type.width
                )
                circuit.add_wasm_to_reg(
                    matched_str.group(2), self.wasm_handler, param_regs, [c_reg_output]
                )
            else:  # Classical instruction.
                # Create registers to hold classical constants.
                c_reg_map = self._create_register_map(circuit)
                # Get and filter true predicates.
                attrs = inspect.getmembers(
                    instr.instr, lambda attr: not (inspect.isroutine(attr))
                )
                filtered_attrs = [
                    attr[0] for attr in attrs if attr[0].startswith("is_") and attr[1]
                ]
                # Retain only supported classical ops.
                if (
                    len(filtered_attrs) == 1
                    and (matching := filtered_attrs[0]) in _PYQIR_TO_TK_CLOPS.keys()
                ):
                    # Generate a register with a unique name
                    # from the QIR one to hold the operation result
                    # and add it to the register map.
                    output_name = cast(str, instr.output_name)
                    c_reg_name3 = "%" + output_name
                    c_reg3 = circuit.add_c_register(
                        c_reg_name3, self.qir_int_type.width
                    )  # Int64 supported in LLVM/QIR and L3.
                    c_reg_map[3] = c_reg3
                    self.add_classical_op(matching, instr, circuit, c_reg_map)
                else:
                    raise InstructionError(
                        "The instruction {:} is currently not supported.".format(
                            type(instr)
                        )
                    )

        if isinstance(term, QirCondBrTerminator):
            if_condition_block = cast(
                QirBlock, self.module.functions[0].get_block_by_name(term.true_dest)
            )
            if_condition_circuit = self.block_to_circuit(
                if_condition_block, Circuit(self.qubits, self.bits)
            )
            circ_box = CircBox(if_condition_circuit)
            c_reg = circuit.get_c_register("c")
            args = list(range(self.qubits)) + list(range(self.bits))  # Order matters.
            circuit.add_circbox(circ_box, args, condition=c_reg[c_reg_index])

            else_condition_block = cast(
                QirBlock, self.module.functions[0].get_block_by_name(term.false_dest)
            )
            else_condition_circuit = self.block_to_circuit(
                else_condition_block, Circuit(self.qubits, self.bits)
            )
            circuit.append(else_condition_circuit)

        if isinstance(term, QirBrTerminator):
            next_block = cast(
                QirBlock, self.module.functions[0].get_block_by_name(term.dest)
            )
            next_circuit = self.block_to_circuit(
                next_block, Circuit(self.qubits, self.bits)
            )
            circuit.append(next_circuit)

        return circuit


def circuit_from_qir(
    input_file: Union[str, os.PathLike],
    gateset: Optional[CustomGateSet] = None,
    wasm_handler: Optional[WasmFileHandler] = None,
    wasm_int_type: types.Int = types.Int(32),
) -> Circuit:
    root, ext = os.path.splitext(os.path.basename(input_file))
    input_file_str = str(input_file)
    output_bc_file: str = ""
    if ext not in [".ll", ".bc"]:
        raise TypeError("Can only convert '.bc' or '.ll' files.")
    if ext == ".ll":
        with open(input_file_str, "r") as f:
            data = f.read()
        output_bc_file = root + ".bc"
        with open(output_bc_file, "wb") as o:
            o.write(ir_to_bitcode(data))
        input_file_str = output_bc_file
    return QirParser(input_file_str, gateset, wasm_handler, wasm_int_type).circuit
