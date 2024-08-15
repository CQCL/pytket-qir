; ModuleID = 'ptest_pytket_qir_conditional_v'
source_filename = "ptest_pytket_qir_conditional_v"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %0, label %sb_1_0, label %sb_0_0

sb_0_0:                                           ; preds = %entry
  br label %entry_0

sb_1_0:                                           ; preds = %entry
  br label %entry_0

entry_0:                                          ; preds = %sb_0_0, %sb_1_0
  %1 = phi i64 [ 0, %sb_0_0 ], [ 1, %sb_1_0 ]
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %2 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  br i1 %2, label %sb_1_1, label %sb_0_1

sb_0_1:                                           ; preds = %entry_0
  %3 = and i64 9223372036854775805, %1
  br label %entry_1

sb_1_1:                                           ; preds = %entry_0
  %4 = or i64 2, %1
  br label %entry_1

entry_1:                                          ; preds = %sb_0_1, %sb_1_1
  %5 = phi i64 [ %3, %sb_0_1 ], [ %4, %sb_1_1 ]
  %6 = icmp eq i64 3, %5
  br i1 %6, label %condb0, label %contb0

condb0:                                           ; preds = %entry_1
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry_1
  call void @__quantum__rt__int_record_output(i64 %5, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="2" "required_num_results"="2" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
