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

from functools import partial
from typing import cast, Dict, List, Optional, Sequence, Tuple

from pyqir import Value, IntPredicate
import pyqir

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
)
from pytket.passes import auto_rebase_pass  # type: ignore

from .gatesets import (
    FuncSpec,
)

from .module import tketqirModule


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
        self.ssa_vars: Dict[str, List[Value]] = {}  # Keep track of set ssa variables.
        self.notupdated = False

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
            # print(dir(self.circuit))
            # print("\n\n")
            for cr in self.circuit.c_registers:
                # print(dir(cr))
                # print("\n\n")
                circuit.add_c_register(cr.name, cr.size)

            # print(args)
            # print(dir(op))
            # print(op.get_exp)
            # print(dir(op.get_exp))

            circuit.add_gate(op, args)
            # exit()
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
            reg2var = self.module.module.add_external_function(
                "reg2var",
                pyqir.FunctionType(
                    pyqir.IntType(self.module.module.context, int_size),
                    [pyqir.IntType(self.module.module.context, 1)] * int_size,
                ),
            )
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
            ssa_var = cast(Value, self.module.builder.call(reg2var, [*bool_reg]))  # type: ignore
            self.ssa_vars[reg_name] = [ssa_var]
            return ssa_var
        else:
            return cast(Value, self.ssa_vars[reg_name][-1])  # type: ignore

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
        elif isinstance(op, ClassicalExpBox):
            for reglist, sizes in [
                (
                    inputs,
                    list(
                        map(
                            lambda obj: obj.size  # type: ignore
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
                        raise ValueError(
                            "ClassicalExpBox op input or output \
                            registers have empty widths."
                        )
                    com_bits = args[:in_width]
                    args = args[in_width:]
                    regname = com_bits[0].reg_name
                    if com_bits != list(self.cregs[regname]):
                        raise ValueError(
                            "ClassicalExpBox ops must act on entire registers."
                        )
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

    def circuit_to_module(
        self, circuit: Circuit, module: tketqirModule
    ) -> tketqirModule:
        """Populate a PyQir module from a pytket circuit."""
        for command in circuit:
            op = command.op
            if isinstance(op, Conditional):
                assert op.width == 1  # only one conditional bit
                # if not op.op.is_gate
                conditional_circuit = self._rebase_op_to_gateset(
                    op.op, command.args[op.width :]
                )
                condition_bit_index = command.args[0].index[0]
                condition_name = command.args[0].reg_name

                # condition_ssa = module.module.results[condition_bit_index]

                self.notupdated = False

                def condition_block() -> None:
                    """
                    Populate recursively the module with the contents of the conditional
                    sub-circuit when the condition is True.
                    """
                    if op.value == 1:
                        self.circuit_to_module(conditional_circuit, module)

                if condition_name in self.ssa_vars:
                    extracti1fromi64 = self.module.module.add_external_function(
                        "extracti1fromi64",
                        pyqir.FunctionType(
                            pyqir.IntType(self.module.module.context, 1),
                            [self.qir_int_type] * 2,
                        ),
                    )

                    ssabool = module.builder.call(
                        extracti1fromi64,
                        [
                            self.ssa_vars[condition_name][-1],
                            pyqir.const(self.qir_int_type, condition_bit_index),
                        ],
                    )

                    module.module.builder.if_(
                        ssabool,
                        true=lambda: condition_block(),  # type: ignore
                    )

                else:
                    module.qis.if_result(
                        module.module.results[condition_bit_index],
                        lambda: condition_block(),
                    )

                print(dir(module.module))
                print(dir(module.module.ir()))
                print(module.module.ir())
                print(self.ssa_vars)

                if self.notupdated:
                    # this is the point where the PHI node needs to be added
                    assert len(self.ssa_vars[self.lastupdatedreg]) > 1
                    # print(module.module.functions)

                    """tryphi = pyqir.Phi.incoming(
                        [
                            (self.ssa_vars[self.lastupdatedreg][-1], "%then"),
                            (self.ssa_vars[self.lastupdatedreg][-2], "%entry"),
                        ]
                    )
                    exit()"""

            elif isinstance(op, WASMOp):
                raise ValueError("WASM not supported yet")
                """#elif op.type == OpType.Measure:
            #    # todo##

                # raise ValueError("MEASURE not supported yet")

                self.notupdated = True
                self.lastupdatedreg = outputs[0]
                if outputs[0] not in self.ssa_vars.keys():
                    self.ssa_vars[outputs[0]] = [output_instr]
                else:
                    self.ssa_vars[outputs[0]].append(output_instr)"""

            elif isinstance(op, ClassicalExpBox):
                inputs, outputs = self._get_c_regs_from_com(command)
                ssa_vars: List = []
                for inp in inputs:
                    bit_reg = circuit.get_c_register(inp)
                    ssa_vars.append(self._reg2ssa_var(bit_reg, self.qir_int_type.width))
                output_instr = _TK_CLOPS_TO_PYQIR[type(op.get_exp())](module.builder)(
                    *ssa_vars
                )
                self.notupdated = True
                self.lastupdatedreg = outputs[0]
                if outputs[0] not in self.ssa_vars.keys():
                    self.ssa_vars[outputs[0]] = [output_instr]
                else:
                    self.ssa_vars[outputs[0]].append(output_instr)
            elif isinstance(op, SetBitsOp):
                _, outputs = self._get_c_regs_from_com(command)
                for out in outputs:
                    self.set_cregs[out] = command.op.values
            elif isinstance(op, MetaOp):
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
                self.notupdated = True
                self.lastupdatedreg = output_name
                if output_name not in self.ssa_vars.keys():
                    self.ssa_vars[output_name] = [output_instr]
                else:
                    self.ssa_vars[output_name].append(output_instr)

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
        return module
