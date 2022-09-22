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

import inspect
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
)
from pyqir.parser._native import PyQirInstruction  # type: ignore
from pyqir.parser._parser import QirIntConstant, QirICmpInstr, QirCallInstr, QirOpInstr, QirOperand  # type: ignore

from pytket_qir.gatesets.base import (
    CustomGateSet,
    OpNat,
    OpName,
    OpSpec,
    QirGate,
)
from pytket_qir.gatesets.pyqir import PYQIR_GATES  # type: ignore


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
        gateset: Optional[CustomGateSet],
        wasm_handler: Optional[WasmFileHandler],
    ) -> None:
        self.module = QirModule(file_path)
        self.gateset: CustomGateSet = gateset if gateset else PYQIR_GATES
        self.wasm_handler = wasm_handler
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
            call_func_name = instr.call_func_name
            assert call_func_name
            matched_str = re.search("__quantum__(.+?)__(.+?)__(.+)", call_func_name)
            if not matched_str:
                raise ValueError("The WASM function call name is not propely defined.")
            opnat = OpNat(matched_str.group(1))
            opname = OpName(matched_str.group(2))
            opspec = OpSpec(matched_str.group(3))
            pyqir_gate = QirGate(opnat=opnat, opname=opname, opspec=opspec)
            return self.gateset.gateset_to_tk(pyqir_gate)

    def get_params(self, instr: PyQirInstruction) -> List[float]:
        params: List = []
        assert instr.call_func_params
        for param in instr.call_func_params:
            assert param.constant
            if param.constant.is_float:
                params.append(param.constant.float_double_value)
        return params

    def get_operation(self, instr: QirInstr) -> Op:
        optype = self.get_optype(instr.instr)
        params = self.get_params(instr.instr)
        return Op.create(optype, params)

    def get_qubit_indices(self, instr: PyQirInstruction) -> List[int]:
        params: List = []
        assert instr.call_func_params
        for param in instr.call_func_params:
            assert param.constant
            if param.constant.is_qubit:
                params.append(param.constant.qubit_static_id)
            elif param.constant.is_result:
                params.append(param.constant.result_static_id)
        return params

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
                        # import pdb; pdb.set_trace()
                        register_name = "%" + operand.name  # Keep QIR syntax.
                        c_reg = circuit.get_c_register(register_name)
                        c_regs.append(c_reg)
                return c_regs

            if isinstance(operands, QirIntConstant):
                return add_register([operands])[0]
            elif isinstance(operands, List):
                return tuple(add_register(list(operands)))
            return None

        # import pdb; pdb.set_trace()
        # assert instr.target_operands
        assert isinstance(instr, QirOpInstr)
        operands = instr.target_operands
        c_op: Callable
        if classical_op == "is_icmp":
            assert isinstance(instr, QirICmpInstr)
            c_reg1 = add_classical_register(operands[0], circuit)
            c_op_dict = cast(Dict, _PYQIR_TO_TK_CLOPS[classical_op])
            c_op = c_op_dict[instr.predicate]
            # import pdb; pdb.set_trace()
            assert isinstance(operands[1], QirIntConstant)
            circuit.add_classicalexpbox_register(
                c_op(c_reg1, operands[1].value),  # Comparaison with constants.
                c_reg_map[3],
            )
        else:
            # import pdb; pdb.set_trace()
            c_op = cast(Callable, _PYQIR_TO_TK_CLOPS[classical_op])
            # Integer negation is represented as a substraction from 0.
            if isinstance(operands[0], QirIntConstant):
                assert isinstance(operands[1], QirIntConstant)
                if operands[0].value == 0:
                    circuit.add_classicalexpbox_register(
                        RegNeg(operands[1].value), c_reg_map[3]
                    )
            c_reg1, c_reg2 = add_classical_register(operands, circuit)
            circuit.add_classicalexpbox_register(c_op(c_reg1, c_reg2), c_reg_map[3])

    def _create_register_map(self, circuit: Circuit) -> Dict:
        # Generate two reusable registers to hold temporary constants.
        c_reg1 = BitRegister("c_reg_1", 64)
        c_reg2 = BitRegister("c_reg_2", 64)
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
                assert instr.instr.call_func_params
                param = instr.instr.call_func_params[0]
                assert param.constant
                c_reg_index = param.constant.result_static_id
            elif instr.instr.is_call:  # WASM external call.
                if not self.wasm_handler:
                    raise ValueError("A WASM file handler must be provided.")
                assert isinstance(instr, QirCallInstr)
                func_name = instr.func_name
                if not func_name:
                    raise ValueError("The WASM function call is not defined.")
                matched_str = re.search("__quantum__(.+?)__(.+?)__(.+)", func_name)
                if not matched_str:
                    raise ValueError(
                        "The WASM function call name is not propely defined."
                    )
                # WASM function call parameters.
                param_regs = []
                for c_reg_index in range(len(instr.func_args)):
                    c_reg_name = "c_reg_wasm" + str(c_reg_index)
                    param_regs.append(circuit.add_c_register(c_reg_name, 64))

                # WASM function return type.
                assert instr.output_name
                c_reg_output_name = "%" + instr.output_name
                c_reg_output = circuit.add_c_register(c_reg_output_name, 64)
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
                    assert instr.output_name
                    c_reg_name3 = "%" + instr.output_name
                    c_reg3 = circuit.add_c_register(
                        c_reg_name3, 64
                    )  # Int64 supported in LLVM/QIR and L3.
                    c_reg_map[3] = c_reg3
                    # import pdb; pdb.set_trace()
                    # instr = cast(instr, PyQirInstruction)
                    # assert isinstance(instr, PyQirInstruction)
                    self.add_classical_op(matching, instr, circuit, c_reg_map)
                else:
                    raise ValueError("Unsupported instruction.")

        if isinstance(term, QirCondBrTerminator):
            if_condition_block = self.module.functions[0].get_block_by_name(
                term.true_dest
            )
            assert isinstance(if_condition_block, QirBlock)
            if_condition_circuit = self.block_to_circuit(
                if_condition_block, Circuit(self.qubits, self.bits)
            )
            circ_box = CircBox(if_condition_circuit)
            c_reg = circuit.get_c_register("c")
            args = list(range(self.qubits)) + list(range(self.bits))  # Order matters.
            circuit.add_circbox(circ_box, args, condition=c_reg[c_reg_index])

            else_condition_block = self.module.functions[0].get_block_by_name(
                term.false_dest
            )
            assert isinstance(else_condition_block, QirBlock)
            else_condition_circuit = self.block_to_circuit(
                else_condition_block, Circuit(self.qubits, self.bits)
            )
            circuit.append(else_condition_circuit)

        if isinstance(term, QirBrTerminator):
            next_block = self.module.functions[0].get_block_by_name(term.dest)
            assert isinstance(next_block, QirBlock)
            next_circuit = self.block_to_circuit(
                next_block, Circuit(self.qubits, self.bits)
            )
            circuit.append(next_circuit)

        return circuit


def circuit_from_qir(
    input_file: Union[str, os.PathLike],
    gateset: Optional[CustomGateSet] = None,
    wasm_handler: Optional[WasmFileHandler] = None,
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
    return QirParser(input_file_str, gateset, wasm_handler).circuit
