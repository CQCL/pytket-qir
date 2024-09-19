; ModuleID = 'test_pytket_qir_barrier'
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

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__barrier2__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__barrier1__body(%Qubit*)

declare void @__quantum__qis__barrier4__body(%Qubit*, %Qubit*, %Qubit*, %Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="5" "required_num_results"="5" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}