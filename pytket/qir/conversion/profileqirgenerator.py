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
from pyqir import BasicBlock, Value

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


class AdaptiveProfileQirGenerator(AbstractQirGenerator):
    """Generate QIR from a pytket circuit."""

    def __init__(
        self,
        circuit: Circuit,
        module: tketqirModule,
        wasm_int_type: int,
        qir_int_type: int,
        trunc: bool,
    ) -> None:

        self.trunc = trunc

        super().__init__(circuit, module, wasm_int_type, qir_int_type)

        self.set_cregs: dict[str, list] = {}  # Keep track of set registers.
        self.ssa_vars: dict[str, list[tuple[Value, BasicBlock]]] = (
            {}
        )  # Keep track of set ssa variables.
        self.list_of_changed_cregs: list[str] = []

        for creg in self.circuit.c_registers:
            reg_name = creg[0].reg_name
            self.reg_const[reg_name] = self.module.module.add_byte_string(
                str.encode(reg_name)
            )

        entry = self.module.module.entry_block
        self.module.module.builder.insert_at_end(entry)
        self.active_block = entry
        self.active_block_main = entry
        self.active_block_list = [entry]

        # set the prefix for the names of the conditional blocks
        self.conditional_bp = "condb"
        # set the prefix for the names of the continue blocks
        self.continue_bp = "contb"

        assert self.conditional_bp != self.continue_bp
        assert self.conditional_bp != "entry"
        assert self.continue_bp != "entry"
        # the code is assuming that the prefixes have length 5
        assert len(self.conditional_bp) == 5
        assert len(self.continue_bp) == 5

        for creg in self.circuit.c_registers:
            self._reg2ssa_var(creg)
            self.list_of_changed_cregs.append(creg.name)
            self.creg_size[creg.name] = creg.size

    def _get_bit_from_creg(self, creg: str, index: int) -> Value:
        ssa_index = pyqir.const(self.qir_int_type, 2**index)

        result = self.module.module.builder.icmp(
            pyqir.IntPredicate.EQ,
            ssa_index,
            self.module.module.builder.and_(ssa_index, self.get_ssa_vars(creg)),
        )

        return result

    def _set_bit_in_creg_blocks(self, creg: str, index: int, ssa_bit: Value) -> None:
        ssa_int = self.get_ssa_vars(creg)

        ssa_index = pyqir.const(self.qir_int_type, 2**index)

        # it would be better to do an invert here, but that is not
        # (yet) available in pyqir
        ssa_int_all_1 = pyqir.const(self.qir_int_type, (2 ** (self.int_size - 1) - 1))

        entry_point = self.module.module.entry_point

        sb_0 = pyqir.BasicBlock(
            self.module.module.context, f"sb_0_{self.block_count_sb}", entry_point
        )
        sb_1 = pyqir.BasicBlock(
            self.module.module.context, f"sb_1_{self.block_count_sb}", entry_point
        )

        continue_block = pyqir.BasicBlock(
            self.module.module.context,
            f"{self.active_block_main.name}_{self.block_count_sb}",
            entry_point,
        )
        if self.active_block_main.name[0:5] != self.conditional_bp:
            self.active_block_list.append(continue_block)

        self.block_count_sb = self.block_count_sb + 1
        self.module.module.builder.condbr(ssa_bit, sb_1, sb_0)

        # if bit 1
        self.module.module.builder.insert_at_end(sb_1)
        result_1 = self.module.module.builder.or_(ssa_index, ssa_int)
        self.module.module.builder.br(continue_block)

        # if bit 0
        self.module.module.builder.insert_at_end(sb_0)
        result_0 = self.module.module.builder.and_(
            self.module.module.builder.xor(
                ssa_index,
                ssa_int_all_1,
            ),
            ssa_int,
        )
        self.module.module.builder.br(continue_block)

        # phi and continue
        self.active_block = continue_block
        self.module.module.builder.insert_at_end(continue_block)
        phi = self.module.module.builder.phi(self.qir_int_type)
        phi.add_incoming(result_0, sb_0)
        phi.add_incoming(result_1, sb_1)

        self.set_ssa_vars(creg, phi, False)

    def _set_bit_in_creg_zext(self, creg: str, index: int, ssa_bit: Value) -> None:
        ssa_int = self.get_ssa_vars(creg)
        ssa_bit_i64 = self.module.module.builder.zext(ssa_bit, self.qir_int_type)
        ssa_index = pyqir.const(self.qir_int_type, 2**index)
        # it would be better to do an invert here, but that is not
        # (yet) available in pyqir
        ssa_int_all_1 = pyqir.const(self.qir_int_type, (2 ** (self.int_size - 1) - 1))

        # if ssa_bit is 1, ((BIT) MUL (2^INDEX) ) OR INT
        ssa_result_1 = self.module.module.builder.or_(
            self.module.module.builder.mul(ssa_bit_i64, ssa_index), ssa_int
        )

        # if ssa_bit is 0, ((2**63-1) XOR ((1-BIT) MUL (2^INDEX))) and INT
        ssa_result_0 = self.module.module.builder.and_(
            self.module.module.builder.xor(
                ssa_int_all_1,
                self.module.module.builder.mul(
                    self.module.module.builder.sub(
                        pyqir.const(self.qir_int_type, 1), ssa_bit_i64
                    ),
                    ssa_index,
                ),
            ),
            ssa_result_1,
        )

        # set ssa
        self.set_ssa_vars(creg, ssa_result_0, False)

    def _set_bit_in_creg(self, creg: str, index: int, ssa_bit: Value) -> None:
        self._set_bit_in_creg_zext(creg, index, ssa_bit)

    def get_ssa_vars(self, reg_name: str) -> Value:
        if reg_name not in self.ssa_vars:
            raise ValueError(f"{reg_name} is not a valid register")
        return self.ssa_vars[reg_name][-1][0]

    def _get_i64_ssa_reg(self, reg_name: str) -> Value:
        if reg_name not in self.ssa_vars:
            raise ValueError(f"{reg_name} is not a valid register")
        return self.ssa_vars[reg_name][-1][0]

    def get_ssa_list(self, reg_name: str) -> list:
        if reg_name not in self.ssa_vars:
            raise ValueError(f"{reg_name} is not a valid register")
        return self.ssa_vars[reg_name]

    def set_ssa_vars(self, reg_name: str, ssa_i64: Value, trunc: bool) -> None:
        if reg_name not in self.ssa_vars:
            raise ValueError(f"{reg_name} is not a valid register")
        if self.trunc and trunc and self.creg_size[reg_name] != self.int_size:
            type_register = pyqir.IntType(self.module.context, self.creg_size[reg_name])
            ssa_i_trunc = self.module.module.builder.trunc(ssa_i64, type_register)
            ssa_i64_zext = self.module.module.builder.zext(
                ssa_i_trunc, self.qir_int_type
            )
            self.ssa_vars[reg_name].append((ssa_i64_zext, self.active_block))
        else:
            self.ssa_vars[reg_name].append((ssa_i64, self.active_block))
        self.list_of_changed_cregs.append(reg_name)

    def _reg2ssa_var(self, bit_reg: BitRegister) -> Value:
        """Convert a BitRegister to an SSA variable using pyqir types."""
        reg_name = bit_reg[0].reg_name
        if reg_name not in self.ssa_vars:
            if len(bit_reg) > self.int_size:
                raise ValueError(
                    f"Classical register should only have the size of {self.int_size}"
                )
            ssa_var = pyqir.const(self.qir_int_type, 0)
            self.ssa_vars[reg_name] = [(ssa_var, self.active_block)]
            return ssa_var
        else:
            return cast(Value, self.ssa_vars[reg_name])

    def _add_phi(self) -> None:
        """
        add phi nodes for the previously changed registers.
        phi requires ssa variables from both predecessor blocks,
        these are not necessarily the blocks where the variables
        have been set. The second loop searches for the second variable
        and adds that with the other predecessor
        """

        for creg in set(self.list_of_changed_cregs):
            phi = self.module.module.builder.phi(self.qir_int_type)
            ssa_list = self.get_ssa_list(creg)
            # the first predecessor if the direct previous (last) entry in the ssa list
            phi.add_incoming(ssa_list[-1][0], ssa_list[-1][1])

            found_second_block = False

            # search for the other ssa variable
            for i in range(-2, -len(ssa_list) - 1, -1):
                if (
                    ssa_list[-1][1].name != ssa_list[i][1].name
                    and ssa_list[i][1].name[0:5] != self.conditional_bp
                ):
                    assert self.active_block_list[-3].name[0:5] != self.conditional_bp
                    # self.active_block_list[-3] is the second predecessor
                    phi.add_incoming(ssa_list[i][0], self.active_block_list[-3])
                    found_second_block = True
                    break

            if not found_second_block:
                raise RuntimeError("Second block missing in phi generation")

            self.set_ssa_vars(creg, phi, False)

    def conv_conditional(self, command: Command, op: Conditional) -> None:
        condition_name = command.args[0].reg_name

        entry_point = self.module.module.entry_point

        condb = pyqir.BasicBlock(
            self.module.module.context,
            f"{self.conditional_bp}{self.block_count}",
            entry_point,
        )
        contb = pyqir.BasicBlock(
            self.module.module.context,
            f"{self.continue_bp}{self.block_count}",
            entry_point,
        )
        self.block_count = self.block_count + 1
        self.active_block_list.append(condb)
        self.active_block_list.append(contb)

        if op.op.type == OpType.CircBox:
            conditional_circuit = self._decompose_conditional_circ_box(
                cast(CircBox, op.op), command.args[op.width :]
            )

            condition_name = command.args[0].reg_name

            if op.width == 1:  # only one conditional bit

                condition_bit_index = command.args[0].index[0]

                ssa_bool = self._get_bit_from_creg(condition_name, condition_bit_index)

                self.list_of_changed_cregs = []
                self.active_block = condb
                self.active_block_main = condb

                if op.value == 1:
                    self.module.module.builder.condbr(ssa_bool, condb, contb)
                    self.module.module.builder.insert_at_end(condb)
                    self.subcircuit_to_module(conditional_circuit)

                if op.value == 0:
                    self.module.module.builder.condbr(ssa_bool, contb, condb)
                    self.module.module.builder.insert_at_end(condb)
                    self.subcircuit_to_module(conditional_circuit)

                self.module.module.builder.br(contb)
                self.module.module.builder.insert_at_end(contb)

                self.active_block = contb
                self.active_block_main = contb

                self._add_phi()

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

                ssa_bool = self.module.module.builder.icmp(
                    pyqir.IntPredicate.EQ,
                    pyqir.const(self.qir_int_type, op.value),
                    self.get_ssa_vars(condition_name),
                )

                self.module.module.builder.condbr(ssa_bool, condb, contb)

                self.module.module.builder.insert_at_end(condb)

                self.list_of_changed_cregs = []
                self.active_block = condb
                self.active_block_main = condb

                self.subcircuit_to_module(conditional_circuit)

                self.module.module.builder.br(contb)
                self.module.module.builder.insert_at_end(contb)

                self.active_block = contb
                self.active_block_main = contb

                self._add_phi()

        else:
            condition_name = command.args[0].reg_name

            if op.width == 1:  # only one conditional bit
                condition_bit_index = command.args[0].index[0]

                ssa_bool = self._get_bit_from_creg(condition_name, condition_bit_index)

                self.list_of_changed_cregs = []
                self.active_block = condb
                self.active_block_main = condb

                if op.value == 1:
                    self.module.module.builder.condbr(ssa_bool, condb, contb)
                    self.module.module.builder.insert_at_end(condb)
                    self.command_to_module(op.op, command.args[op.width :])

                if op.value == 0:
                    self.module.module.builder.condbr(ssa_bool, contb, condb)
                    self.module.module.builder.insert_at_end(condb)
                    self.command_to_module(op.op, command.args[op.width :])

                self.module.module.builder.br(contb)
                self.module.module.builder.insert_at_end(contb)

                self.active_block = contb
                self.active_block_main = contb

                self._add_phi()

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

                ssa_bool = self.module.module.builder.icmp(
                    pyqir.IntPredicate.EQ,
                    pyqir.const(self.qir_int_type, op.value),
                    self.get_ssa_vars(condition_name),
                )

                self.module.module.builder.condbr(ssa_bool, condb, contb)
                self.module.module.builder.insert_at_end(condb)

                self.list_of_changed_cregs = []
                self.active_block = condb
                self.active_block_main = condb

                self.command_to_module(op.op, command.args[op.width :])

                self.module.module.builder.br(contb)
                self.module.module.builder.insert_at_end(contb)

                self.active_block = contb
                self.active_block_main = contb

                self._add_phi()

    def conv_measure(self, bits: list[Bit], qubits: list[Qubit]) -> None:

        assert len(bits) == 1
        assert len(qubits) == 1

        qubit_index = qubits[0].index[0]

        self.module.qis.mz(
            self.module.module.qubits[qubit_index],
            self.module.module.results[qubit_index],
        )

        ssa_measureresult = self.module.builder.call(
            self.read_bit_from_result,
            [
                self.module.module.results[qubit_index],
            ],
        )

        self._set_bit_in_creg(bits[0].reg_name, bits[0].index[0], ssa_measureresult)

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
