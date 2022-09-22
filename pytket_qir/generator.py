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

from enum import Enum
from functools import partial
import os
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union


from pytket import Circuit, OpType, Bit, Qubit  # type: ignore
from pytket.qasm.qasm import _retrieve_registers  # type: ignore
from pytket.wasm import WasmFileHandler  # type: ignore
from pytket.circuit import (  # type: ignore
    BitRegister,
    ClassicalExpBox,
    Command,
    Conditional,
    Op,
    SetBitsOp,
    WASMOp,
)
from pytket.circuit.logic_exp import (  # type: ignore
    BitWiseOp,
    RegAdd,
    RegAnd,
    RegEq,
    RegGeq,
    RegGt,
    RegLeq,
    RegLt,
    RegNeq,
    RegSub,
    RegMul,
    RegOr,
    RegLsh,
    RegRsh,
    RegXor,
)

from pyqir.generator import SimpleModule, IntPredicate, types  # type: ignore
from pyqir.generator.types import Qubit, Result  # type: ignore

from pytket_qir.gatesets.base import (
    CustomGateSet,
    CustomQirGate,
    OpNat,
    OpSpec,
    QirGate,
)
from pytket_qir.gatesets.pyqir import PYQIR_GATES, _TK_TO_PYQIR  # type: ignore
from pytket_qir.module import Module
from pytket_qir.utils import QIRFormat  # type: ignore


_TK_CLOPS_TO_PYQIR: Dict = {
    RegAnd: lambda b: b.and_,
    RegOr: lambda b: b.or_,
    RegXor: lambda b: b.xor,
    RegAdd: lambda b: b.add,
    RegSub: lambda b: b.sub,
    RegMul: lambda b: b.mul,
    RegLsh: lambda b: b.shl,
    RegRsh: lambda b: b.lshr,
    RegEq: lambda b: partial(b.icmp, IntPredicate.EQ),
    RegNeq: lambda b: partial(b.icmp, IntPredicate.NE),
    RegGt: lambda b: partial(b.icmp, IntPredicate.UGT),
    RegGeq: lambda b: partial(b.icmp, IntPredicate.UGE),
    RegLt: lambda b: partial(b.icmp, IntPredicate.ULT),
    RegLeq: lambda b: partial(b.icmp, IntPredicate.ULE),
}


class CommandUnsupportedError(Exception):
    pass


def _get_optype_and_params(op: Op) -> Tuple[OpType, Sequence[float]]:
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


def _to_qis_qubits(qubits: List[Qubit], mod: SimpleModule) -> Sequence[Qubit]:
    return [mod.qubits[qubit.index[0]] for qubit in qubits]


def _to_qis_results(bits: List[Bit], mod: SimpleModule) -> Optional[Result]:
    if bits:
        return mod.results[bits[0].index[0]]
    return None


def _to_qis_bits(args: List[Bit], mod: SimpleModule) -> Sequence[Result]:
    if args:
        return [mod.results[bit.index[0]] for bit in args[:-1]]
    return []


class QIRGenerator:
    """Generate QIR from a pytket circuit."""

    def __init__(self, circuit: Circuit, module: Module) -> None:
        self.circuit = circuit
        self.module = module
        self.cregs = _retrieve_registers(self.circuit.bits, BitRegister)
        self.set_cregs: Dict[str, List] = {}  # Keep track of set registers.
        self.ssa_vars: Dict[str, Callable] = {}  # Keep track of set ssa variables.
        self.reg2var = self.module.module.add_external_function(
            "reg2var", types.Function([types.BOOL] * 64, types.Int(64))
        )
        self.populated_module = self.circuit_to_module(circuit, self.module)

    def _reg2ssa_var(self, bit_reg: BitRegister) -> Callable:
        """Convert a BitRegister to an SSA variable via pyqir types."""
        # Check the register has been previously set.
        reg_name = bit_reg[0].reg_name
        if reg_name not in self.ssa_vars.keys():
            if reg_value := self.set_cregs.get(reg_name):
                bit_reg = reg_value
            if (size := len(bit_reg)) <= 64:  # Widening by zero-padding.
                bool_reg = list(map(bool, bit_reg)) + [False] * (64 - size)
            else:  # Narrowing by truncation.
                bool_reg = list(map(bool, bit_reg[:64]))
            ssa_var = self.module.builder.call(self.reg2var, [*bool_reg])
            self.ssa_vars[reg_name] = ssa_var
            return ssa_var
        else:
            return self.ssa_vars[reg_name]

    def _get_c_regs_from_com(self, command: Command) -> Tuple[List[str], List[str]]:
        """Get classical registers for several command op types."""
        op = command.op
        args = command.args
        inputs: List[str] = []
        outputs: List[str] = []

        if isinstance(op, WASMOp):
            for reglist, sizes in [
                (inputs, op.input_widths),
                (outputs, op.output_widths),
            ]:
                for in_width in sizes:
                    assert in_width > 0
                    com_bits = args[:in_width]
                    args = args[in_width:]
                    regname = com_bits[0].reg_name
                    if com_bits != list(self.cregs[regname]):
                        CommandUnsupportedError(
                            "Command ops must act on entire registers."
                        )
                    reglist.append(regname)
        elif isinstance(op, ClassicalExpBox):
            for reglist, sizes in [
                (
                    inputs,
                    list(
                        map(
                            lambda obj: obj.size
                            if isinstance(obj, BitRegister)
                            else None,
                            op.get_exp().args,
                        )
                    ),
                ),
                (outputs, [op.get_n_o()]),
            ]:
                if not sizes:
                    ValueError(
                        "Command op input or output registers have empty widths."
                    )
                for in_width in sizes:
                    com_bits = args[:in_width]
                    args = args[in_width:]
                    regname = com_bits[0].reg_name
                    if com_bits != list(self.cregs[regname]):
                        CommandUnsupportedError(
                            "Command ops must act on entire registers."
                        )
                    reglist.append(regname)
        elif isinstance(op, SetBitsOp):
            for reglist, sizes in [
                (inputs, [op.n_inputs]),
                (outputs, [op.n_outputs]),
            ]:
                for in_width in sizes:
                    if in_width > 0:
                        com_bits = args[:in_width]
                        args = args[in_width:]
                        regname = com_bits[0].reg_name
                        if com_bits != list(self.cregs[regname]):
                            CommandUnsupportedError(
                                "Command ops must act on entire registers."
                            )
                        reglist.append(regname)
        return inputs, outputs

    def circuit_to_module(self, circ: Circuit, module: Module) -> Module:
        """Populate a PyQir module from a pytket circuit."""
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
                        self.circuit_to_module(conditional_circuit, module)

                def condition_zero_block():
                    """
                    Populate recursively the module with the contents of the conditional
                    sub-circuit when the condition is False.
                    """
                    if op.value == 0:
                        self.circuit_to_module(conditional_circuit, module)

                module.qis.if_result(
                    module.module.results[condition_bit_index],
                    one=lambda: condition_one_block(),
                    zero=lambda: condition_zero_block(),
                )
            elif isinstance(op, WASMOp):
                inputs, _ = self._get_c_regs_from_com(command)
                bit_reg = circ.get_c_register(inputs[0])

                # Need to create a singleton enum to hold the WASM function name.
                class ExtOpName(Enum):
                    WASM = op.func_name

                # Update datastructures with WASM function name and
                # appropriate definition.

                # Update translation dict.
                _TK_TO_PYQIR[OpType.WASM] = QirGate(
                    opnat=OpNat.HYBRID, opname=ExtOpName.WASM, opspec=OpSpec.BODY
                )

                # Update gateset.
                gateset = PYQIR_GATES.gateset
                gateset["wasm"] = CustomQirGate(
                    opnat=OpNat.HYBRID,
                    opname=ExtOpName.WASM,
                    opspec=OpSpec.BODY,
                    function_signature=[types.Int(64)],
                    return_type=types.Int(64),
                )

                # Update gateset in module.
                module.gateset = PYQIR_GATES

                # Convert a bool register to an ssa variable.
                ssa_var = self._reg2ssa_var(bit_reg)
                assert ssa_var

                gate = module.gateset.tk_to_gateset(op.type)
                get_gate = getattr(module, gate.opname.value)
                module.builder.call(get_gate, [ssa_var])
            elif isinstance(op, ClassicalExpBox):
                inputs, _ = self._get_c_regs_from_com(command)

                ssa_vars: List = []
                for inp in inputs:
                    bit_reg = circ.get_c_register(inp)
                    ssa_vars.append(self._reg2ssa_var(bit_reg))

                _TK_CLOPS_TO_PYQIR[type(op.get_exp())](module.builder)(*ssa_vars)
            elif isinstance(op, SetBitsOp):
                inputs, outputs = self._get_c_regs_from_com(command)
                for out in outputs:
                    self.set_cregs[out] = command.op.values
            else:
                optype, params = _get_optype_and_params(op)
                qubits = _to_qis_qubits(command.qubits, module.module)
                results = _to_qis_results(command.bits, module.module)
                if module.gateset.name == "PyQir":
                    pyqir_gate = module.gateset.tk_to_gateset(optype)
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
                else:
                    bits: Optional[Sequence[Result]] = None
                    if type(optype) == BitWiseOp:
                        bits = _to_qis_bits(command.args, module.module)
                    gate = module.gateset.tk_to_gateset(optype)
                    get_gate = getattr(module, gate.opname.value)
                    if bits:
                        module.builder.call(get_gate, bits)  # type: ignore
                    elif params:
                        module.builder.call(get_gate, [*params, *qubits])
                    elif results:
                        module.builder.call(get_gate, [*qubits, results])  # type: ignore
                    else:
                        module.builder.call(get_gate, qubits)
        return module


def circuit_to_qir(
    circ: Circuit,
    gateset: Optional[CustomGateSet] = None,
    wasm_path: Optional[Union[str, os.PathLike]] = None,
    qir_format: Optional[QIRFormat] = QIRFormat.BITCODE,
) -> Union[str, bytes]:
    """Return QIR from a pytket circuit."""
    wasm_handler = None
    if wasm_path:
        try:
            wasm_handler = WasmFileHandler(str(wasm_path))
        except ValueError as ve:
            raise ve
    module = Module(
        name="Pytket circuit",
        num_qubits=circ.n_qubits,
        num_results=len(circ.bits),
        gateset=gateset,
        wasm_handler=wasm_handler,
    )
    populated_module = QIRGenerator(circ, module).populated_module
    if qir_format == QIRFormat.BITCODE:
        return populated_module.module.bitcode()
    else:
        return populated_module.module.ir()


def write_qir_file(
    circ: Circuit,
    file_name: str,
    gateset: Optional[CustomGateSet] = None,
    wasm_path: Optional[Union[str, os.PathLike]] = None,
) -> None:
    """Generate a QIR file from a pytket circuit."""
    _, ext = os.path.splitext(os.path.basename(file_name))
    if ext == ".bc":
        qir_format = QIRFormat.BITCODE
        file_param = "wb"
    elif ext == ".ll":
        qir_format = QIRFormat.IR
        file_param = "w"
    else:
        raise ValueError("The file extension should either be '.ll' or '.bc'.")
    qir = circuit_to_qir(
        circ=circ,
        gateset=gateset,
        wasm_path=wasm_path,
        qir_format=qir_format,
    )
    with open(file_name, file_param) as out:
        out.write(qir)
