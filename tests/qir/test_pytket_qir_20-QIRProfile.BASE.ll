; ModuleID = 'test_pytket_qir_20'
source_filename = "test_pytket_qir_20"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [5 x i8] c"c[0]\00"
@1 = internal constant [5 x i8] c"c[1]\00"
@2 = internal constant [5 x i8] c"c[2]\00"
@3 = internal constant [5 x i8] c"c[3]\00"
@4 = internal constant [5 x i8] c"c[4]\00"
@5 = internal constant [5 x i8] c"c[5]\00"
@6 = internal constant [5 x i8] c"c[6]\00"
@7 = internal constant [5 x i8] c"c[7]\00"
@8 = internal constant [5 x i8] c"c[8]\00"
@9 = internal constant [5 x i8] c"c[9]\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 5 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 6 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 7 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 8 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 9 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 2 to %Qubit*), %Result* inttoptr (i64 2 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 3 to %Qubit*), %Result* inttoptr (i64 3 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 4 to %Qubit*), %Result* inttoptr (i64 4 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 5 to %Qubit*), %Result* inttoptr (i64 5 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 6 to %Qubit*), %Result* inttoptr (i64 6 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 7 to %Qubit*), %Result* inttoptr (i64 7 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 8 to %Qubit*), %Result* inttoptr (i64 8 to %Result*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 9 to %Qubit*), %Result* inttoptr (i64 9 to %Result*))
  call void @__quantum__rt__result_record_output(%Result* null, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 1 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 2 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 3 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 4 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @4, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 5 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @5, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 6 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @6, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 7 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @7, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 8 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @8, i32 0, i32 0))
  call void @__quantum__rt__result_record_output(%Result* inttoptr (i64 9 to %Result*), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @9, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__result_record_output(%Result*, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="10" "required_num_results"="10" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
