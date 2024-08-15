; ModuleID = 'ptest_pytket_qir_conditional'
source_filename = "ptest_pytket_qir_conditional"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"
@3 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* null)
  br i1 false, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %0 = phi i64 [ 0, %condb0 ], [ 0, %entry ]
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 2 to %Qubit*), %Result* inttoptr (i64 2 to %Result*))
  %1 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 2 to %Result*))
  br i1 %1, label %sb_1_0, label %sb_0_0

sb_0_0:                                           ; preds = %contb0
  %2 = and i64 9223372036854775803, %0
  br label %contb0_0

sb_1_0:                                           ; preds = %contb0
  %3 = or i64 4, %0
  br label %contb0_0

contb0_0:                                         ; preds = %sb_0_0, %sb_1_0
  %4 = phi i64 [ %2, %sb_0_0 ], [ %3, %sb_1_0 ]
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %5 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  br i1 %5, label %sb_1_1, label %sb_0_1

sb_0_1:                                           ; preds = %contb0_0
  %6 = and i64 9223372036854775799, %4
  br label %contb0_1

sb_1_1:                                           ; preds = %contb0_0
  %7 = or i64 8, %4
  br label %contb0_1

contb0_1:                                         ; preds = %sb_0_1, %sb_1_1
  %8 = phi i64 [ %6, %sb_0_1 ], [ %7, %sb_1_1 ]
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %9 = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %9, label %sb_1_2, label %sb_0_2

sb_0_2:                                           ; preds = %contb0_1
  %10 = and i64 9223372036854775791, %8
  br label %contb0_2

sb_1_2:                                           ; preds = %contb0_1
  %11 = or i64 16, %8
  br label %contb0_2

contb0_2:                                         ; preds = %sb_0_2, %sb_1_2
  %12 = phi i64 [ %10, %sb_0_2 ], [ %11, %sb_1_2 ]
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %12, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="3" "required_num_results"="3" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
