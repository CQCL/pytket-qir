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

from pytket.circuit import (
    Bit,
    Circuit,
    Qubit,
)

from .baseprofileqirgenerator import (
    BaseProfileQirGenerator,
)
from .module import tketqirModule


class AzureBaseProfileQirGenerator(BaseProfileQirGenerator):
    """Generate QIR from a pytket circuit."""

    def __init__(
        self,
        circuit: Circuit,
        module: tketqirModule,
        wasm_int_type: int,
        qir_int_type: int,
    ) -> None:

        super().__init__(circuit, module, wasm_int_type, qir_int_type)

        # void @__quantum__rt__array_record_output(result)
        self.record_output_array = self.module.module.add_external_function(
            "__quantum__rt__array_record_output",
            pyqir.FunctionType(
                pyqir.Type.void(self.module.module.context),
                [
                    self.qir_int_type,
                    pyqir.PointerType(pyqir.IntType(self.module.module.context, 8)),
                ],
            ),
        )

    def conv_measure(self, bits: list[Bit], qubits: list[Qubit]) -> None:
        assert len(bits) == 1
        assert len(qubits) == 1

    def record_output(self) -> None:

        # this will measure all qubits at the end of the circuit
        # the result of the measurement will be added to an array and recorded together

        for i in range(len(self.circuit.qubits)):
            self.module.qis.mz(
                self.module.module.qubits[i],
                self.module.module.results[i],
            )

        self.module.builder.call(
            self.record_output_array,
            [
                pyqir.const(self.qir_int_type, len(self.circuit.qubits)),
                pyqir.Constant.null(
                    pyqir.PointerType(pyqir.IntType(self.module.module.context, 8))
                ),
            ],
        )

        for i in range(len(self.circuit.qubits)):
            self.module.builder.call(
                self.record_output_res,
                [
                    self.module.module.results[i],
                    pyqir.Constant.null(
                        pyqir.PointerType(pyqir.IntType(self.module.module.context, 8))
                    ),
                ],
            )
