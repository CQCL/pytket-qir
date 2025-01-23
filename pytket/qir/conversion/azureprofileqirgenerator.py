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

from .module import tketqirModule
from .profileqirgenerator import (
    AdaptiveProfileQirGenerator,
)


class AzureAdaptiveProfileQirGenerator(AdaptiveProfileQirGenerator):
    """Generate QIR from a pytket circuit."""

    def __init__(
        self,
        circuit: Circuit,
        module: tketqirModule,
        wasm_int_type: int,
        qir_int_type: int,
        trunc: bool,
    ) -> None:

        super().__init__(circuit, module, wasm_int_type, qir_int_type, trunc)

        self.azure_sar_dict["!llvm.module.flags = !{!0, !1, !2, !3}"] = (
            "!llvm.module.flags = !{!0, !1, !2, !3, !4, !5, !6, !7, !8, !9, !10}"
        )

        self.azure_sar_dict[
            '!3 = !{i32 1, !"dynamic_result_management", i1 false}'
        ] = """!3 = !{i32 1, !"dynamic_result_management", i1 false}
!4 = !{i32 1, !"classical_ints", i1 true}
!5 = !{i32 1, !"qubit_resetting", i1 true}
!6 = !{i32 1, !"classical_floats", i1 false}
!7 = !{i32 1, !"backwards_branching", i1 false}
!8 = !{i32 1, !"classical_fixed_points", i1 false}
!9 = !{i32 1, !"user_functions", i1 false}
!10 = !{i32 1, !"multiple_target_branching", i1 false}"""

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

        self.module.builder.call(
            self.record_output_array,
            [
                pyqir.const(self.qir_int_type, len(self.circuit.c_registers)),
                pyqir.Constant.null(
                    pyqir.PointerType(pyqir.IntType(self.module.module.context, 8))
                ),
            ],
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
