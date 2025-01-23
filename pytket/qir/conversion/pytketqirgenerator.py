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

from typing import cast

import pyqir
from pyqir import Value

from pytket.circuit import (
    Bit,
    BitRegister,
    CircBox,
    Circuit,
    Command,
    Conditional,
    OpType,
    Qubit,
)

from .module import tketqirModule
from .qirgenerator import (
    AbstractQirGenerator,
)


class PytketQirGenerator(AbstractQirGenerator):
    """Generates QIR from a pytket circuit in line with the pytket profile.
    This profile uses the functions `get_creg_bit`, `set_creg_bit`,
    `set_creg_to_int`, `create_creg`, `get_int_from_creg` and
    `mz_to_creg_bit` for the handling of the classical registers.
    The other aspects of the QIR file are identical to the adaptive profile.
    """

    def __init__(
        self,
        circuit: Circuit,
        module: tketqirModule,
        wasm_int_type: int,
        qir_int_type: int,
    ) -> None:

        super().__init__(circuit, module, wasm_int_type, qir_int_type)

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

        for creg in self.circuit.c_registers:
            reg_name = creg[0].reg_name
            self.reg_const[reg_name] = self.module.module.add_byte_string(
                str.encode(reg_name)
            )

        entry = self.module.module.entry_block
        self.module.module.builder.insert_at_end(entry)

        for creg in self.circuit.c_registers:
            self._reg2ssa_var(creg, qir_int_type)

    def get_ssa_vars(self, reg_name: str) -> Value:
        if reg_name not in self.ssa_vars:
            raise ValueError(f"{reg_name} is not a valid register")
        return self.ssa_vars[reg_name]

    def _get_i64_ssa_reg(self, name: str) -> Value:
        ssa_var = self.module.builder.call(
            self.get_int_from_creg,
            [self.get_ssa_vars(name)],
        )
        return ssa_var

    def set_ssa_vars(self, reg_name: str, ssa_i64: Value, trunc: bool) -> None:

        self.module.builder.call(
            self.set_creg_to_int,
            [self.get_ssa_vars(reg_name), ssa_i64],
        )

    def _set_bit_in_creg(self, creg: str, index: int, ssa_bit: Value) -> None:
        self.module.builder.call(
            self.set_creg_bit,
            [
                self.get_ssa_vars(creg),
                pyqir.const(self.qir_int_type, index),
                ssa_bit,
            ],
        )

    def _get_bit_from_creg(self, creg: str, index: int) -> Value:
        return self.module.builder.call(
            self.get_creg_bit,
            [
                self.get_ssa_vars(creg),
                pyqir.const(self.qir_int_type, index),
            ],
        )

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

    def conv_conditional(self, command: Command, op: Conditional) -> None:
        condition_name = command.args[0].reg_name

        entry_point = self.module.module.entry_point

        condb = pyqir.BasicBlock(
            self.module.module.context, f"condb{self.block_count}", entry_point
        )
        contb = pyqir.BasicBlock(
            self.module.module.context, f"contb{self.block_count}", entry_point
        )
        self.block_count = self.block_count + 1

        if op.op.type == OpType.CircBox:
            conditional_circuit = self._decompose_conditional_circ_box(
                cast(CircBox, op.op), command.args[op.width :]
            )

            condition_name = command.args[0].reg_name

            if op.width == 1:  # only one conditional bit

                condition_bit_index = command.args[0].index[0]

                ssabool = self.module.builder.call(
                    self.get_creg_bit,
                    [
                        self.get_ssa_vars(condition_name),
                        pyqir.const(self.qir_int_type, condition_bit_index),
                    ],
                )

                if op.value == 1:
                    self.module.module.builder.condbr(ssabool, condb, contb)
                    self.module.module.builder.insert_at_end(condb)
                    self.subcircuit_to_module(conditional_circuit)

                if op.value == 0:
                    self.module.module.builder.condbr(ssabool, contb, condb)
                    self.module.module.builder.insert_at_end(condb)
                    self.subcircuit_to_module(conditional_circuit)

                self.module.module.builder.br(contb)
                self.module.module.builder.insert_at_end(contb)

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

                ssabool = self.module.module.builder.icmp(
                    pyqir.IntPredicate.EQ,
                    pyqir.const(self.qir_int_type, op.value),
                    self._get_i64_ssa_reg(condition_name),
                )

                self.module.module.builder.condbr(ssabool, condb, contb)

                self.module.module.builder.insert_at_end(condb)

                self.subcircuit_to_module(conditional_circuit)

                self.module.module.builder.br(contb)
                self.module.module.builder.insert_at_end(contb)

        else:
            condition_name = command.args[0].reg_name

            if op.width == 1:  # only one conditional bit
                condition_bit_index = command.args[0].index[0]

                ssabool = self.module.builder.call(
                    self.get_creg_bit,
                    [
                        self.get_ssa_vars(condition_name),
                        pyqir.const(self.qir_int_type, condition_bit_index),
                    ],
                )

                if op.value == 1:
                    self.module.module.builder.condbr(ssabool, condb, contb)
                    self.module.module.builder.insert_at_end(condb)
                    self.command_to_module(op.op, command.args[op.width :])

                if op.value == 0:
                    self.module.module.builder.condbr(ssabool, contb, condb)
                    self.module.module.builder.insert_at_end(condb)
                    self.command_to_module(op.op, command.args[op.width :])

                self.module.module.builder.br(contb)
                self.module.module.builder.insert_at_end(contb)

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

                ssabool = self.module.module.builder.icmp(
                    pyqir.IntPredicate.EQ,
                    pyqir.const(self.qir_int_type, op.value),
                    self._get_i64_ssa_reg(condition_name),
                )

                self.module.module.builder.condbr(ssabool, condb, contb)
                self.module.module.builder.insert_at_end(condb)

                self.command_to_module(op.op, command.args[op.width :])

                self.module.module.builder.br(contb)
                self.module.module.builder.insert_at_end(contb)

    def conv_measure(self, bits: list[Bit], qubits: list[Qubit]) -> None:

        assert len(bits) == 1
        assert len(qubits) == 1

        self.module.builder.call(
            self.mz_to_creg_bit,
            [
                self.module.module.qubits[qubits[0].index[0]],
                self.get_ssa_vars(bits[0].reg_name),
                pyqir.const(self.qir_int_type, bits[0].index[0]),
            ],
        )

    def record_output(self) -> None:

        for creg in self.circuit.c_registers:
            reg_name = creg[0].reg_name
            self.module.builder.call(
                self.record_output_i64,
                [
                    self._get_i64_ssa_reg(reg_name),
                    self.reg_const[reg_name],
                ],
            )
