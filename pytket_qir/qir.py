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

"""This module contains all functionality to parse and generate QIR files."""

import inspect
import os
import re
from typing import Dict, List, Optional, Tuple, Union

from pytket import Circuit, OpType, Bit, Qubit  # type: ignore
from pytket.circuit import BitRegister, CircBox, Conditional, Op  # type: ignore
from pytket.circuit.logic_exp import (
    BitWiseOp,
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

from pyqir.parser import (  # type: ignore
    QirBlock,
    QirBrTerminator,
    QirCondBrTerminator,
    QirModule,
    QirInstr,
)
from pyqir.parser._native import PyQirInstruction  # type: ignore
from pyqir.generator import SimpleModule, BasicQisBuilder, ir_to_bitcode, types  # type: ignore
from pyqir.parser._native import PyQirInstruction, PyQirOperand  # type: ignore
from pyqir.generator import SimpleModule, BasicQisBuilder, ir_to_bitcode, types  # type: ignore
from pyqir.generator.types import Qubit, Result  # type: ignore


from pytket_qir.gatesets.base import (
    CustomGateSet,
    GateSet,
    OpNat,
    OpName,
    OpSpec,
    QirGate,
)
from pytket_qir.gatesets.pyqir.pyqir import PYQIR_GATES  # type: ignore


classical_ops: Dict = {
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

    def __init__(self, file_path: str, gateset: Optional[CustomGateSet]) -> None:
        self.module = QirModule(file_path)
        self.gateset: Union[GateSet, CustomGateSet] = (
            gateset if gateset else PYQIR_GATES
        )
        self.qubits = self.get_required_qubits()
        self.bits = self.get_required_results()
        entry_block = self.module.functions[0].get_block_by_name("entry")
        if entry_block is None:
            raise NotImplementedError("The QIR file does not contain an entry block.")
        self.circuit = self.block_to_circuit(
            entry_block, Circuit(self.qubits, self.bits)
        )

    def get_required_qubits(self) -> int:
        # Note: InteropFriendly is to be changed to EntryPoint in future versions.
        interop_funcs = self.module.get_funcs_by_attr("EntryPoint")
        qubits = interop_funcs[0].get_attribute_value("requiredQubits")
        if qubits is not None:
            return int(qubits)
        return 0

    def get_required_results(self) -> int:
        # Note: InteropFriendly is to be changed to EntryPoint in future versions.
        interop_funcs = self.module.get_funcs_by_attr("EntryPoint")
        results = interop_funcs[0].get_attribute_value("requiredResults")
        if results is not None:
            return int(results)
        return 0

    def get_optype(self, instr: PyQirInstruction) -> OpType:
        if instr.is_call:
            call_func_name = instr.call_func_name
            matched_str = re.search("__quantum__(.+?)__(.+?)__(.+)", call_func_name)
            assert matched_str
            opnat = OpNat(matched_str.group(1))
            opname = OpName(matched_str.group(2))
            opspec = OpSpec(matched_str.group(3))
            pyqir_gate = QirGate(opnat=opnat, opname=opname, opspec=opspec)
            return self.gateset.gateset_to_tk(pyqir_gate)

    def get_params(self, instr: PyQirInstruction) -> List[float]:
        params: List = []
        for param in instr.call_func_params:
            if param.constant.is_float:
                params.append(param.constant.float_double_value)
        return params

    def get_operation(self, instr: QirInstr) -> Op:
        optype = self.get_optype(instr.instr)
        params = self.get_params(instr.instr)
        return Op.create(optype, params)

    def get_qubit_indices(self, instr: PyQirInstruction) -> List[int]:
        params: List = []
        for param in instr.call_func_params:
            if param.constant.is_qubit:
                params.append(param.constant.qubit_static_id)
            elif param.constant.is_result:
                params.append(param.constant.result_static_id)
        return params

    def add_classical_op(
        self,
        classical_op: str,
        instr: PyQirInstruction,
        circuit: Circuit,
        c_reg_map: Dict,
    ) -> None:
        def add_classical_register(
            operands: Union[List, PyQirOperand], circuit: Circuit
        ) -> Union[Tuple, PyQirOperand]:
            c_regs: List[BitRegister] = []

            def add_register(operands: List) -> List:
                for index, operand in enumerate(operands):
                    if operand.is_constant:
                        c_reg = c_reg_map[index + 1]
                        circuit.add_c_setreg(operand.constant.int_value, c_reg)
                        c_regs.append(c_reg)
                    else:
                        assert operand.is_local
                        register_name = "%" + operand.local_name  # Keep QIR syntax.
                        c_reg = circuit.get_c_register(register_name)
                        c_regs.append(c_reg)
                return c_regs

            if isinstance(operands, PyQirOperand):
                operands = [operands]
                return add_register(operands)[0]
            else:
                return tuple(add_register(operands))

        operands = instr.instr.target_operands
        if classical_op == "is_icmp":
            c_reg1 = add_classical_register(operands[0], circuit)
            c_op = classical_ops[classical_op][instr.predicate]
            circuit.add_classicalexpbox_register(
                c_op(
                    c_reg1, operands[1].constant.int_value
                ),  # Comparaison with constants.
                c_reg_map[3],
            )
        else:
            c_op = classical_ops[classical_op]
            # Integer negation is represented as a substraction from 0.
            if operands[0].is_constant:
                if operands[0].constant.int_value == 0:
                    circuit.add_classicalexpbox_register(
                        RegNeg(operands[1].constant.int_value), c_reg_map[3]
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
                c_reg_index = instr.instr.call_func_params[0].constant.result_static_id
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
                    and (matching := filtered_attrs[0]) in classical_ops.keys()
                ):
                    # Generate a register with a unique name
                    # from the QIR one to hold the operation result
                    # and add it to the register map.
                    c_reg_name3 = "%" + instr.instr.output_name
                    c_reg3 = circuit.add_c_register(
                        c_reg_name3, 64
                    )  # Int64 supported in LLVM/QIR and L3.
                    c_reg_map[3] = c_reg3
                    self.add_classical_op(matching, instr, circuit, c_reg_map)
                else:
                    raise ValueError("Unsupported instruction.")

        if isinstance(term, QirCondBrTerminator):
            if_condition_block = self.module.functions[0].get_block_by_name(
                term.true_dest
            )
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
            else_condition_circuit = self.block_to_circuit(
                else_condition_block, Circuit(self.qubits, self.bits)
            )
            circuit.append(else_condition_circuit)

        if isinstance(term, QirBrTerminator):
            next_block = self.module.functions[0].get_block_by_name(term.dest)
            next_circuit = self.block_to_circuit(
                next_block, Circuit(self.qubits, self.bits)
            )
            circuit.append(next_circuit)

        return circuit


def circuit_from_qir(
    input_file: Union[str, os.PathLike], gateset: Optional[CustomGateSet] = None
) -> Circuit:
    root, ext = os.path.splitext(os.path.basename(input_file))
    input_file_str = str(input_file)
    output_bc_file: str = ""
    if ext not in [".ll", ".bc"]:
        raise TypeError("Can only convert .bc or .ll files.")
    if ext == ".ll":
        with open(input_file_str, "r") as f:
            data = f.read()
        output_bc_file = root + ".bc"
        with open(output_bc_file, "wb") as o:
            o.write(ir_to_bitcode(data))
        input_file_str = output_bc_file
    return QirParser(input_file_str, gateset).circuit


class QIRUnsupportedError(Exception):
    pass


class Module:
    """Module extensions to account for any input gate set."""

    def __init__(
        self,
        name: str,
        num_qubits: int,
        num_results: int,
        gateset: Optional[CustomGateSet] = None,
    ) -> None:
        self.module = SimpleModule(name, num_qubits, num_results)
        self.builder = self.module.builder
        self.qis = BasicQisBuilder(self.builder)
        if gateset:
            self.gateset = gateset
            for v in self.gateset.gateset.values():
                self.__setattr__(
                    v.opname.value,
                    self.module.add_external_function(
                        self.gateset.template.substitute(
                            opnat=v.opnat.value,
                            opname=v.opname.value,
                            opspec=v.opspec.value,
                        ),
                        types.Function(v.function_signature, v.return_type),
                    ),
                )
        else:
            self.default_gateset = PYQIR_GATES


def _get_optype_and_params(op: Op) -> Tuple[OpType, List[float]]:
    optype = op.type
    params: List = []
    if optype == OpType.ExplicitPredicate:
        if op.get_name() == "AND":
            optype = BitWiseOp.AND
        elif op.get_name() == "OR":
            optype = BitWiseOp.OR
        elif op.get_name() == "XOR":
            optype = BitWiseOp.XOR
    else:
        params = op.params
        if optype == OpType.TK1:
            params = [op.params[1], op.params[0] - 0.5, op.params[2] + 0.5]
    return (optype, params)


def _to_qis_qubits(qubits: List[Qubit], mod: SimpleModule) -> List[Qubit]:
    return [mod.qubits[qubit.index[0]] for qubit in qubits]


def _to_qis_results(bits: List[Bit], mod: SimpleModule) -> Optional[Result]:
    if bits:
        return mod.results[bits[0].index[0]]
    return None


def _to_qis_bits(args: List[Bit], mod: SimpleModule) -> List[Result]:
    if args:
        return [mod.results[bit.index[0]] for bit in args[:-1]]
    return []


def circuit_to_module(circ: Circuit, module: Module) -> Module:
    """A method to generate a QIR string from a pytket circuit."""
    for command in circ:
        op = command.op
        if isinstance(op, Conditional):
            conditional_circuit = op.op.get_circuit()
            condition_bit_index = command.args[0].index[0]

            def condition_one_block():
                """
                Populate recursively the module with the contents of the conditional
                sub-circuit when the condition is True.
                """
                if op.value == 1:
                    circuit_to_module(conditional_circuit, module)

            def condition_zero_block():
                """
                Populate recursively the module with the contents of the conditional
                sub-circuit when the condition is False.
                """
                if op.value == 0:
                    circuit_to_module(conditional_circuit, module)

            module.qis.if_result(
                module.module.results[condition_bit_index],
                one=lambda: condition_one_block(),
                zero=lambda: condition_zero_block(),
            )
        else:
            optype, params = _get_optype_and_params(op)
            qubits = _to_qis_qubits(command.qubits, module.module)
            results = _to_qis_results(command.bits, module.module)
            if hasattr(module, "gateset"):
                bits: Optional[List[Result]] = None
                if type(optype) == BitWiseOp:
                    bits = _to_qis_bits(command.args, module.module)
                gate = module.gateset.tk_to_gateset(optype)
                get_gate = getattr(module, gate.opname.value)
                if bits:
                    module.builder.call(get_gate, bits)
                elif params:
                    module.builder.call(get_gate, [*params, *qubits])
                elif results:
                    module.builder.call(get_gate, [*qubits, results])
                else:
                    module.builder.call(get_gate, qubits)
            else:
                pyqir_gate = module.default_gateset.tk_to_gateset(optype)
                if not pyqir_gate.opspec == OpSpec.BODY:
                    opname = pyqir_gate.opname.value + "_" + pyqir_gate.opspec.value
                    get_gate = getattr(module.qis, opname)
                else:
                    get_gate = getattr(module.qis, pyqir_gate.opname.value)
                if params:
                    get_gate(*params, *qubits)
                elif results:
                    get_gate(*qubits, results)
                else:
                    get_gate(*qubits)
    return module


def write_qir_file(
    circ: Circuit, output_file: str, gateset: Optional[CustomGateSet] = None
) -> None:
    """A method to generate a qir file from a tket circuit."""
    root, ext = os.path.splitext(os.path.basename(output_file))
    if ext not in [".ll", ".bc"]:
        raise ValueError("The file extension should either be '.ll' or '.bc'.")
    module = Module(
        name=root,
        num_qubits=circ.n_qubits,
        num_results=len(circ.bits),
        gateset=gateset,
    )
    populated_module = circuit_to_module(circ, module)
    if ext == ".ll":
        with open(output_file, "w") as out:
            out.write(populated_module.module.ir())
    elif ext == ".bc":
        with open(output_file, "wb") as out:
            out.write(ir_to_bitcode(populated_module.module.ir(), output_file))


def circuit_to_qir_bytes(
    circ: Circuit, gateset: Optional[CustomGateSet] = None
) -> bytes:
    """Return a pytket circuit as bytes."""
    module = Module(
        name="Pytket circuit",
        num_qubits=circ.n_qubits,
        num_results=len(circ.bits),
        gateset=gateset,
    )
    populated_module = circuit_to_module(circ, module)
    return ir_to_bitcode(populated_module.module.ir())
