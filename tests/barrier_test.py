# Copyright 2020-2023 Cambridge Quantum Computing
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

from pytket.qir.conversion.api import pytket_to_qir, QIRFormat

from pytket.circuit import (
    Circuit,
)


def test_pytket_qir_barrier() -> None:
    # test barrier handling

    circ = Circuit(5)
    circ.H(0)
    circ.add_barrier([0, 1])
    circ.H(1)
    circ.add_barrier([0])
    circ.H(1)
    circ.add_barrier([0, 1, 3, 4])
    circ.H(4)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_barrier", returntype=QIRFormat.STRING
    )

    print(result)

    assert (
        result
        == """; ModuleID = 'test_pytket_qir_barrier'
source_filename = "test_pytket_qir_barrier"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__barrier2__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__barrier1__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__barrier4__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* inttoptr (i64 3 to %Qubit*), %Qubit* inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 4 to %Qubit*))
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__barrier2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__barrier4__body(%Qubit*, %Qubit*, %Qubit*, %Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="5" "num_required_results"="5" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


def test_pytket_qir_barrier_ii() -> None:
    # test barrier handling

    circ = Circuit(5)
    circ.H(0)
    circ.add_barrier([0, 1], data="order2")
    circ.add_barrier([0, 1, 4], data="order3")
    circ.H(1)
    circ.add_barrier([0, 1], data="group2")
    circ.add_barrier([0, 1, 4], data="group3")
    circ.H(1)
    circ.add_barrier([1], data="sleep(5.1)")
    circ.add_barrier([0], data="sleep(10000)")

    result = pytket_to_qir(
        circ, name="test_pytket_qir_barrier_ii", returntype=QIRFormat.STRING
    )

    print(result)

    assert (
        result
        == """; ModuleID = 'test_pytket_qir_barrier_ii'
source_filename = "test_pytket_qir_barrier_ii"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__order2__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__order3__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__group2__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__group3__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__sleep__body(%Qubit* null, double 1.000000e+04)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__sleep__body(%Qubit* inttoptr (i64 1 to %Qubit*), double 5.100000e+00)
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__order2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__order3__body(%Qubit*, %Qubit*, %Qubit*)

declare void @__quantum__qis__group2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__group3__body(%Qubit*, %Qubit*, %Qubit*)

declare void @__quantum__qis__sleep__body(%Qubit*, double)

attributes #0 = { "entry_point" "num_required_qubits"="5" "num_required_results"="5" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


if __name__ == "__main__":
    test_pytket_qir_barrier()
    test_pytket_qir_barrier_ii()
