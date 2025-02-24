# Copyright Quantinuum
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

import abc
import math
from collections.abc import Sequence
from functools import partial
from typing import Optional, Union

import pyqir
from pyqir import IntPredicate, Value

from pytket import predicates
from pytket.circuit import (
    BarrierOp,
    Bit,
    BitRegister,
    CircBox,
    Circuit,
    ClBitVar,
    ClExpr,
    ClExprOp,
    ClOp,
    ClRegVar,
    Command,
    Conditional,
    CopyBitsOp,
    Op,
    OpType,
    Qubit,
    RangePredicateOp,
    SetBitsOp,
    UnitID,
    WASMOp,
    WiredClExpr,
)
from pytket.circuit.logic_exp import (
    BitAnd,
    BitEq,
    BitNeq,
    BitNot,
    BitOne,
    BitOr,
    BitWiseOp,
    BitXor,
    BitZero,
    LogicExp,
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

_TK_CLOPS_TO_PYQIR_2_BITS: dict = {
    BitAnd: lambda b: b.and_,
    BitOr: lambda b: b.or_,
    BitXor: lambda b: b.xor,
    BitNeq: lambda b: partial(b.icmp, IntPredicate.NE),
    BitEq: lambda b: partial(b.icmp, IntPredicate.EQ),
}

_TK_CLOPS_TO_PYQIR_BIT: dict = {
    BitNot: lambda b: b.sub,
}

_TK_CLOPS_TO_PYQIR_2_BITS_NO_PARAM: dict = {
    BitOne: 1,
    BitZero: 0,
}

_TK_CLEXPR_OP_TO_PYQIR: dict = {
    ClOp.BitAnd: lambda b: b.and_,
    ClOp.BitOr: lambda b: b.or_,
    ClOp.BitXor: lambda b: b.xor,
    ClOp.BitEq: lambda b: partial(b.icmp, IntPredicate.EQ),
    ClOp.BitNeq: lambda b: partial(b.icmp, IntPredicate.NE),
    # ClOp.BitNot
    # ClOp.BitZero
    # ClOp.BitOne
    ClOp.RegAnd: lambda b: b.and_,
    ClOp.RegOr: lambda b: b.or_,
    ClOp.RegXor: lambda b: b.xor,
    ClOp.RegEq: lambda b: partial(b.icmp, IntPredicate.EQ),
    ClOp.RegNeq: lambda b: partial(b.icmp, IntPredicate.NE),
    # ClOp.RegNot
    # ClOp.RegZero
    # ClOp.RegOne
    ClOp.RegLt: lambda b: partial(b.icmp, IntPredicate.ULT),
    ClOp.RegGt: lambda b: partial(b.icmp, IntPredicate.UGT),
    ClOp.RegLeq: lambda b: partial(b.icmp, IntPredicate.ULE),
    ClOp.RegGeq: lambda b: partial(b.icmp, IntPredicate.UGE),
    ClOp.RegAdd: lambda b: b.add,
    ClOp.RegSub: lambda b: b.sub,
    ClOp.RegMul: lambda b: b.mul,
    # ClOp.RegDiv
    # ClOp.RegPow
    ClOp.RegLsh: lambda b: b.shl,
    ClOp.RegRsh: lambda b: b.lshr,
    # ClOp.RegNeg
}

_TK_CLEXPR_OP_WITH_REG_ARGS = set(
    [
        ClOp.RegAnd,
        ClOp.RegOr,
        ClOp.RegXor,
        ClOp.RegEq,
        ClOp.RegNeq,
        ClOp.RegNot,
        ClOp.RegLt,
        ClOp.RegGt,
        ClOp.RegLeq,
        ClOp.RegGeq,
        ClOp.RegAdd,
        ClOp.RegSub,
        ClOp.RegMul,
        ClOp.RegDiv,
        ClOp.RegPow,
        ClOp.RegLsh,
        ClOp.RegRsh,
        ClOp.RegNeg,
    ]
)


class AbstractQirGenerator:
    """Abstract Class for the QIR generation from a pytket circuit.
    Implementing the functionality that is not specific to any profile"""

    def __init__(
        self,
        circuit: Circuit,
        module: tketqirModule,
        wasm_int_type: int,
        qir_int_type: int,
    ) -> None:
        self.circuit = circuit
        self.module = module
        self.wasm_int_type = pyqir.IntType(self.module.context, wasm_int_type)
        self.int_size = qir_int_type
        self.qir_int_type = pyqir.IntType(self.module.context, qir_int_type)
        self.qir_i1p_type = pyqir.PointerType(pyqir.IntType(self.module.context, 1))
        self.qir_bool_type = pyqir.IntType(self.module.context, 1)
        self.qubit_type = pyqir.qubit_type(self.module.context)
        self.result_type = pyqir.result_type(self.module.context)

        self.cregs = _retrieve_registers(self.circuit.bits, BitRegister)  # type: ignore
        self.creg_size: dict[str, int] = {}
        self.target_gateset = self.module.gateset.base_gateset

        self.block_count = 0
        self.block_count_sb = 0

        self.has_wasm = False
        self.wasm_sar_dict: dict[str, str] = {}
        self.azure_sar_dict: dict[str, str] = {}
        self.wasm_sar_dict["!llvm.module.flags"] = (
            'attributes #1 = { "wasm" }\n\n!llvm.module.flags'
        )
        self.wasm_sar_dict[
            'attributes #1 = { "irreversible" }\n\nattributes #1 = { "wasm" }'
        ] = 'attributes #1 = { "wasm" }\nattributes #2 = { "irreversible" }'
        self.wasm_sar_dict[
            "declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1"
        ] = "declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #2"

        self.int_type_str = f"i{qir_int_type}"

        self.target_gateset.add(OpType.PhasedX)
        self.target_gateset.add(OpType.ZZPhase)
        self.target_gateset.add(OpType.ZZMax)
        self.target_gateset.add(OpType.TK2)

        self.reg_const: dict[str, Value] = {}

        self.getset_predicate = predicates.GateSetPredicate(
            set(self.target_gateset)
        )  # noqa: E501

        # __quantum__qis__read_result__body(result)
        self.read_bit_from_result = self.module.module.add_external_function(
            "__quantum__qis__read_result__body",
            pyqir.FunctionType(
                pyqir.IntType(self.module.module.context, 1),
                [pyqir.result_type(self.module.module.context)],
            ),
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

        self.wasm: dict[str, pyqir.Function] = {}

        self.additional_quantum_gates: dict[OpType, pyqir.Function] = {}

    @abc.abstractmethod
    def _get_bit_from_creg(self, creg: str, index: int) -> Value:
        pass

    @abc.abstractmethod
    def _set_bit_in_creg(self, creg: str, index: int, ssa_bit: Value) -> None:
        pass

    def _set_bit(self, bit: Bit, ssa_bit: Value) -> None:
        self._set_bit_in_creg(bit.reg_name, bit.index[0], ssa_bit)

    @abc.abstractmethod
    def get_ssa_vars(self, reg_name: str) -> Value:
        pass

    @abc.abstractmethod
    def _get_i64_ssa_reg(self, name: str) -> Value:
        pass

    @abc.abstractmethod
    def set_ssa_vars(self, reg_name: str, ssa_i64: Value, trunc: bool) -> None:
        pass

    def _add_barrier_op(self, index: int, qir_qubits: Sequence) -> None:
        # __quantum__qis__barrier1__body()
        if self.barrier[index] is None:
            self.barrier[index] = self.module.module.add_external_function(
                f"__quantum__qis__barrier{index}__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [pyqir.qubit_type(self.module.module.context)] * index,
                ),
            )

        self.module.builder.call(
            self.barrier[index],  # type: ignore
            [*qir_qubits],
        )

    def _add_group_op(self, index: int, qir_qubits: Sequence) -> None:
        # __quantum__qis__group1__body()
        if self.group[index] is None:
            self.group[index] = self.module.module.add_external_function(
                f"__quantum__qis__group{index}__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [pyqir.qubit_type(self.module.module.context)] * index,
                ),
            )

        self.module.builder.call(
            self.group[index],  # type: ignore
            [*qir_qubits],
        )

    def _add_order_op(self, index: int, qir_qubits: Sequence) -> None:
        # __quantum__qis__order1__body()
        if self.order[index] is None:
            self.order[index] = self.module.module.add_external_function(
                f"__quantum__qis__order{index}__body",
                pyqir.FunctionType(
                    pyqir.Type.void(self.module.module.context),
                    [pyqir.qubit_type(self.module.module.context)] * index,
                ),
            )

        self.module.builder.call(
            self.order[index],  # type: ignore
            [*qir_qubits],
        )

    def _add_sleep_op(self, index: int, qir_qubits: Sequence, duration: float) -> None:
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

        self.module.builder.call(
            self.sleep[index],  # type: ignore
            [
                *qir_qubits,
                pyqir.const(pyqir.Type.double(self.module.module.context), duration),
            ],
        )

    def _decompose_conditional_circ_box(
        self, op: CircBox, args: list[UnitID]
    ) -> Circuit:
        """Rebase an op to the target gateset if needed."""
        circuit = Circuit(self.circuit.n_qubits)
        arg_names = set([b.reg_name for b in args if type(b) is Bit])
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

    def _to_qis_qubits(self, qubits: list[Qubit]) -> list[Value]:
        return [self.module.module.qubits[qubit.index[0]] for qubit in qubits]

    def _to_qis_results(self, bits: list[Bit]) -> Optional[Value]:
        if bits:
            return self.module.module.results[bits[0].index[0]]
        return None

    def _to_qis_bits(self, args: list[Bit]) -> Sequence[Value]:
        for b in args:
            assert b.reg_name == "c"
        if args:
            return [self.module.module.results[bit.index[0]] for bit in args[:-1]]
        return []

    def _get_c_regs_from_com(
        self, op: Op, args: list[Union[Bit, Qubit]]
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
        self, reg: Union[BitRegister, RegAnd, RegOr, RegXor, int]
    ) -> Value:
        if type(reg) in _TK_CLOPS_TO_PYQIR_REG:
            assert len(reg.args) == 2  # type: ignore

            ssa_left = self._get_ssa_from_cl_reg_op(reg.args[0])  # type: ignore
            ssa_right = self._get_ssa_from_cl_reg_op(reg.args[1])  # type: ignore

            # add function to module
            output_instruction = _TK_CLOPS_TO_PYQIR_REG[type(reg)](self.module.builder)(
                ssa_left, ssa_right
            )
            return output_instruction  # type: ignore
        elif type(reg) is BitRegister:
            return self._get_i64_ssa_reg(reg.name)
        elif type(reg) is int:
            return pyqir.const(self.qir_int_type, reg)
        else:
            raise ValueError(f"unsupported classical register operation: {type(reg)}")

    def _get_ssa_from_cl_bit_op(
        self, bit: Union[LogicExp, Bit, BitAnd, BitOr, BitXor, int]
    ) -> Value:
        if type(bit) is Bit:
            result = self._get_bit_from_creg(bit.reg_name, bit.index[0])

            return result
        elif type(bit) is int:
            return pyqir.const(self.qir_bool_type, bit)
        elif type(bit) in _TK_CLOPS_TO_PYQIR_BIT:
            assert len(bit.args) == 1  # type: ignore

            ssa_left = pyqir.const(self.qir_bool_type, 1)
            ssa_right = self._get_ssa_from_cl_bit_op(bit.args[0])  # type: ignore

            # add function to module
            output_instruction = _TK_CLOPS_TO_PYQIR_BIT[type(bit)](self.module.builder)(
                ssa_left, ssa_right
            )

            return output_instruction  # type: ignore
        elif type(bit) in _TK_CLOPS_TO_PYQIR_2_BITS:
            assert len(bit.args) == 2  # type: ignore

            ssa_left = self._get_ssa_from_cl_bit_op(bit.args[0])  # type: ignore
            ssa_right = self._get_ssa_from_cl_bit_op(bit.args[1])  # type: ignore

            # add function to module
            output_instruction = _TK_CLOPS_TO_PYQIR_2_BITS[type(bit)](
                self.module.builder
            )(ssa_left, ssa_right)

            return output_instruction  # type: ignore
        else:
            raise ValueError(f"unsupported bitwise operation {type(bit)}")

    def get_wasm_sar(self) -> dict[str, str]:
        return self.wasm_sar_dict

    def get_azure_sar(self) -> dict[str, str]:
        return self.azure_sar_dict

    def conv_RangePredicateOp(self, op: RangePredicateOp, args: list[Bit]) -> None:
        # special case handling for REG_EQ

        if op.lower == op.upper:
            registername = args[0].reg_name

            result = self.module.module.builder.icmp(
                pyqir.IntPredicate.EQ,
                pyqir.const(self.qir_int_type, op.lower),
                self._get_i64_ssa_reg(registername),
            )

            self._set_bit(args[-1], result)

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

            self._set_bit(args[-1], result)

    @abc.abstractmethod
    def conv_conditional(self, command: Command, op: Conditional) -> None:
        pass

    def conv_WASMOp(self, op: WASMOp, args: list[Union[Bit, Qubit]]) -> None:
        self.has_wasm = True

        paramreg, resultreg = self._get_c_regs_from_com(op, args)

        ssa_param = [self._get_i64_ssa_reg(p) for p in paramreg]

        if op.func_name not in self.wasm:
            wasm_func_interface = "declare "
            parametertype = [self.qir_int_type] * len(paramreg)
            if len(resultreg) == 0:
                returntype = pyqir.Type.void(self.module.module.context)
                wasm_func_interface += "void "
            elif len(resultreg) == 1:
                returntype = self.qir_int_type
                wasm_func_interface += f"{self.int_type_str} "
            else:
                raise ValueError(
                    "wasm function which return more than"
                    + " one value are not supported yet"
                    + f"please don't use {op.func_name}"
                )

            self.wasm[op.func_name] = self.module.module.add_external_function(
                f"{op.func_name}",
                pyqir.FunctionType(
                    returntype,
                    parametertype,
                ),
            )

            wasm_func_interface += f"@{op.func_name}("
            if len(paramreg) > 0:
                param_str = f"{self.int_type_str}, " * (len(paramreg) - 1)
                wasm_func_interface += param_str
                wasm_func_interface += f"{self.int_type_str})"
            else:
                wasm_func_interface += ")"

            self.wasm_sar_dict[wasm_func_interface] = f"{wasm_func_interface} #1"

        result = self.module.builder.call(
            self.wasm[op.func_name],
            [*ssa_param],
        )

        if len(resultreg) == 1:
            self.set_ssa_vars(resultreg[0], result, True)

    def conv_ZZPhase(self, qubits: list[Qubit], op: Op) -> None:
        if OpType.ZZPhase not in self.additional_quantum_gates:
            self.additional_quantum_gates[OpType.ZZPhase] = (
                self.module.module.add_external_function(
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
            self.additional_quantum_gates[OpType.PhasedX] = (
                self.module.module.add_external_function(
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
            self.additional_quantum_gates[OpType.TK2] = (
                self.module.module.add_external_function(
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
            self.additional_quantum_gates[OpType.ZZMax] = (
                self.module.module.add_external_function(
                    "__quantum__qis__zzmax__body",
                    pyqir.FunctionType(
                        pyqir.Type.void(self.module.module.context),
                        [
                            pyqir.qubit_type(self.module.module.context),
                            pyqir.qubit_type(self.module.module.context),
                        ],
                    ),
                )
            )

        self.module.builder.call(
            self.additional_quantum_gates[OpType.ZZMax],
            [
                self.module.module.qubits[qubits[0].index[0]],
                self.module.module.qubits[qubits[1].index[0]],
            ],
        )

    @abc.abstractmethod
    def conv_measure(self, bits: list[Bit], qubits: list[Qubit]) -> None:
        pass

    def _get_ssa_from_clexpr_arg(
        self,
        arg: int | ClBitVar | ClRegVar | ClExpr,
        bit_posn: dict[int, int],
        reg_posn: dict[int, list[int]],
        cmd_args: list[Bit],
        expect_register: bool,
    ) -> tuple[bool, Value]:
        if isinstance(arg, int):
            if expect_register:
                return False, pyqir.const(self.qir_int_type, arg)
            elif arg not in (0, 1):
                raise ValueError(f"Invalid bit value {arg}")
            else:
                return True, pyqir.const(self.qir_bool_type, arg)
        elif isinstance(arg, ClBitVar):
            cmd_arg: Bit = cmd_args[bit_posn[arg.index]]
            return True, self._get_bit_from_creg(cmd_arg.reg_name, cmd_arg.index[0])
        elif isinstance(arg, ClRegVar):
            return False, self._get_i64_ssa_reg(
                cmd_args[reg_posn[arg.index][0]].reg_name
            )
        else:
            assert isinstance(arg, ClExpr)
            expr_op: ClOp = arg.op
            ssa_args = [
                self._get_ssa_from_clexpr_arg(
                    expr_arg,
                    bit_posn,
                    reg_posn,
                    cmd_args,
                    expr_op in _TK_CLEXPR_OP_WITH_REG_ARGS,
                )[1]
                for expr_arg in arg.args
            ]
            match expr_op:
                case ClOp.BitAnd | ClOp.BitOr | ClOp.BitXor | ClOp.BitEq | ClOp.BitNeq:
                    return True, _TK_CLEXPR_OP_TO_PYQIR[expr_op](self.module.builder)(
                        *ssa_args
                    )
                case ClOp.BitNot:
                    # Implemented as x --> 1 - x
                    assert len(ssa_args) == 1
                    return True, self.module.builder.sub(
                        pyqir.const(self.qir_bool_type, 1), ssa_args[0]
                    )
                case ClOp.BitZero:
                    assert len(ssa_args) == 0
                    return True, pyqir.const(self.qir_bool_type, 0)
                case ClOp.BitOne:
                    assert len(ssa_args) == 0
                    return True, pyqir.const(self.qir_bool_type, 1)
                case (
                    ClOp.RegAnd
                    | ClOp.RegOr
                    | ClOp.RegXor
                    | ClOp.RegAdd
                    | ClOp.RegSub
                    | ClOp.RegMul
                    | ClOp.RegLsh
                    | ClOp.RegRsh
                ):
                    assert len(ssa_args) == 2
                    return False, _TK_CLEXPR_OP_TO_PYQIR[expr_op](self.module.builder)(
                        *ssa_args
                    )
                case (
                    ClOp.RegEq
                    | ClOp.RegNeq
                    | ClOp.RegLt
                    | ClOp.RegGt
                    | ClOp.RegLeq
                    | ClOp.RegGeq
                ):
                    assert len(ssa_args) == 2
                    return True, _TK_CLEXPR_OP_TO_PYQIR[expr_op](self.module.builder)(
                        *ssa_args
                    )
                case ClOp.RegNot:
                    # Implemented as x --> 2^self.int_size - 1 - x
                    assert len(ssa_args) == 1
                    return False, self.module.builder.sub(
                        pyqir.const(self.qir_int_type, (1 << self.int_size) - 1),
                        ssa_args[0],
                    )
                case ClOp.RegZero:
                    assert len(ssa_args) == 0
                    return False, pyqir.const(self.qir_int_type, 0)
                case ClOp.RegOne:
                    # Sets all bits in the register to 1
                    assert len(ssa_args) == 0
                    return False, pyqir.const(
                        self.qir_int_type, (1 << self.int_size) - 1
                    )
                case ClOp.RegNeg:
                    # Implemented as x --> 0 - x
                    assert len(ssa_args) == 1
                    return False, self.module.builder.sub(
                        pyqir.const(self.qir_int_type, 0), ssa_args[0]
                    )
                case ClOp.RegDiv | ClOp.RegPow:
                    # https://github.com/CQCL/pytket-qir/issues/181
                    raise ValueError(f"Classical operation {expr_op} not supported")
                case _:
                    raise ValueError("Invalid classical operation")

    def conv_clexprop(self, op: ClExprOp, args: list[Bit]) -> None:
        wexpr: WiredClExpr = op.expr
        expr: ClExpr = wexpr.expr
        bit_posn: dict[int, int] = wexpr.bit_posn
        reg_posn: dict[int, list[int]] = wexpr.reg_posn
        output_posn: list[int] = wexpr.output_posn

        # We require that all register variables correspond to actual complete
        # registers.
        input_regs: dict[int, BitRegister] = {}
        all_cregs = set(self.cregs.values())
        for i, posns in reg_posn.items():
            reg_args = [args[j] for j in posns]
            for creg in all_cregs:
                if creg.to_list() == reg_args:
                    input_regs[i] = creg
                    break
            else:
                raise ValueError(
                    f"ClExprOp ({wexpr}) contains a register variable (r{i}) "
                    "that is not wired to any BitRegister in the circuit."
                )

        returntypebool, output_instruction = self._get_ssa_from_clexpr_arg(
            expr, bit_posn, reg_posn, args, expr.op in _TK_CLEXPR_OP_WITH_REG_ARGS
        )

        if returntypebool:
            assert len(output_posn) == 1
            output_arg: Bit = args[output_posn[0]]
            self._set_bit_in_creg(
                output_arg.reg_name, output_arg.index[0], output_instruction
            )
        else:
            assert len(output_posn) > 0
            output_args: list[Bit] = [args[i] for i in output_posn]
            output_reg_name: Optional[str] = None
            for creg in all_cregs:
                if creg.to_list() == output_args:
                    output_reg_name = creg.name
                    break
            else:
                raise ValueError(
                    f"ClExprOp ({wexpr}) has outputs that do not "
                    "correspond to any BitRegister in the circuit."
                )
            self.set_ssa_vars(output_reg_name, output_instruction, True)

    def conv_SetBitsOp(self, bits: list[Bit], op: SetBitsOp) -> None:
        assert len(op.values) == len(bits)

        for b, v in zip(bits, op.values):
            output_instruction = pyqir.const(self.qir_bool_type, int(v))

            self._set_bit(b, output_instruction)

    def conv_CopyBitsOp(self, args: list) -> None:
        assert len(args) % 2 == 0
        half_length = len(args) // 2

        for i, o in zip(args[:half_length], args[half_length:]):
            output_instruction = self._get_bit_from_creg(i.reg_name, i.index[0])

            self._set_bit(o, output_instruction)

    def conv_BarrierOp(self, qubits: list[Qubit], op: BarrierOp) -> None:
        assert qubits[0].reg_name == "q"

        qir_qubits = self._to_qis_qubits(qubits)

        if op.data == "":
            self._add_barrier_op(len(qubits), qir_qubits)
        elif op.data[0:5] == "order":
            self._add_order_op(len(qubits), qir_qubits)
        elif op.data[0:5] == "group":
            self._add_group_op(len(qubits), qir_qubits)
        elif op.data[0:5] == "sleep":
            self._add_sleep_op(len(qubits), qir_qubits, float(op.data[6:-1]))
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
        if type(optype) is BitWiseOp:
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

        elif isinstance(op, ClExprOp):
            self.conv_clexprop(op, args)

        elif isinstance(op, SetBitsOp):
            self.conv_SetBitsOp(bits, op)

        elif isinstance(op, CopyBitsOp):
            self.conv_CopyBitsOp(args)

        elif isinstance(op, BarrierOp):
            self.conv_BarrierOp(qubits, op)

        else:
            self.conv_other(bits, qubits, op, args)

        return self.module

    @abc.abstractmethod
    def record_output(self) -> None:
        """function to record the output"""

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

            self.record_output()

        return self.module

    def subcircuit_to_module(
        self,
        circuit: Circuit,
    ) -> tketqirModule:
        """Populate a PyQir module from a pytket subcircuit."""

        for command in circuit:
            self.command_to_module(command.op, command.args)

        return self.module
