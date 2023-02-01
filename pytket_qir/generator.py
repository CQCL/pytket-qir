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
import json
from functools import partial
import re
from typing import cast, Dict, List, Optional, Sequence, Tuple

from pytket import Circuit, OpType, Bit, Qubit  # type: ignore
from pytket.qasm.qasm import _retrieve_registers  # type: ignore
from pytket.circuit import (  # type: ignore
    BitRegister,
    ClassicalExpBox,
    Command,
    Conditional,
    CopyBitsOp,
    Op,
    MetaOp,
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
from pytket.passes import auto_rebase_pass  # type: ignore

from pyqir.generator import const, IntPredicate, types  # type: ignore
from pyqir.generator.types import Qubit  # type: ignore
from pyqir.generator._native import Value  # type: ignore

from pytket_qir.gatesets.base import (
    CustomQirGate,
    FuncNat,
    FuncSpec,
    QirGate,
)
from pytket_qir.gatesets.pyqir import PYQIR_GATES, _TK_TO_PYQIR  # type: ignore
from pytket_qir.module import Module
from pytket_qir.utils import (  # type: ignore
    ClassicalExpBoxError,
    SetBitsOpError,
    WASMError,
    BarrierError,
)


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


class QirGenerator:
    """Generate QIR from a pytket circuit."""

    def __init__(
        self,
        circuit: Circuit,
        module: Module,
        wasm_int_type: types.Int,
        qir_int_type: types.Int,
    ) -> None:
        self.circuit = circuit
        self.module = module
        self.wasm_int_type = wasm_int_type
        self.qir_int_type = qir_int_type
        self.cregs = _retrieve_registers(self.circuit.bits, BitRegister)
        self.target_gateset = self.module.gateset.base_gateset
        # Will throw an exception if the rebase can not handle the target gateset.
        self.rebase_to_gateset = auto_rebase_pass(self.target_gateset)
        self.set_cregs: Dict[str, List] = {}  # Keep track of set registers.
        self.ssa_vars: Dict[str, Value] = {}  # Keep track of set ssa variables.

    def _rebase_to_gateset(self, command: Command) -> Optional[Circuit]:
        """Rebase to the target gateset if needed."""
        optype = command.op.type
        params = command.op.params
        args = command.args
        if optype not in self.module.gateset.base_gateset:
            circuit = Circuit(self.circuit.n_qubits, self.circuit.n_bits)
            circuit.add_gate(optype, params, args)
            self.rebase_to_gateset.apply(circuit)
            return circuit
        return None

    def _get_optype_and_params(self, op: Op) -> Tuple[OpType, Sequence[float]]:
        optype = op.type
        params: List = []
        if optype == OpType.ExplicitPredicate:
            if op.get_name() == "AND":
                optype = BitWiseOp.AND
            elif op.get_name() == "OR":
                optype = BitWiseOp.OR
            elif op.get_name() == "XOR":
                optype = BitWiseOp.XOR
        elif optype in [OpType.Barrier, OpType.CopyBits]:
            pass
        else:
            params = op.params
        return (optype, params)

    def _to_qis_qubits(self, qubits: List[Qubit]) -> Sequence[Qubit]:
        return [self.module.module.qubits[qubit.index[0]] for qubit in qubits]

    def _to_qis_results(self, bits: List[Bit]) -> Optional[Value]:
        if bits:
            return self.module.module.results[bits[0].index[0]]
        return None

    def _to_qis_bits(self, args: List[Bit]) -> Sequence[Value]:
        if args:
            return [self.module.module.results[bit.index[0]] for bit in args[:-1]]
        return []

    def _reg2ssa_var(self, bit_reg: BitRegister, int_size: int) -> Value:
        """Convert a BitRegister to an SSA variable using pyqir types."""
        reg_name = bit_reg[0].reg_name
        if (
            reg_name not in self.ssa_vars.keys()
        ):  # Check if the register has been previously set.
            reg2var = self.module.module.add_external_function(
                "reg2var",
                types.Function(
                    [types.BOOL] * int_size,
                    types.Int(int_size),
                ),
            )
            # Check if the register has been previously set. If not, initialise to 0.
            if reg_value := self.set_cregs.get(reg_name):
                bit_reg = reg_value
                value = sum([n * 2**k for k, n in enumerate(reg_value)])
                return const(types.Int(64), value)
            else:
                bit_reg = [False] * len(bit_reg)
            if (size := len(bit_reg)) <= int_size:  # Widening by zero-padding.
                bool_reg = bit_reg + [False] * (int_size - size)
            else:  # Narrowing by truncation.
                bool_reg = bit_reg[:int_size]
            ssa_var = cast(Value, self.module.builder.call(reg2var, [*bool_reg]))
            self.ssa_vars[reg_name] = ssa_var
            return ssa_var
        else:
            return cast(Value, self.ssa_vars[reg_name])

    def _get_c_regs_from_com(self, command: Command) -> Tuple[List[str], List[str]]:
        """Get classical registers from command op types."""
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
                        WASMError("WASM ops must act on entire registers.")
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
                for in_width in sizes:
                    if in_width == 0:
                        raise ClassicalExpBoxError(
                            "ClassicalExpBox op input or output \
                            registers have empty widths."
                        )
                    com_bits = args[:in_width]
                    args = args[in_width:]
                    regname = com_bits[0].reg_name
                    if com_bits != list(self.cregs[regname]):
                        ClassicalExpBoxError(
                            "ClassicalExpBox ops must act on entire registers."
                        )
                    reglist.append(regname)
        elif isinstance(op, SetBitsOp):
            for reglist, sizes in [
                (outputs, [op.n_outputs]),
            ]:
                for in_width in sizes:
                    if in_width == 0:
                        raise SetBitsOpError(
                            "A value is getting assigned to an empty register."
                        )
                    com_bits = args[:in_width]
                    args = args[in_width:]
                    regname = com_bits[0].reg_name
                    if com_bits != list(self.cregs[regname]):
                        SetBitsOpError("SetBitOp must act on entire registers.")
                    reglist.append(regname)
        return inputs, outputs

    def circuit_to_module(self, circuit: Circuit, module: Module) -> Module:
        """Populate a PyQir module from a pytket circuit."""
        for command in circuit:
            op = command.op
            if isinstance(op, Conditional):
                # Only supports measurements now as it searches through self.set_vars
                # for SSA variables as conditions.
                # These are set when parsing CopyBits for measurement conversion to i1.
                # Conditions using other types (bools as results of classical
                # arithmetic) can be supported by adding the variable appropriately.
                conditional_circuit = op.op.get_circuit()
                condition_bit_index = command.args[0].index[0]
                condition_name = command.args[0].reg_name

                if ssa_var := self.ssa_vars.get(condition_name):
                    condition_ssa = ssa_var
                else:
                    condition_ssa = module.module.results[condition_bit_index]

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

                module.module.builder.if_(
                    condition_ssa,
                    true=lambda: condition_one_block(),
                    false=lambda: condition_zero_block(),
                )
            elif isinstance(op, WASMOp):
                inputs, _ = self._get_c_regs_from_com(command)
                input_type_list: List
                try:
                    bit_reg = circuit.get_c_register(inputs[0])
                    input_type_list = [self.wasm_int_type]
                except IndexError:
                    input_type_list = []

                # Need to create a singleton enum to hold the WASM function name.
                WasmName = Enum("WasmName", [("WASM", op.func_name)])

                # Update datastructures with WASM function name and
                # appropriate definition.

                # Update translation dict.
                _TK_TO_PYQIR[OpType.WASM] = QirGate(
                    func_nat=FuncNat.HYBRID,
                    func_name=WasmName.WASM,
                    func_spec=FuncSpec.BODY,
                )

                # Update gateset.
                gateset = PYQIR_GATES.gateset
                gateset["wasm"] = CustomQirGate(
                    func_nat=FuncNat.HYBRID,
                    func_name=WasmName.WASM,
                    func_spec=FuncSpec.BODY,
                    function_signature=input_type_list,
                    return_type=self.wasm_int_type,
                )

                # Update gateset in module.
                module.gateset = PYQIR_GATES

                # Create an ssa variable if there is an input to the WASMOp.
                if len(input_type_list) == 0:
                    ssa_args = []
                else:
                    ssa_args = [self._reg2ssa_var(bit_reg, self.wasm_int_type.width)]

                gate = module.gateset.tk_to_gateset(op.type)
                get_gate = getattr(module, gate.func_name.value)
                module.builder.call(get_gate, ssa_args)
            elif isinstance(op, ClassicalExpBox):
                inputs, outputs = self._get_c_regs_from_com(command)
                ssa_vars: List = []
                for inp in inputs:
                    bit_reg = circuit.get_c_register(inp)
                    ssa_vars.append(self._reg2ssa_var(bit_reg, self.qir_int_type.width))
                output_instr = _TK_CLOPS_TO_PYQIR[type(op.get_exp())](module.builder)(
                    *ssa_vars
                )
                self.ssa_vars[outputs[0]] = output_instr
            elif isinstance(op, SetBitsOp):
                _, outputs = self._get_c_regs_from_com(command)
                for out in outputs:
                    self.set_cregs[out] = command.op.values
            elif isinstance(op, MetaOp):
                optype, _ = self._get_optype_and_params(op)
                gate = module.gateset.tk_to_gateset(optype)
                get_gate = getattr(module, gate.func_name.value)
                data = json.loads(op.data)
                func_name = cast(str, data["name"])
                matched_str = re.search("__quantum__(.+?)__(.+?)_(.+)", func_name)
                if not matched_str:
                    raise BarrierError(
                        "The runtime function name is not properly defined."
                    )
                if matched_str.group(2) == "result":
                    res_index = data["index"]
                    ssa_var = cast(Value, self.module.module.results[res_index])
                else:
                    ssa_var_name = data["arg"]
                    ssa_var = cast(Value, self.ssa_vars[ssa_var_name])
                module.builder.call(get_gate, [ssa_var])
            elif isinstance(op, CopyBitsOp):
                input_reg = command.args[0]
                output_reg = command.args[1]
                output_name = output_reg.reg_name
                optype, _ = self._get_optype_and_params(op)
                gate = module.gateset.tk_to_gateset(optype)
                ssa_var = cast(Value, self.module.module.results[input_reg.index[0]])
                get_gate = getattr(module, gate.func_name.value)
                output_instr = module.builder.call(get_gate, [ssa_var])
                self.ssa_vars[output_name] = output_instr
            else:
                rebased_circ = self._rebase_to_gateset(
                    command
                )  # Check if the command must be rebased.
                if rebased_circ is not None:
                    self.circuit_to_module(rebased_circ, module)
                else:
                    optype, params = self._get_optype_and_params(op)
                    qubits = self._to_qis_qubits(command.qubits)
                    results = self._to_qis_results(command.bits)
                    bits: Optional[Sequence[Value]] = None
                    if type(optype) == BitWiseOp:
                        bits = self._to_qis_bits(command.args)
                    gate = module.gateset.tk_to_gateset(optype)
                    if not gate.func_spec == FuncSpec.BODY:
                        func_name = gate.func_name.value + "_" + gate.func_spec.value
                        get_gate = getattr(module.qis, func_name)
                    else:
                        get_gate = getattr(module.qis, gate.func_name.value)
                    if bits:
                        get_gate(*bits)
                    elif params:
                        get_gate(*params, *qubits)
                    elif results:
                        get_gate(*qubits, results)
                    else:
                        get_gate(*qubits)
        return module

    def command_to_module(
        self, command: Command, circuit: Circuit, module: Module
    ) -> Module:
        """Populate a PyQir module from a pytket circuit command."""
        op = command.op
        if isinstance(op, WASMOp):
            inputs, _ = self._get_c_regs_from_com(command)
            input_type_list: List
            try:
                bit_reg = circuit.get_c_register(inputs[0])
                input_type_list = [self.wasm_int_type]
            except IndexError:
                input_type_list = []

            # Need to create a singleton enum to hold the WASM function name.
            WasmName = Enum("WasmName", [("WASM", op.func_name)])

            # Update datastructures with WASM function name and
            # appropriate definition.

            # Update translation dict.
            _TK_TO_PYQIR[OpType.WASM] = QirGate(
                func_nat=FuncNat.HYBRID,
                func_name=WasmName.WASM,
                func_spec=FuncSpec.BODY,
            )

            # Update gateset.
            gateset = PYQIR_GATES.gateset
            gateset["wasm"] = CustomQirGate(
                func_nat=FuncNat.HYBRID,
                func_name=WasmName.WASM,
                func_spec=FuncSpec.BODY,
                function_signature=input_type_list,
                return_type=self.wasm_int_type,
            )

            # Update gateset in module.
            module.gateset = PYQIR_GATES

            # Create an ssa variable if there is an input to the WASMOp.
            if len(input_type_list) == 0:
                ssa_args = []
            else:
                ssa_args = [self._reg2ssa_var(bit_reg, self.wasm_int_type.width)]

            gate = module.gateset.tk_to_gateset(op.type)
            get_gate = getattr(module, gate.func_name.value)
            module.builder.call(get_gate, ssa_args)
        elif isinstance(op, MetaOp):
            optype, _ = self._get_optype_and_params(op)
            gate = module.gateset.tk_to_gateset(optype)
            get_gate = getattr(module, gate.func_name.value)
            data = json.loads(op.data)
            func_name = cast(str, data["name"])
            matched_str = re.search("__quantum__(.+?)__(.+?)_(.+)", func_name)
            if not matched_str:
                raise BarrierError("The runtime function name is not properly defined.")
            if matched_str.group(2) == "result":
                res_index = data["index"]
                ssa_var = cast(Value, self.module.module.results[res_index])
            else:
                ssa_var_name = data["arg"]
                ssa_var = cast(Value, self.ssa_vars[ssa_var_name])
            module.builder.call(get_gate, [ssa_var])
        elif isinstance(op, CopyBitsOp):
            input_reg = command.args[0]
            output_reg = command.args[1]
            output_name = output_reg.reg_name
            optype, _ = self._get_optype_and_params(op)
            gate = module.gateset.tk_to_gateset(optype)
            ssa_var = cast(Value, self.module.module.results[input_reg.index[0]])
            get_gate = getattr(module, gate.func_name.value)
            output_instr = cast(Value, module.builder.call(get_gate, [ssa_var]))
            self.ssa_vars[output_name] = output_instr
        else:
            rebased_circ = self._rebase_to_gateset(
                command
            )  # Check if the command must be rebased.
            if rebased_circ is not None:
                self.circuit_to_module(rebased_circ, module)
            else:
                optype, params = self._get_optype_and_params(op)
                qubits = self._to_qis_qubits(command.qubits)
                results = self._to_qis_results(command.bits)
                bits: Optional[Sequence[Value]] = None
                if type(optype) == BitWiseOp:
                    bits = self._to_qis_bits(command.args)
                gate = module.gateset.tk_to_gateset(optype)
                if not gate.func_spec == FuncSpec.BODY:
                    func_name = gate.func_name.value + "_" + gate.func_spec.value
                    get_gate = getattr(module.qis, func_name)
                else:
                    get_gate = getattr(module.qis, gate.func_name.value)
                if bits:
                    get_gate(*bits)
                elif params:
                    get_gate(*params, *qubits)
                elif results:
                    get_gate(*qubits, results)
                else:
                    get_gate(*qubits)
        return module
