# Copyright 2019-2024 Quantinuum
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
This module contains all functionality to generate QIR files
from pytket circuits.
"""

import math
from collections.abc import Sequence
from functools import partial
from typing import Optional, Union, cast

import pyqir
from pyqir import IntPredicate, Value

from pytket import Bit, Circuit, Qubit, predicates, wasm  # type: ignore
from pytket.circuit import (
    BarrierOp,
    BitRegister,
    ClassicalExpBox,
    Command,
    Conditional,
    CopyBitsOp,
    Op,
    OpType,
    RangePredicateOp,
    SetBitsOp,
    WASMOp,
)
from pytket.circuit.logic_exp import (
    BitAnd,
    BitEq,
    BitNeq,
    BitOne,
    BitOr,
    BitWiseOp,
    BitXor,
    BitZero,
    RegAdd,
    RegAnd,
    RegEq,
    RegGeq,
    RegGt,
    RegLeq,
    RegLsh,
    RegLt,
    RegMul,
    RegNeq,
    RegOr,
    RegRsh,
    RegSub,
    RegXor,
)
from pytket.qasm.qasm import _retrieve_registers
from pytket.transform import Transform
from pytket.unit_id import UnitType

from .gatesets import (
    FuncSpec,
)
from .module import tketqirModule

_TK_CLOPS_TO_PYQIR_REG: dict = {
    RegAnd: lambda b: b.and_,
    RegOr: lambda b: b.or_,
    RegXor: lambda b: b.xor,
    RegAdd: lambda b: b.add,
    RegSub: lambda b: b.sub,
    RegMul: lambda b: b.mul,
    RegLsh: lambda b: b.shl,
    RegRsh: lambda b: b.lshr,
}

_TK_CLOPS_TO_PYQIR_REG_BOOL: dict = {
    RegEq: lambda b: partial(b.icmp, IntPredicate.EQ),
    RegNeq: lambda b: partial(b.icmp, IntPredicate.NE),
    RegGt: lambda b: partial(b.icmp, IntPredicate.UGT),
    RegGeq: lambda b: partial(b.icmp, IntPredicate.UGE),
    RegLt: lambda b: partial(b.icmp, IntPredicate.ULT),
    RegLeq: lambda b: partial(b.icmp, IntPredicate.ULE),
}

_TK_CLOPS_TO_PYQIR_BIT: dict = {
    BitAnd: lambda b: b.and_,
    BitOr: lambda b: b.or_,
    BitXor: lambda b: b.xor,
    BitNeq: lambda b: partial(b.icmp, IntPredicate.NE),
    BitEq: lambda b: partial(b.icmp, IntPredicate.EQ),
}

_TK_CLOPS_TO_PYQIR_BIT_NO_PARAM: dict = {
    BitOne: 1,
    BitZero: 0,
}


class QirGenerator:
    """Generate QIR from a pytket circuit."""

    def __init__(
        self,
        circuit: Circuit,
        module: tketqirModule,
        wasm_int_type: int,
        qir_int_type: int,
        wfh: Optional[wasm.WasmFileHandler] = None,
    ) -> None:
        self.circuit = circuit
        self.module = module
        self.wasm_int_type = pyqir.IntType(self.module.context, wasm_int_type)
        self.qir_int_type = pyqir.IntType(self.module.context, qir_int_type)
        self.qir_i1p_type = pyqir.PointerType(pyqir.IntType(self.module.context, 1))
        self.qir_bool_type = pyqir.IntType(self.module.context, 1)
        self.qubit_type = pyqir.qubit_type(self.module.context)
        self.result_type = pyqir.result_type(self.module.context)

        self.cregs = _retrieve_registers(self.circuit.bits, BitRegister)
        self.target_gateset = self.module.gateset.base_gateset

        self.wasm_sar_dict: dict[str, str] = {}
        self.wasm_sar_dict[
            "!llvm.module.flags"
        ] = 'attributes #1 = { "wasm" }\n\n!llvm.module.flags'
        self.int_type_str = f"i{qir_int_type}"

        self.target_gateset.add(OpType.PhasedX)
        self.target_gateset.add(OpType.ZZPhase)
        self.target_gateset.add(OpType.ZZMax)
        self.target_gateset.add(OpType.TK2)

        self.getset_predicate = predicates.GateSetPredicate(
            set(self.target_gateset)
        )  # noqa: E501

        self.set_cregs: dict[str, list] = {}  # Keep track of set registers.
        self.ssa_vars: dict[str, Value] = {}  # Keep track of set ssa variables.

        # i1 get_creg_bit(i1* creg, i64 index)
        self.get_creg_bit = self.module.module.add_external_function(
            "get_creg_bit",
            pyqir.FunctionType(
                pyqir.IntType(self.module.module.context, 1),
                [self.qir_i1p_type, self.qir_int_type],
            ),
        )

        # void set_creg_bit(i1* creg, i64 index, i1 value)
        self.set_creg_bit = self.module.module.add_external_function(
            "set_creg_bit",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [
                    self.qir_i1p_type,
                    self.qir_int_type,
                    pyqir.IntType(self.module.module.context, 1),
                ],
            ),
        )

        # void set_creg_to_int(i1* creg, i64 value)
        self.set_creg_to_int = self.module.module.add_external_function(
            "set_creg_to_int",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [
                    self.qir_i1p_type,
                    self.qir_int_type,
                ],
            ),
        )

        # __quantum__qis__read_result__body(result)
        self.read_bit_from_result = self.module.module.add_external_function(
            "__quantum__qis__read_result__body",
            pyqir.FunctionType(
                pyqir.IntType(self.module.module.context, 1),
                [pyqir.result_type(self.module.module.context)],
            ),
        )

        # i1* create_creg(i64 size)
        self.create_creg = self.module.module.add_external_function(
            "create_creg",
            pyqir.FunctionType(
                self.qir_i1p_type,
                [pyqir.IntType(self.module.module.context, qir_int_type)],
            ),
        )

        # i64 get_int_from_creg(i1* creg)
        self.get_int_from_creg = self.module.module.add_external_function(
            "get_int_from_creg",
            pyqir.FunctionType(
                self.qir_int_type,
                [
                    self.qir_i1p_type,
                ],
            ),
        )

        # void mz_to_creg_bit(qubit, i1* creg, int creg_index)
        # measures one qubit to one bit entry in a creg
        self.mz_to_creg_bit = self.module.module.add_external_function(
            "mz_to_creg_bit",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [
                    pyqir.qubit_type(self.module.module.context),
                    self.qir_i1p_type,
                    self.qir_int_type,
                ],
            ),
        )

        self.reg_const = {}

        for creg in self.circuit.c_registers:
            reg_name = creg[0].reg_name
            self.reg_const[reg_name] = self.module.module.add_byte_string(
                str.encode(reg_name)
            )

            # void __quantum__rt__int_record_output(i64)
        self.record_output_i64 = self.module.module.add_external_function(
            "__quantum__rt__int_record_output",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [
                    pyqir.IntType(self.module.module.context, qir_int_type),
                    pyqir.PointerType(pyqir.IntType(self.module.module.context, 8)),
                ],
            ),
        )

        # void __quantum__rt__tuple_start_record_output()
        self.record_output_start = self.module.module.add_external_function(
            "__quantum__rt__tuple_start_record_output",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [],
            ),
        )

        # void __quantum__rt__tuple_end_record_output()
        self.record_output_end = self.module.module.add_external_function(
            "__quantum__rt__tuple_end_record_output",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [],
            ),
        )

        self.barrier: list[Optional[pyqir.Function]] = [None] * (
            self.circuit.n_qubits + 1
        )
        self.order: list[Optional[pyqir.Function]] = [None] * (
            self.circuit.n_qubits + 1
        )
        self.group: list[Optional[pyqir.Function]] = [None] * (
            self.circuit.n_qubits + 1
        )
        self.sleep: list[Optional[pyqir.Function]] = [None] * (
            self.circuit.n_qubits + 1
        )

        # void functionname()
        if wfh is not None:
            self.wasm: dict[str, pyqir.Function] = {}
            for fn in wfh._functions:
                wasm_func_interface = "declare "
                parametertype = [self.qir_int_type] * wfh._functions[fn][0]
                if wfh._functions[fn][1] == 0:
                    returntype = pyqir.Type.void(self.module.module.context)
                    wasm_func_interface += "void "
                elif wfh._functions[fn][1] == 1:
                    returntype = self.qir_int_type
                    wasm_func_interface += f"{self.int_type_str} "
                else:
                    raise ValueError(
                        "wasm function which return more than"
                        + " one value are not supported yet"
                    )

                self.wasm[fn] = self.module.module.add_external_function(
                    f"{fn}",
                    pyqir.FunctionType(
                        returntype,
                        parametertype,
                    ),
                )

                wasm_func_interface += f"@{fn}("
                if wfh._functions[fn][0] > 0:
                    param_str = f"{self.int_type_str}, " * (wfh._functions[fn][0] - 1)
                    wasm_func_interface += param_str
                    wasm_func_interface += f"{self.int_type_str})"
                else:
                    wasm_func_interface += ")"

                self.wasm_sar_dict[wasm_func_interface] = f"{wasm_func_interface} #1"

        self.additional_quantum_gates: dict[OpType, pyqir.Function] = {}

        for creg in self.circuit.c_registers:
            self._reg2ssa_var(creg, qir_int_type)

    def get_ssa_vars(self, reg_name: str) -> Value:
        if reg_name not in self.ssa_vars:
            raise ValueError(f"{reg_name} is not a valid register")
        return self.ssa_vars[reg_name]

    def _add_barrier_op(
        self, module: tketqirModule, index: int, qir_qubits: Sequence
    ) -> None:
        # __quantum__qis__barrier1__body()
        if self.barrier[index] is None:
            self.barrier[index] = self.module.module.add_external_function(
                f"__quantum__qis__barrier{index}__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [pyqir.qubit_type(self.module.module.context)] * index,
                ),
            )

        module.builder.call(
            self.barrier[index],  # type: ignore
            [*qir_qubits],
        )

    def _add_group_op(
        self, module: tketqirModule, index: int, qir_qubits: Sequence
    ) -> None:
        # __quantum__qis__group1__body()
        if self.group[index] is None:
            self.group[index] = self.module.module.add_external_function(
                f"__quantum__qis__group{index}__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [pyqir.qubit_type(self.module.module.context)] * index,
                ),
            )

        module.builder.call(
            self.group[index],  # type: ignore
            [*qir_qubits],
        )

    def _add_order_op(
        self, module: tketqirModule, index: int, qir_qubits: Sequence
    ) -> None:
        # __quantum__qis__order1__body()
        if self.order[index] is None:
            self.order[index] = self.module.module.add_external_function(
                f"__quantum__qis__order{index}__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [pyqir.qubit_type(self.module.module.context)] * index,
                ),
            )

        module.builder.call(
            self.order[index],  # type: ignore
            [*qir_qubits],
        )

    def _add_sleep_op(
        self, module: tketqirModule, index: int, qir_qubits: Sequence, duration: float
    ) -> None:
        # __quantum__qis__sleep__body()

        if index > 1:
            raise ValueError("Sleep operation only allowed on one qubit")

        if self.sleep[index] is None:
            paramlist = [pyqir.qubit_type(self.module.module.context)] * index
            paramlist.append(
                pyqir.Type.double(self.module.module.context)
            )  # add float parameter
            self.sleep[index] = self.module.module.add_external_function(
                "__quantum__qis__sleep__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    paramlist,
                ),
            )

        module.builder.call(
            self.sleep[index],  # type: ignore
            [
                *qir_qubits,
                pyqir.const(pyqir.Type.double(self.module.module.context), duration),
            ],
        )

    def _rebase_command_to_gateset(self, command: Command) -> Optional[Circuit]:
        """Rebase to the target gateset if needed."""
        optype = command.op.type
        params = command.op.params
        args = command.args
        if optype not in self.module.gateset.base_gateset:
            circuit = Circuit(self.circuit.n_qubits, self.circuit.n_bits)
            circuit.add_gate(optype, params, args)
            if not self.getset_predicate.verify(circuit):
                raise ValueError(f"Gate not supported {optype}, {params}, {args}")
            return circuit
        return None

    def _decompose_conditional_circ_box(self, op: Op, args: list) -> Optional[Circuit]:
        """Rebase an op to the target gateset if needed."""
        circuit = Circuit(self.circuit.n_qubits)
        arg_names = set([b.reg_name for b in args if type(b) == Bit])
        for cr_name in arg_names:
            circuit.add_c_register(self.circuit.get_c_register(cr_name))

        circuit.add_circbox(op, args)
        Transform.DecomposeBoxes().apply(circuit)

        return circuit

    def _get_optype_and_params(self, op: Op) -> tuple[OpType, Sequence[float]]:
        optype: OpType = op.type
        params: list = []
        if optype in [OpType.ExplicitPredicate, OpType.Barrier, OpType.CopyBits]:
            pass
        else:
            params = op.params
        return (optype, params)

    def _get_i64_ssa_reg(self, name: str) -> Value:
        ssa_var = self.module.builder.call(
            self.get_int_from_creg,
            [self.get_ssa_vars(name)],
        )
        return ssa_var

    def _to_qis_qubits(self, qubits: list[Qubit]) -> list[Qubit]:
        return [self.module.module.qubits[qubit.index[0]] for qubit in qubits]

    def _to_qis_results(self, bits: list[Bit]) -> Optional[Value]:
        if bits:
            return self.module.module.results[bits[0].index[0]]  # type: ignore
        return None

    def _to_qis_bits(self, args: list[Bit]) -> Sequence[Value]:
        for b in args:
            assert b.name == "c"
        if args:
            return [self.module.module.results[bit.index[0]] for bit in args[:-1]]
        return []

    def _reg2ssa_var(self, bit_reg: BitRegister, int_size: int) -> Value:
        """Convert a BitRegister to an SSA variable using pyqir types."""
        reg_name = bit_reg[0].reg_name
        if reg_name not in self.ssa_vars:
            if len(bit_reg) > int_size:
                raise ValueError(
                    f"Classical register should only have the size of {int_size}"
                )
            ssa_var = self.module.builder.call(
                self.create_creg, [pyqir.const(self.qir_int_type, len(bit_reg))]
            )
            self.ssa_vars[reg_name] = ssa_var
            return ssa_var
        else:
            return cast(Value, self.ssa_vars[reg_name])  # type: ignore

    def _get_c_regs_from_com(
        self, op: Op, args: Union[Bit, Qubit]
    ) -> tuple[list[str], list[str]]:
        """Get classical registers from command op types."""
        inputs: list[str] = []
        outputs: list[str] = []

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
                        raise ValueError("WASM ops must act on entire registers.")
                    reglist.append(regname)
        return inputs, outputs

    def _get_ssa_from_cl_reg_op(
        self, reg: Union[BitRegister, RegAnd, RegOr, RegXor, int], module: tketqirModule
    ) -> Value:
        if type(reg) in _TK_CLOPS_TO_PYQIR_REG:
            assert len(reg.args) == 2  # type: ignore

            ssa_left = self._get_ssa_from_cl_reg_op(reg.args[0], module)  # type: ignore
            ssa_right = self._get_ssa_from_cl_reg_op(
                reg.args[1], module  # type: ignore
            )

            # add function to module
            output_instruction = _TK_CLOPS_TO_PYQIR_REG[type(reg)](module.builder)(
                ssa_left, ssa_right
            )
            return output_instruction  # type: ignore
        elif type(reg) == BitRegister:
            return self._get_i64_ssa_reg(reg.name)
        elif type(reg) == int:
            return pyqir.const(self.qir_int_type, reg)
        else:
            raise ValueError(f"unsupported classical register operation: {type(reg)}")

    def _get_ssa_from_cl_bit_op(
        self, bit: Union[Bit, BitAnd, BitOr, BitXor], module: tketqirModule
    ) -> Value:
        if type(bit) == Bit:
            result = module.builder.call(
                self.get_creg_bit,
                [
                    self.get_ssa_vars(bit.reg_name),
                    pyqir.const(self.qir_int_type, bit.index[0]),
                ],
            )

            return result
        elif type(bit) == int:
            return pyqir.const(self.qir_bool_type, bit)
        elif type(bit) in _TK_CLOPS_TO_PYQIR_BIT:
            assert len(bit.args) == 2

            ssa_left = self._get_ssa_from_cl_bit_op(bit.args[0], module)
            ssa_right = self._get_ssa_from_cl_bit_op(bit.args[1], module)

            # add function to module
            output_instruction = _TK_CLOPS_TO_PYQIR_BIT[type(bit)](module.builder)(
                ssa_left, ssa_right
            )

            return output_instruction  # type: ignore
        else:
            raise ValueError(f"unsupported bitwise operation {type(bit)}")

    def get_wasm_sar(self) -> dict[str, str]:
        return self.wasm_sar_dict

    def conv_RangePredicateOp(
        self, op: RangePredicateOp, args: Union[Bit, Qubit]
    ) -> None:
        # special case handling for REG_EQ

        if op.lower == op.upper:
            registername = args[0].reg_name

            result = self.module.module.builder.icmp(
                pyqir.IntPredicate.EQ,
                pyqir.const(self.qir_int_type, op.lower),
                self._get_i64_ssa_reg(registername),
            )

            condition_bit_index = args[-1].index[0]
            result_registername = args[-1].reg_name

            self.module.builder.call(
                self.set_creg_bit,
                [
                    self.get_ssa_vars(result_registername),
                    pyqir.const(self.qir_int_type, condition_bit_index),
                    result,
                ],
            )

        else:
            lower_qir = pyqir.const(self.qir_int_type, op.lower)
            upper_qir = pyqir.const(self.qir_int_type, op.upper)

            registername = args[0].reg_name

            lower_cond = self.module.module.builder.icmp(
                pyqir.IntPredicate.SGT,
                lower_qir,
                self._get_i64_ssa_reg(registername),
            )

            upper_cond = self.module.module.builder.icmp(
                pyqir.IntPredicate.SGT,
                self._get_i64_ssa_reg(registername),
                upper_qir,
            )

            result = self.module.module.builder.and_(lower_cond, upper_cond)

            condition_bit_index = args[-1].index[0]
            registername = args[-1].reg_name

            self.module.builder.call(
                self.set_creg_bit,
                [
                    self.get_ssa_vars(registername),
                    pyqir.const(self.qir_int_type, condition_bit_index),
                    result,
                ],
            )

    def conv_conditional(self, command: Command, op: Conditional) -> None:
        condition_name = command.args[0].reg_name

        if op.op.type == OpType.CircBox:
            conditional_circuit = self._decompose_conditional_circ_box(
                op.op, command.args[op.width :]
            )

            condition_name = command.args[0].reg_name

            if op.width == 1:  # only one conditional bit
                condition_bit_index = command.args[0].index[0]

                def condition_block_true() -> None:
                    """
                    Populate recursively the module with the contents of the
                    conditional sub-circuit when the condition is True.
                    """
                    if op.value == 1:
                        self.subcircuit_to_module(conditional_circuit)

                def condition_block_false() -> None:
                    """
                    Populate recursively the module with the contents of the
                    conditional sub-circuit when the condition is False.
                    """
                    if op.value == 0:
                        self.subcircuit_to_module(conditional_circuit)

                ssabool = self.module.builder.call(
                    self.get_creg_bit,
                    [
                        self.get_ssa_vars(condition_name),
                        pyqir.const(self.qir_int_type, condition_bit_index),
                    ],
                )

                self.module.module.builder.if_(
                    ssabool,
                    true=lambda: condition_block_true(),
                    false=lambda: condition_block_false(),
                )

            else:
                for i in range(op.width):
                    if command.args[i].reg_name != condition_name:
                        raise ValueError(
                            "conditional can only work with one entire register"
                        )

                for i in range(op.width - 1):
                    if command.args[i].index[0] >= command.args[i + 1].index[0]:
                        raise ValueError(
                            "conditional can only work with one entire register"
                        )

                if self.circuit.get_c_register(condition_name).size != op.width:
                    raise ValueError(
                        "conditional can only work with one entire register"
                    )

                def condition_block() -> None:
                    """
                    Populate recursively the module with the contents of the
                    conditional sub-circuit when the condition is True.
                    """
                    self.subcircuit_to_module(conditional_circuit)

                ssabool = self.module.module.builder.icmp(
                    pyqir.IntPredicate.EQ,
                    pyqir.const(self.qir_int_type, op.value),
                    self._get_i64_ssa_reg(condition_name),
                )

                self.module.module.builder.if_(
                    ssabool,
                    true=lambda: condition_block(),
                )
        else:
            condition_name = command.args[0].reg_name

            if op.width == 1:  # only one conditional bit
                condition_bit_index = command.args[0].index[0]

                def condition_block_true() -> None:
                    """
                    Populate recursively the module with the contents of the
                    conditional sub-circuit when the condition is True.
                    """
                    if op.value == 1:
                        self.command_to_module(op.op, command.args[op.width :])

                def condition_block_false() -> None:
                    """
                    Populate recursively the module with the contents of the
                    conditional sub-circuit when the condition is False.
                    """
                    if op.value == 0:
                        self.command_to_module(op.op, command.args[op.width :])

                ssabool = self.module.builder.call(
                    self.get_creg_bit,
                    [
                        self.get_ssa_vars(condition_name),
                        pyqir.const(self.qir_int_type, condition_bit_index),
                    ],
                )

                self.module.module.builder.if_(
                    ssabool,
                    true=lambda: condition_block_true(),
                    false=lambda: condition_block_false(),
                )

            else:
                for i in range(op.width):
                    if command.args[i].reg_name != condition_name:
                        raise ValueError(
                            "conditional can only work with one entire register"
                        )

                for i in range(op.width - 1):
                    if command.args[i].index[0] >= command.args[i + 1].index[0]:
                        raise ValueError(
                            "conditional can only work with one entire register"
                        )

                if self.circuit.get_c_register(condition_name).size != op.width:
                    raise ValueError(
                        "conditional can only work with one entire register"
                    )

                def condition_block() -> None:
                    """
                    Populate recursively the module with the contents of the
                    conditional sub-circuit when the condition is True.
                    """
                    self.command_to_module(op.op, command.args[op.width :])

                ssabool = self.module.module.builder.icmp(
                    pyqir.IntPredicate.EQ,
                    pyqir.const(self.qir_int_type, op.value),
                    self._get_i64_ssa_reg(condition_name),
                )

                self.module.module.builder.if_(
                    ssabool,
                    true=lambda: condition_block(),
                )

    def conv_WASMOp(self, op: WASMOp, args: Union[Bit, Qubit]) -> None:
        paramreg, resultreg = self._get_c_regs_from_com(op, args)

        paramssa = [self._get_i64_ssa_reg(p) for p in paramreg]

        result = self.module.builder.call(
            self.wasm[op.func_name],
            [*paramssa],
        )

        if len(resultreg) == 1:
            self.module.builder.call(
                self.set_creg_to_int,
                [self.get_ssa_vars(resultreg[0]), result],
            )

    def conv_ZZPhase(self, qubits: list[Qubit], op: Op) -> None:
        if OpType.ZZPhase not in self.additional_quantum_gates:
            self.additional_quantum_gates[
                OpType.ZZPhase
            ] = self.module.module.add_external_function(
                "__quantum__qis__rzz__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [
                        pyqir.Type.double(self.module.module.context),
                        pyqir.qubit_type(self.module.module.context),
                        pyqir.qubit_type(self.module.module.context),
                    ],
                ),
            )

        self.module.builder.call(
            self.additional_quantum_gates[OpType.ZZPhase],
            [
                pyqir.const(
                    pyqir.Type.double(self.module.module.context),
                    (float(op.params[0]) * math.pi),
                ),
                self.module.module.qubits[qubits[0].index[0]],
                self.module.module.qubits[qubits[1].index[0]],
            ],
        )

    def conv_phasedx(self, qubits: list[Qubit], op: Op) -> None:
        if OpType.PhasedX not in self.additional_quantum_gates:
            self.additional_quantum_gates[
                OpType.PhasedX
            ] = self.module.module.add_external_function(
                "__quantum__qis__phasedx__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [
                        pyqir.Type.double(self.module.module.context),
                        pyqir.Type.double(self.module.module.context),
                        pyqir.qubit_type(self.module.module.context),
                    ],
                ),
            )

        self.module.builder.call(
            self.additional_quantum_gates[OpType.PhasedX],
            [
                pyqir.const(
                    pyqir.Type.double(self.module.module.context),
                    (float(op.params[0]) * math.pi),
                ),
                pyqir.const(
                    pyqir.Type.double(self.module.module.context),
                    (float(op.params[1]) * math.pi),
                ),
                self.module.module.qubits[qubits[0].index[0]],
            ],
        )

    def conv_tk2(self, qubits: list[Qubit], op: Op) -> None:
        if OpType.TK2 not in self.additional_quantum_gates:
            self.additional_quantum_gates[
                OpType.TK2
            ] = self.module.module.add_external_function(
                "__quantum__qis__rxxyyzz__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [
                        pyqir.Type.double(self.module.module.context),
                        pyqir.Type.double(self.module.module.context),
                        pyqir.Type.double(self.module.module.context),
                        pyqir.qubit_type(self.module.module.context),
                        pyqir.qubit_type(self.module.module.context),
                    ],
                ),
            )

        self.module.builder.call(
            self.additional_quantum_gates[OpType.TK2],
            [
                pyqir.const(
                    pyqir.Type.double(self.module.module.context),
                    (float(op.params[0]) * math.pi),
                ),
                pyqir.const(
                    pyqir.Type.double(self.module.module.context),
                    (float(op.params[1]) * math.pi),
                ),
                pyqir.const(
                    pyqir.Type.double(self.module.module.context),
                    (float(op.params[2]) * math.pi),
                ),
                self.module.module.qubits[qubits[0].index[0]],
                self.module.module.qubits[qubits[1].index[0]],
            ],
        )

    def conv_zzmax(self, qubits: list[Qubit]) -> None:
        if OpType.ZZMax not in self.additional_quantum_gates:
            self.additional_quantum_gates[
                OpType.ZZMax
            ] = self.module.module.add_external_function(
                "__quantum__qis__zzmax__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [
                        pyqir.qubit_type(self.module.module.context),
                        pyqir.qubit_type(self.module.module.context),
                    ],
                ),
            )

        self.module.builder.call(
            self.additional_quantum_gates[OpType.ZZMax],
            [
                self.module.module.qubits[qubits[0].index[0]],
                self.module.module.qubits[qubits[1].index[0]],
            ],
        )

    def conv_measure(self, bits: list[Bit], qubits: list[Qubit]) -> None:
        self.module.builder.call(
            self.mz_to_creg_bit,
            [
                self.module.module.qubits[qubits[0].index[0]],
                self.get_ssa_vars(bits[0].reg_name),
                pyqir.const(self.qir_int_type, bits[0].index[0]),
            ],
        )

    def conv_classicalexpbox(self, op: ClassicalExpBox, args: list) -> None:
        returntypebool = False
        result_index = (
            0  # defines the default value for ops that returns bool, see below
        )

        outputs = args[-1].reg_name

        if type(op.get_exp()) in _TK_CLOPS_TO_PYQIR_REG:
            # classical ops acting on registers returning register
            ssa_left = cast(  # type: ignore
                Value,
                self._get_ssa_from_cl_reg_op(
                    op.get_exp().args[0], self.module  # type: ignore
                ),
            )
            ssa_right = cast(  # type: ignore
                Value,
                self._get_ssa_from_cl_reg_op(
                    op.get_exp().args[1], self.module  # type: ignore
                ),
            )

            # add function to module
            output_instruction = _TK_CLOPS_TO_PYQIR_REG[type(op.get_exp())](
                self.module.builder
            )(ssa_left, ssa_right)

        elif type(op.get_exp()) in _TK_CLOPS_TO_PYQIR_BIT_NO_PARAM:
            # classical ops without parameters
            output_instruction = pyqir.const(
                self.qir_bool_type,
                _TK_CLOPS_TO_PYQIR_BIT_NO_PARAM[type(op.get_exp())],
            )
            returntypebool = True
            result_index = args[-1].index[0]

        elif type(op.get_exp()) in _TK_CLOPS_TO_PYQIR_BIT:
            # classical ops acting on bits returning bit
            ssa_left = cast(  # type: ignore
                Value,
                self._get_ssa_from_cl_bit_op(op.get_exp().args[0], self.module),
            )
            ssa_right = cast(  # type: ignore
                Value,
                self._get_ssa_from_cl_bit_op(op.get_exp().args[1], self.module),
            )

            # add function to module
            returntypebool = True
            result_index = args[-1].index[0]
            output_instruction = _TK_CLOPS_TO_PYQIR_BIT[type(op.get_exp())](
                self.module.builder
            )(ssa_left, ssa_right)

        elif type(op.get_exp()) in _TK_CLOPS_TO_PYQIR_REG_BOOL:
            # classical ops acting on registers returning bit
            ssa_left = cast(  # type: ignore
                Value,
                self._get_ssa_from_cl_reg_op(
                    op.get_exp().args[0], self.module  # type: ignore
                ),
            )
            ssa_right = cast(  # type: ignore
                Value,
                self._get_ssa_from_cl_reg_op(
                    op.get_exp().args[1], self.module  # type: ignore
                ),
            )

            # add function to module
            returntypebool = True
            output_instruction = _TK_CLOPS_TO_PYQIR_REG_BOOL[type(op.get_exp())](
                self.module.builder
            )(ssa_left, ssa_right)

        else:
            raise ValueError(f"unexpected classical op {type(op.get_exp())}")

        if returntypebool:
            # the return value of the some classical ops is bool in qir,
            # so the return value can only be written to one entry
            # of the register this implementation write the value
            # to the 0-th entry
            # of the register, this could be changed to a user given value

            self.module.builder.call(
                self.set_creg_bit,
                [
                    self.get_ssa_vars(outputs),
                    pyqir.const(self.qir_int_type, result_index),
                    output_instruction,
                ],
            )
        else:
            self.module.builder.call(
                self.set_creg_to_int,
                [self.get_ssa_vars(outputs), output_instruction],
            )

    def conv_SetBitsOp(self, bits: list[Bit], op: SetBitsOp) -> None:
        assert len(op.values) == len(bits)

        for b, v in zip(bits, op.values):
            output_instruction = pyqir.const(self.qir_bool_type, int(v))

            self.module.builder.call(
                self.set_creg_bit,
                [
                    self.get_ssa_vars(b.reg_name),
                    pyqir.const(self.qir_int_type, b.index[0]),
                    output_instruction,
                ],
            )

    def conv_CopyBitsOp(self, args: list) -> None:
        assert len(args) % 2 == 0
        half_length = len(args) // 2

        for i, o in zip(args[:half_length], args[half_length:]):
            output_instruction = self.module.builder.call(
                self.get_creg_bit,
                [
                    self.get_ssa_vars(i.reg_name),
                    pyqir.const(self.qir_int_type, i.index[0]),
                ],
            )

            self.module.builder.call(
                self.set_creg_bit,
                [
                    self.get_ssa_vars(o.reg_name),
                    pyqir.const(self.qir_int_type, o.index[0]),
                    output_instruction,
                ],
            )

    def conv_BarrierOp(self, qubits: list[Qubit], op: BarrierOp) -> None:
        assert qubits[0].reg_name == "q"

        qir_qubits = self._to_qis_qubits(qubits)

        if op.data == "":
            self._add_barrier_op(self.module, len(qubits), qir_qubits)
        elif op.data[0:5] == "order":
            self._add_order_op(self.module, len(qubits), qir_qubits)
        elif op.data[0:5] == "group":
            self._add_group_op(self.module, len(qubits), qir_qubits)
        elif op.data[0:5] == "sleep":
            self._add_sleep_op(
                self.module,
                len(qubits),
                qir_qubits,
                float(op.data[6:-1]),
            )
        else:
            raise ValueError("op is not supported yet")

    def conv_other(
        self, bits: list[Bit], qubits: list[Qubit], op: Op, args: list
    ) -> None:
        optype, params = self._get_optype_and_params(op)
        pi_params = [p * math.pi for p in params]
        qubits_qis = self._to_qis_qubits(qubits)
        results = self._to_qis_results(bits)
        bits_qis: Optional[Sequence[Value]] = None
        if type(optype) == BitWiseOp:
            bits_qis = self._to_qis_bits(args)
        gate = self.module.gateset.tk_to_gateset(optype)
        if gate.func_spec != FuncSpec.BODY:
            func_name = gate.func_name.value + "_" + gate.func_spec.value
            get_gate = getattr(self.module.qis, func_name)
        else:
            get_gate = getattr(self.module.qis, gate.func_name.value)
        if bits_qis:
            get_gate(*bits_qis)
        elif params:
            get_gate(*pi_params, *qubits_qis)
        elif results:
            get_gate(*qubits_qis, results)
        else:
            get_gate(*qubits_qis)

    def command_to_module(self, op: Op, args: list) -> tketqirModule:
        """Populate a PyQir module from a pytket command."""
        qubits = [q for q in args if q.type == UnitType.qubit]
        bits = [b for b in args if b.type == UnitType.bit]

        if isinstance(op, RangePredicateOp):
            self.conv_RangePredicateOp(op, args)

        elif isinstance(op, Conditional):
            raise ValueError("conditional ops can't contain conditional ops")

        elif isinstance(op, WASMOp):
            self.conv_WASMOp(op, args)

        elif op.type == OpType.ZZPhase:
            self.conv_ZZPhase(qubits, op)

        elif op.type == OpType.PhasedX:
            self.conv_phasedx(qubits, op)

        elif op.type == OpType.TK2:
            self.conv_tk2(qubits, op)

        elif op.type == OpType.ZZMax:
            self.conv_zzmax(qubits)

        elif op.type == OpType.Measure:
            self.conv_measure(bits, qubits)

        elif op.type == OpType.Phase:
            # ignore phase op
            pass

        elif isinstance(op, ClassicalExpBox):
            self.conv_classicalexpbox(op, args)

        elif isinstance(op, SetBitsOp):
            self.conv_SetBitsOp(bits, op)

        elif isinstance(op, CopyBitsOp):
            self.conv_CopyBitsOp(args)

        elif isinstance(op, BarrierOp):
            self.conv_BarrierOp(qubits, op)

        else:
            self.conv_other(bits, qubits, op, args)

        return self.module

    def circuit_to_module(
        self, circuit: Circuit, record_output: bool = False
    ) -> tketqirModule:
        """Populate a PyQir module from a pytket circuit."""

        for command in circuit:
            op = command.op

            if isinstance(op, Conditional):
                self.conv_conditional(command, op)

            else:
                self.command_to_module(op, command.args)

        if record_output:
            self.module.builder.call(
                self.record_output_start,
                [],
            )

            for creg in self.circuit.c_registers:
                reg_name = creg[0].reg_name
                self.module.builder.call(
                    self.record_output_i64,
                    [
                        self._get_i64_ssa_reg(reg_name),
                        self.reg_const[reg_name],
                    ],
                )

            self.module.builder.call(
                self.record_output_end,
                [],
            )

        return self.module

    def subcircuit_to_module(
        self,
        circuit: Circuit,
    ) -> tketqirModule:
        """Populate a PyQir module from a pytket subcircuit."""

        for command in circuit:
            self.command_to_module(command.op, command.args)

        return self.module
