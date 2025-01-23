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


import pyqir
from pyqir import Value

from pytket.circuit import (
    Bit,
    BitRegister,
    Circuit,
    Command,
    Conditional,
    Qubit,
)

from .module import tketqirModule
from .qirgenerator import (
    AbstractQirGenerator,
)


class BaseProfileQirGenerator(AbstractQirGenerator):
    """Generate QIR from a pytket circuit."""

    def __init__(
        self,
        circuit: Circuit,
        module: tketqirModule,
        wasm_int_type: int,
        qir_int_type: int,
    ) -> None:

        super().__init__(circuit, module, wasm_int_type, qir_int_type)

        self.measure_results: list[list] = []

        self.reg_const_list: dict[str, list] = {}

        for creg in self.circuit.c_registers:
            reg_name = creg[0].reg_name
            self.reg_const_list[reg_name] = []

        for creg in self.circuit.c_registers:
            reg_name = creg[0].reg_name
            for i in range(creg.size):
                self.reg_const_list[reg_name].append(
                    self.module.module.add_byte_string(str.encode(f"{reg_name}[{i}]"))
                )

        entry = self.module.module.entry_block
        self.module.module.builder.insert_at_end(entry)

        # void __quantum__rt__result_record_output(result)
        self.record_output_res = self.module.module.add_external_function(
            "__quantum__rt__result_record_output",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [
                    pyqir.result_type(self.module.module.context),
                    pyqir.PointerType(pyqir.IntType(self.module.module.context, 8)),
                ],
            ),
        )

    def _get_bit_from_creg(self, creg: str, index: int) -> Value:
        raise ValueError("Classical register operations not available in base profile")

    def _set_bit_in_creg(self, creg: str, index: int, ssa_bit: Value) -> None:
        raise ValueError("Classical REG Ops Not available in base profile")

    def get_ssa_vars(self, reg_name: str) -> Value:
        raise ValueError("Classical REG Ops Not available in base profile")

    def _get_i64_ssa_reg(self, reg_name: str) -> Value:
        raise ValueError("Classical REG Ops Not available in base profile")

    def get_ssa_list(self, reg_name: str) -> list:
        raise ValueError("Classical REG Ops Not available in base profile")

    def set_ssa_vars(self, reg_name: str, ssa_i64: Value, trunc: bool) -> None:
        raise ValueError("Classical REG Ops Not available in base profile")

    def _reg2ssa_var(self, bit_reg: BitRegister) -> Value:
        raise ValueError("Classical REG Ops Not available in base profile")

    def conv_conditional(self, command: Command, op: Conditional) -> None:
        raise ValueError("Conditional not available in base profile")

    def conv_measure(self, bits: list[Bit], qubits: list[Qubit]) -> None:
        assert len(bits) == 1
        assert len(qubits) == 1

        qubit_index = qubits[0].index[0]

        self.module.qis.mz(
            self.module.module.qubits[qubit_index],
            self.module.module.results[qubit_index],
        )

        self.measure_results.append(
            [
                self.reg_const_list[bits[0].reg_name][bits[0].index[0]],
                self.module.module.results[qubit_index],
            ]
        )

    def record_output(self) -> None:

        for res in self.measure_results:
            self.module.builder.call(
                self.record_output_res,
                [
                    res[1],
                    res[0],
                ],
            )
