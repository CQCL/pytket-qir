# Copyright 2019-2023 Cambridge Quantum Computing
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

from functools import partial
from typing import cast, Dict, List, Optional, Sequence, Tuple, Union

from pyqir import Value, IntPredicate
import pyqir

from pytket import Circuit, OpType, Bit, Qubit  # type: ignore
from pytket.qasm.qasm import _retrieve_registers  # type: ignore
from pytket.circuit import (  # type: ignore
    BitRegister,
    ClassicalExpBox,
    Command,
    Conditional,
    RangePredicateOp,
    CopyBitsOp,
    Op,
    MetaOp,
    SetBitsOp,
    WASMOp,
    OpType,
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
    BitOr,
    BitXor,
    BitNeq,
    BitEq,
    BitAnd,
)

from pytket.passes import auto_rebase_pass  # type: ignore

from .gatesets import (
    FuncSpec,
)

from .module import tketqirModule


_TK_CLOPS_TO_PYQIR_REG: Dict = {
    RegAnd: lambda b: b.and_,
    RegOr: lambda b: b.or_,
    RegXor: lambda b: b.xor,
    RegAdd: lambda b: b.add,
    RegSub: lambda b: b.sub,
    RegMul: lambda b: b.mul,
    RegLsh: lambda b: b.shl,
    RegRsh: lambda b: b.lshr,
}

_TK_CLOPS_TO_PYQIR_REG_BOOL: Dict = {
    RegEq: lambda b: partial(b.icmp, IntPredicate.EQ),
    RegNeq: lambda b: partial(b.icmp, IntPredicate.NE),
    RegGt: lambda b: partial(b.icmp, IntPredicate.UGT),
    RegGeq: lambda b: partial(b.icmp, IntPredicate.UGE),
    RegLt: lambda b: partial(b.icmp, IntPredicate.ULT),
    RegLeq: lambda b: partial(b.icmp, IntPredicate.ULE),
}

_TK_CLOPS_TO_PYQIR_BIT: Dict = {
    BitAnd: lambda b: b.and_,
    BitOr: lambda b: b.or_,
    BitXor: lambda b: b.xor,
    BitNeq: lambda b: partial(b.icmp, IntPredicate.NE),
    BitEq: lambda b: partial(b.icmp, IntPredicate.EQ),
}


class QirGenerator:
    """Generate QIR from a pytket circuit."""

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
        self.qir_int_type = pyqir.IntType(self.module.context, qir_int_type)
        self.qubit_type = pyqir.qubit_type(self.module.context)
        self.result_type = pyqir.result_type(self.module.context)

        self.cregs = _retrieve_registers(self.circuit.bits, BitRegister)
        self.target_gateset = self.module.gateset.base_gateset

        # Will throw an exception if the rebase can not handle the target gateset.
        self.rebase_to_gateset = auto_rebase_pass(self.target_gateset)

        self.set_cregs: Dict[str, List] = {}  # Keep track of set registers.
        self.ssa_vars: Dict[str, Value] = {}  # Keep track of set ssa variables.

        # i1 read_bit_from_reg(i64 reg, i64 index)
        self.read_bit_from_reg = self.module.module.add_external_function(
            "read_bit_from_reg",
            pyqir.FunctionType(
                pyqir.IntType(self.module.module.context, 1),
                [self.qir_int_type] * 2,
            ),
        )

        # void set_one_bit_in_reg(i64 reg, i64 index, i1 value)
        self.set_one_bit_in_reg = self.module.module.add_external_function(
            "set_one_bit_in_reg",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [
                    self.qir_int_type,
                    self.qir_int_type,
                    pyqir.IntType(self.module.module.context, 1),
                ],
            ),
        )

        # void set_all_bits_in_reg(i64 reg, i64 value)
        self.set_all_bits_in_reg = self.module.module.add_external_function(
            "set_all_bits_in_reg",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [
                    self.qir_int_type,
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

        # i64 reg2var(i1, i1, i1, ...)
        self.reg2var = self.module.module.add_external_function(
            "reg2var",
            pyqir.FunctionType(
                pyqir.IntType(self.module.module.context, qir_int_type),
                [pyqir.IntType(self.module.module.context, 1)] * qir_int_type,
            ),
        )

        # void __quantum__rt__int_record_output(i64)
        self.record_output = self.module.module.add_external_function(
            "__quantum__rt__int_record_output",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [pyqir.IntType(self.module.module.context, qir_int_type)],
            ),
        )

        self.barrier: List[Optional[pyqir.Function]] = [None] * (
            self.circuit.n_qubits + 1
        )
        self.order: List[Optional[pyqir.Function]] = [None] * (
            self.circuit.n_qubits + 1
        )
        self.group: List[Optional[pyqir.Function]] = [None] * (
            self.circuit.n_qubits + 1
        )
        self.sleep: List[Optional[pyqir.Function]] = [None] * (
            self.circuit.n_qubits + 1
        )

        for creg in self.circuit.c_registers:
            self._reg2ssa_var(creg, qir_int_type)

    def _add_barrier_op(
        self, module: tketqirModule, index: int, qir_qubits: Sequence
    ) -> None:
        # __quantum__qis__barrier1__body()
        if self.barrier[index] == None:
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
        if self.group[index] == None:
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
        if self.order[index] == None:
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

        if self.sleep[index] == None:
            paramlist = [pyqir.qubit_type(self.module.module.context)] * index
            paramlist.append(
                pyqir.Type.double(self.module.module.context)
            )  # add float parameter
            self.sleep[index] = self.module.module.add_external_function(
                f"__quantum__qis__sleep__body",
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
            self.rebase_to_gateset.apply(circuit)
            return circuit
        return None

    def _rebase_op_to_gateset(self, op: OpType, args: List) -> Optional[Circuit]:
        """Rebase an op to the target gateset if needed."""
        optype = op.type
        if op.type == OpType.ClassicalExpBox:
            circuit = Circuit(self.circuit.n_qubits)
            for cr in self.circuit.c_registers:
                circuit.add_c_register(cr.name, cr.size)

            circuit.add_gate(op, args)
            return circuit
        else:
            params = op.params
            circuit = Circuit(self.circuit.n_qubits, self.circuit.n_bits)
            circuit.add_gate(optype, params, args)
            self.rebase_to_gateset.apply(circuit)
            return circuit

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
            return self.module.module.results[bits[0].index[0]]  # type: ignore
        return None

    def _to_qis_bits(self, args: List[Bit]) -> Sequence[Value]:
        for b in args:
            assert b.name == "c"
        if args:
            return [self.module.module.results[bit.index[0]] for bit in args[:-1]]
        return []

    def _reg2ssa_var(self, bit_reg: BitRegister, int_size: int) -> Value:
        """Convert a BitRegister to an SSA variable using pyqir types."""
        reg_name = bit_reg[0].reg_name
        if (
            reg_name not in self.ssa_vars.keys()
        ):  # Check if the register has been previously set.
            # Check if the register has been previously set. If not, initialise to 0.
            if reg_value := self.set_cregs.get(reg_name):
                bit_reg = reg_value
                value = sum([n * 2**k for k, n in enumerate(reg_value)])
                return pyqir.const(self.qir_int_type, value)
            else:
                bit_reg = [False] * len(bit_reg)
            if (size := len(bit_reg)) <= int_size:  # Widening by zero-padding.
                bool_reg = bit_reg + [False] * (int_size - size)
            else:  # Narrowing by truncation.
                bool_reg = bit_reg[:int_size]
            ssa_var = cast(Value, self.module.builder.call(self.reg2var, [*bool_reg]))  # type: ignore
            self.ssa_vars[reg_name] = ssa_var
            return ssa_var
        else:
            return cast(Value, self.ssa_vars[reg_name])  # type: ignore

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
                        raise ValueError("WASM ops must act on entire registers.")
                    reglist.append(regname)
        elif isinstance(op, SetBitsOp):
            for reglist, sizes in [
                (outputs, [op.n_outputs]),
            ]:
                for in_width in sizes:
                    if in_width == 0:
                        raise ValueError(
                            "A value is getting assigned to an empty register."
                        )
                    com_bits = args[:in_width]
                    args = args[in_width:]
                    regname = com_bits[0].reg_name
                    if com_bits != list(self.cregs[regname]):
                        raise ValueError("SetBitOp must act on entire registers.")
                    reglist.append(regname)
        return inputs, outputs

    def _get_ssa_from_cl_reg_op(
        self, reg: Union[BitRegister, RegAnd, RegOr, RegXor], module: tketqirModule
    ) -> Value:

        if type(reg) in _TK_CLOPS_TO_PYQIR_REG:
            assert len(reg.args) == 2

            ssa_left = self._get_ssa_from_cl_reg_op(reg.args[0], module)
            ssa_right = self._get_ssa_from_cl_reg_op(reg.args[1], module)

            # add function to module
            output_instruction = _TK_CLOPS_TO_PYQIR_REG[type(reg)](module.builder)(
                ssa_left, ssa_right
            )
            return output_instruction  # type: ignore
        elif type(reg) == BitRegister:
            return self.ssa_vars[reg.name]
        else:
            raise ValueError("unsupported classical register operaton")

    def _get_ssa_from_cl_bit_op(
        self, bit: Union[Bit, BitAnd, BitOr, BitXor], module: tketqirModule
    ) -> Value:

        if type(bit) == Bit:

            result = module.builder.call(
                self.read_bit_from_reg,
                [
                    self.ssa_vars[bit.reg_name],
                    pyqir.const(self.qir_int_type, bit.index[0]),
                ],
            )

            return result
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
            raise ValueError("unsupported bisewise operation")

    def circuit_to_module(
        self, circuit: Circuit, module: tketqirModule, record_output: bool = False
    ) -> tketqirModule:
        """Populate a PyQir module from a pytket circuit."""

        for command in circuit:
            op = command.op

            if isinstance(op, RangePredicateOp):
                lower_qir = pyqir.const(self.qir_int_type, op.lower)
                upper_qir = pyqir.const(self.qir_int_type, op.upper)

                registername = command.args[0].reg_name

                lower_cond = module.module.builder.icmp(
                    pyqir.IntPredicate.SGT, lower_qir, self.ssa_vars[registername]
                )
                upper_cond = module.module.builder.icmp(
                    pyqir.IntPredicate.SGT, self.ssa_vars[registername], upper_qir
                )

                result = module.module.builder.and_(lower_cond, upper_cond)

                condition_bit_index = command.args[-1].index[0]
                registername = command.args[-1].reg_name

                self.module.builder.call(
                    self.set_one_bit_in_reg,
                    [
                        self.ssa_vars[registername],
                        pyqir.const(self.qir_int_type, condition_bit_index),
                        result,
                    ],
                )

            elif isinstance(op, Conditional):
                assert op.width == 1  # only one conditional bit
                conditional_circuit = self._rebase_op_to_gateset(
                    op.op, command.args[op.width :]
                )
                condition_bit_index = command.args[0].index[0]
                condition_name = command.args[0].reg_name

                def condition_block_true() -> None:
                    """
                    Populate recursively the module with the contents of the conditional
                    sub-circuit when the condition is True.
                    """
                    if op.value == 1:
                        self.circuit_to_module(conditional_circuit, module)

                def condition_block_false() -> None:
                    """
                    Populate recursively the module with the contents of the conditional
                    sub-circuit when the condition is False.
                    """
                    if op.value == 0:
                        self.circuit_to_module(conditional_circuit, module)

                if condition_name in self.ssa_vars:

                    ssabool = module.builder.call(
                        self.read_bit_from_reg,
                        [
                            self.ssa_vars[condition_name],
                            pyqir.const(self.qir_int_type, condition_bit_index),
                        ],
                    )

                    module.module.builder.if_(
                        ssabool,
                        true=lambda: condition_block_true(),  # type: ignore
                        false=lambda: condition_block_false(),  # type: ignore
                    )

                else:
                    ValueError(
                        "circuit contruction with special condition not yet supported"
                    )
                    # this should be an assertion when working

            elif isinstance(op, WASMOp):
                raise ValueError(
                    "WASM not supported yet, support expected with pytket-qir==0.3.0"
                )
            elif op.type == OpType.Measure:

                assert len(command.bits) == 1
                assert len(command.qubits) == 1
                assert command.qubits[0].reg_name == "q"

                module.qis.mz(
                    module.module.qubits[command.qubits[0].index[0]],
                    module.module.results[command.qubits[0].index[0]],
                )

                ssa_measureresult = self.module.builder.call(
                    self.read_bit_from_result,
                    [
                        module.module.results[command.qubits[0].index[0]],
                    ],
                )

                self.module.builder.call(
                    self.set_one_bit_in_reg,
                    [
                        self.ssa_vars[command.bits[0].reg_name],
                        pyqir.const(self.qir_int_type, command.bits[0].index[0]),
                        ssa_measureresult,
                    ],
                )

            elif isinstance(op, ClassicalExpBox):

                returntypebool = False
                result_index = (
                    0  # defines the default value for ops that returns bool, see below
                )
                outputs = command.args[-1].reg_name
                ssa_left = self.ssa_vars[list(self.ssa_vars)[0]]  # set default value
                ssa_right = self.ssa_vars[list(self.ssa_vars)[0]]  # set default value

                #

                if type(op.get_exp()) in _TK_CLOPS_TO_PYQIR_REG:
                    # classical ops acting on registers returning register
                    ssa_left = self._get_ssa_from_cl_reg_op(
                        op.get_exp().args[0], module
                    )
                    ssa_right = self._get_ssa_from_cl_reg_op(
                        op.get_exp().args[1], module
                    )

                    # add function to module
                    output_instruction = _TK_CLOPS_TO_PYQIR_REG[type(op.get_exp())](
                        module.builder
                    )(ssa_left, ssa_right)

                elif type(op.get_exp()) in _TK_CLOPS_TO_PYQIR_BIT:
                    # classical ops acting on bits returning bit
                    ssa_left = self._get_ssa_from_cl_bit_op(
                        op.get_exp().args[0], module
                    )
                    ssa_right = self._get_ssa_from_cl_bit_op(
                        op.get_exp().args[1], module
                    )

                    # add function to module
                    returntypebool = True
                    result_index = command.args[-1].index[0]  # todo
                    output_instruction = _TK_CLOPS_TO_PYQIR_BIT[type(op.get_exp())](
                        module.builder
                    )(ssa_left, ssa_right)

                elif type(op.get_exp()) in _TK_CLOPS_TO_PYQIR_REG_BOOL:
                    # classical ops acting on registers returning bit
                    ssa_left = self._get_ssa_from_cl_reg_op(
                        op.get_exp().args[0], module
                    )
                    ssa_right = self._get_ssa_from_cl_reg_op(
                        op.get_exp().args[1], module
                    )

                    # add function to module
                    returntypebool = True
                    output_instruction = _TK_CLOPS_TO_PYQIR_REG_BOOL[
                        type(op.get_exp())
                    ](module.builder)(ssa_left, ssa_right)

                else:
                    raise ValueError(" unexpected classical op")

                if returntypebool:
                    # the return value of the some classical ops is bool in qir,
                    # so the return value can only be written to one entry
                    # of the register this implementation write the value
                    # to the 0-th entry
                    # of the register, this could be changed to a user given value

                    self.module.builder.call(
                        self.set_one_bit_in_reg,
                        [
                            self.ssa_vars[outputs],
                            pyqir.const(self.qir_int_type, result_index),
                            output_instruction,
                        ],
                    )
                else:
                    self.module.builder.call(
                        self.set_all_bits_in_reg,
                        [self.ssa_vars[outputs], output_instruction],
                    )

            elif isinstance(op, SetBitsOp):
                _, outputs = self._get_c_regs_from_com(command)
                for out in outputs:
                    self.set_cregs[out] = command.op.values
            elif isinstance(op, MetaOp):

                assert command.qubits[0].reg_name == "q"

                qir_qubits = self._to_qis_qubits(command.qubits)

                if command.op.data == "":
                    self._add_barrier_op(module, len(command.qubits), qir_qubits)
                elif command.op.data[0:5] == "order":
                    self._add_order_op(module, len(command.qubits), qir_qubits)
                elif command.op.data[0:5] == "group":
                    self._add_group_op(module, len(command.qubits), qir_qubits)
                elif command.op.data[0:5] == "sleep":
                    self._add_sleep_op(
                        module,
                        len(command.qubits),
                        qir_qubits,
                        float(command.op.data[6:-1]),
                    )
                else:
                    raise ValueError("Meta op is not supported yet")

            elif isinstance(op, CopyBitsOp):
                input_reg = command.args[0]
                output_reg = command.args[1]
                output_name = output_reg.reg_name
                optype, _ = self._get_optype_and_params(op)
                gate = module.gateset.tk_to_gateset(optype)
                ssa_var = cast(Value, self.module.module.results[input_reg.index[0]])
                get_gate = getattr(module, gate.func_name.value)
                output_instr = module.builder.call(get_gate, [ssa_var])
                ssa_var_result = output_instr
                self.set_all_bits_in_reg(self.ssa_vars[output_name], ssa_var_result)  # type: ignore

            else:
                rebased_circ = self._rebase_command_to_gateset(
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
        if record_output:
            for creg in self.circuit.c_registers:
                reg_name = creg[0].reg_name
                self.module.builder.call(
                    self.record_output,
                    [
                        self.ssa_vars[reg_name],
                    ],
                )

        return module
