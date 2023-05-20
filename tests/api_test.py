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

from pytket.qir.conversion.api import pytket_to_qir, ReturnTypeQIR

from pytket.circuit import Circuit, Qubit, Bit, BitRegister  # type: ignore

from pytket.circuit.logic_exp import (  # type: ignore
    reg_eq,
    reg_neq,
    reg_geq,
    reg_gt,
    reg_lt,
    reg_leq,
)
import base64


def test_pytket_qir_BINARY() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(
        circ, name="test_pytket_qir", returntype=ReturnTypeQIR.BINARY
    )

    assert type(result) == bytes

    resultb64 = base64.b64encode(result)

    print(resultb64)

    assert (
        resultb64
        == b"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YSAAAAsAAAATBEEsEAAAAAEAAABERwAAIwYFAIJgUBmBhgMBAgAAAAdQEM0UYQAAAAAAAHEgAAADAAAAMg4QIoQAwgMAAAAAAAAAAF0MAAByAAAAEgOUewMAAABtYWlucmVhZF9iaXRfZnJvbV9yZWdzZXRfb25lX2JpdF9pbl9yZWdzZXRfYWxsX2JpdHNfaW5fcmVnX19xdWFudHVtX19xaXNfX3JlYWRfcmVzdWx0X19ib2R5cmVnMnZhcl9fcXVhbnR1bV9fcnRfX2ludF9yZWNvcmRfb3V0cHV0X19xdWFudHVtX19xaXNfX2JhcnJpZXIxX19ib2R5X19xdWFudHVtX19xaXNfX29yZGVyMV9fYm9keV9fcXVhbnR1bV9fcWlzX19ncm91cDFfX2JvZHlfX3F1YW50dW1fX3Fpc19fc2xlZXAxX19ib2R5X19xdWFudHVtX19xaXNfX2JhcnJpZXIyX19ib2R5X19xdWFudHVtX19xaXNfX29yZGVyMl9fYm9keV9fcXVhbnR1bV9fcWlzX19ncm91cDJfX2JvZHlfX3F1YW50dW1fX3Fpc19fc2xlZXAyX19ib2R5X19xdWFudHVtX19xaXNfX2hfX2JvZHkxNC4wLjYgZjI4YzAwNmE1ODk1ZmMwZTMyOWZlMTVmZWFkODFlMzc0NTdjYjFkMXRlc3RfcHl0a2V0X3FpcgAAAAAA"
    )


def test_pytket_qir() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(
        circ, name="test_pytket_qir", returntype=ReturnTypeQIR.STRING
    )

    print(result)

    assert (
        result
        == """; ModuleID = 'test_pytket_qir'
source_filename = "test_pytket_qir"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__order1__body(%Qubit*)

declare void @__quantum__qis__group1__body(%Qubit*)

declare void @__quantum__qis__sleep1__body(%Qubit*)

declare void @__quantum__qis__barrier2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__order2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__group2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__sleep2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


def test_pytket_qir_2() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_2", returntype=ReturnTypeQIR.STRING
    )

    print(result)

    assert (
        result
        == """; ModuleID = 'test_pytket_qir_2'
source_filename = "test_pytket_qir_2"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__order1__body(%Qubit*)

declare void @__quantum__qis__group1__body(%Qubit*)

declare void @__quantum__qis__sleep1__body(%Qubit*)

declare void @__quantum__qis__barrier2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__order2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__group2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__sleep2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


def test_pytket_qir_ii() -> None:
    circ = Circuit(3, 3)
    circ.H(0)
    circ.H(1)
    circ.H(2)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_ii", returntype=ReturnTypeQIR.STRING
    )

    print(result)

    assert (
        result
        == """; ModuleID = 'test_pytket_qir_ii'
source_filename = "test_pytket_qir_ii"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__rt__int_record_output(i64 %0)
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__order1__body(%Qubit*)

declare void @__quantum__qis__group1__body(%Qubit*)

declare void @__quantum__qis__sleep1__body(%Qubit*)

declare void @__quantum__qis__barrier2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__order2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__group2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__sleep2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


def test_pytket_qir_5_ii() -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_classicalexpbox_register(a | b, c)
    circ.H(0)
    circ.H(0, condition=b[4])
    circ.H(0)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_5_ii", returntype=ReturnTypeQIR.STRING
    )

    print(result)

    assert (
        result
        == """; ModuleID = 'test_pytket_qir_5_ii'
source_filename = "test_pytket_qir_5_ii"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %2 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %3 = or i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %3)
  call void @__quantum__qis__h__body(%Qubit* null)
  %4 = call i1 @read_bit_from_reg(i64 %1, i64 4)
  br i1 %4, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__rt__int_record_output(i64 %0)
  call void @__quantum__rt__int_record_output(i64 %1)
  call void @__quantum__rt__int_record_output(i64 %2)
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__order1__body(%Qubit*)

declare void @__quantum__qis__group1__body(%Qubit*)

declare void @__quantum__qis__sleep1__body(%Qubit*)

declare void @__quantum__qis__barrier2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__order2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__group2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__sleep2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


def test_pytket_qir_5_iii() -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_c_register("d", 5)
    circ.add_classicalexpbox_register(a | b, c)
    circ.H(0)
    circ.H(0, condition=Bit(3))
    circ.H(0)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_5_iii", returntype=ReturnTypeQIR.STRING
    )

    print(result)

    assert circ.c_registers == [
        BitRegister("a", 5),
        BitRegister("b", 5),
        BitRegister("c", 5),
        BitRegister("d", 5),
    ]

    assert (
        result
        == """; ModuleID = 'test_pytket_qir_5_iii'
source_filename = "test_pytket_qir_5_iii"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %2 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %3 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %4 = or i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %4)
  call void @__quantum__qis__h__body(%Qubit* null)
  %5 = call i1 @read_bit_from_reg(i64 %2, i64 3)
  br i1 %5, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__rt__int_record_output(i64 %0)
  call void @__quantum__rt__int_record_output(i64 %1)
  call void @__quantum__rt__int_record_output(i64 %2)
  call void @__quantum__rt__int_record_output(i64 %3)
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__order1__body(%Qubit*)

declare void @__quantum__qis__group1__body(%Qubit*)

declare void @__quantum__qis__sleep1__body(%Qubit*)

declare void @__quantum__qis__barrier2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__order2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__group2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__sleep2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


def test_pytket_qir_5() -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_c_register("d", 5)
    circ.add_classicalexpbox_register(a | b, c)
    circ.H(2)
    circ.H(1)
    circ.X(0)
    circ.Measure(Qubit(0), c[4])
    circ.Z(0, condition=c[4])
    circ.H(0)

    assert circ.n_qubits == 3
    assert circ.n_bits == 20

    result = pytket_to_qir(
        circ, name="test_pytket_qir_5", returntype=ReturnTypeQIR.STRING
    )

    print(result)

    assert (
        result
        == """; ModuleID = 'test_pytket_qir_5'
source_filename = "test_pytket_qir_5"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %2 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %3 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %4 = or i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %4)
  call void @__quantum__qis__x__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %5 = call i1 @__quantum__qis__read_result__body(%Result* null)
  call void @set_one_bit_in_reg(i64 %2, i64 4, i1 %5)
  %6 = call i1 @read_bit_from_reg(i64 %2, i64 4)
  br i1 %6, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__z__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__rt__int_record_output(i64 %0)
  call void @__quantum__rt__int_record_output(i64 %1)
  call void @__quantum__rt__int_record_output(i64 %2)
  call void @__quantum__rt__int_record_output(i64 %3)
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__order1__body(%Qubit*)

declare void @__quantum__qis__group1__body(%Qubit*)

declare void @__quantum__qis__sleep1__body(%Qubit*)

declare void @__quantum__qis__barrier2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__order2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__group2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__sleep2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__x__body(%Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

declare void @__quantum__qis__z__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


def test_pytket_qir_3() -> None:
    # test calssical exp box handling
    circ = Circuit(2)
    a = circ.add_c_register("a", 3)
    b = circ.add_c_register("b", 3)
    c = circ.add_c_register("c", 3)
    d = circ.add_c_register("d", 3)
    circ.add_classicalexpbox_register(a & d, c)
    circ.add_classicalexpbox_register(a | b, c)
    circ.add_classicalexpbox_register(a ^ b, c)
    circ.add_classicalexpbox_register(a + b, c)
    circ.add_classicalexpbox_register(a - b, c)
    circ.add_classicalexpbox_register(a * b, c)
    # circ.add_classicalexpbox_register(a // b, c) No division yet.
    circ.add_classicalexpbox_register(a << b, c)
    circ.add_classicalexpbox_register(a >> b, c)
    circ.add_classicalexpbox_register(reg_eq(a, b), c)
    circ.add_classicalexpbox_register(reg_neq(a, b), c)
    circ.add_classicalexpbox_register(reg_gt(a, b), c)
    circ.add_classicalexpbox_register(reg_geq(a, b), c)
    circ.add_classicalexpbox_register(reg_lt(a, b), c)
    circ.add_classicalexpbox_register(reg_leq(a, b), c)

    assert circ.n_qubits == 2
    assert circ.n_bits == 12

    result = pytket_to_qir(
        circ, name="test_pytket_qir_3", returntype=ReturnTypeQIR.STRING
    )

    print(result)

    assert (
        result
        == """; ModuleID = 'test_pytket_qir_3'
source_filename = "test_pytket_qir_3"

%Result = type opaque
%Qubit = type opaque

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %2 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %3 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %4 = and i64 %0, %3
  call void @set_all_bits_in_reg(i64 %2, i64 %4)
  %5 = or i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %5)
  %6 = xor i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %6)
  %7 = add i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %7)
  %8 = sub i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %8)
  %9 = mul i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %9)
  %10 = shl i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %10)
  %11 = lshr i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %11)
  %12 = icmp eq i64 %0, %1
  call void @set_one_bit_in_reg(i64 %2, i64 0, i1 %12)
  %13 = icmp ne i64 %0, %1
  call void @set_one_bit_in_reg(i64 %2, i64 0, i1 %13)
  %14 = icmp ugt i64 %0, %1
  call void @set_one_bit_in_reg(i64 %2, i64 0, i1 %14)
  %15 = icmp uge i64 %0, %1
  call void @set_one_bit_in_reg(i64 %2, i64 0, i1 %15)
  %16 = icmp ult i64 %0, %1
  call void @set_one_bit_in_reg(i64 %2, i64 0, i1 %16)
  %17 = icmp ule i64 %0, %1
  call void @set_one_bit_in_reg(i64 %2, i64 0, i1 %17)
  call void @__quantum__rt__int_record_output(i64 %0)
  call void @__quantum__rt__int_record_output(i64 %1)
  call void @__quantum__rt__int_record_output(i64 %2)
  call void @__quantum__rt__int_record_output(i64 %3)
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__order1__body(%Qubit*)

declare void @__quantum__qis__group1__body(%Qubit*)

declare void @__quantum__qis__sleep1__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="2" "num_required_results"="2" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
"""
    )


if __name__ == "__main__":
    test_pytket_qir()
    test_pytket_qir_2()
    test_pytket_qir_ii()
    test_pytket_qir_5_ii()
    test_pytket_qir_5_iii()
    test_pytket_qir_5()
    test_pytket_qir_3()
