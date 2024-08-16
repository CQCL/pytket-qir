; ModuleID = 'ptest_pytket_qir_conditional_10b'
source_filename = "ptest_pytket_qir_conditional_10b"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  br i1 false, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  call void @__quantum__qis__z__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__y__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* null)
  br i1 false, label %sb_1_0, label %sb_0_0

contb0:                                           ; preds = %condb0_4, %entry
  %0 = phi i64 [ %13, %condb0_4 ], [ 0, %entry ]
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  ret void

sb_0_0:                                           ; preds = %condb0
  br label %condb0_0

sb_1_0:                                           ; preds = %condb0
  br label %condb0_0

condb0_0:                                         ; preds = %sb_0_0, %sb_1_0
  %1 = phi i64 [ 0, %sb_0_0 ], [ 1, %sb_1_0 ]
  br i1 true, label %sb_1_1, label %sb_0_1

sb_0_1:                                           ; preds = %condb0_0
  %2 = and i64 9223372036854775805, %1
  br label %condb0_1

sb_1_1:                                           ; preds = %condb0_0
  %3 = or i64 2, %1
  br label %condb0_1

condb0_1:                                         ; preds = %sb_0_1, %sb_1_1
  %4 = phi i64 [ %2, %sb_0_1 ], [ %3, %sb_1_1 ]
  br i1 false, label %sb_1_2, label %sb_0_2

sb_0_2:                                           ; preds = %condb0_1
  %5 = and i64 9223372036854775803, %4
  br label %condb0_2

sb_1_2:                                           ; preds = %condb0_1
  %6 = or i64 4, %4
  br label %condb0_2

condb0_2:                                         ; preds = %sb_0_2, %sb_1_2
  %7 = phi i64 [ %5, %sb_0_2 ], [ %6, %sb_1_2 ]
  br i1 false, label %sb_1_3, label %sb_0_3

sb_0_3:                                           ; preds = %condb0_2
  %8 = and i64 9223372036854775799, %7
  br label %condb0_3

sb_1_3:                                           ; preds = %condb0_2
  %9 = or i64 8, %7
  br label %condb0_3

condb0_3:                                         ; preds = %sb_0_3, %sb_1_3
  %10 = phi i64 [ %8, %sb_0_3 ], [ %9, %sb_1_3 ]
  br i1 false, label %sb_1_4, label %sb_0_4

sb_0_4:                                           ; preds = %condb0_3
  %11 = and i64 9223372036854775791, %10
  br label %condb0_4

sb_1_4:                                           ; preds = %condb0_3
  %12 = or i64 16, %10
  br label %condb0_4

condb0_4:                                         ; preds = %sb_0_4, %sb_1_4
  %13 = phi i64 [ %11, %sb_0_4 ], [ %12, %sb_1_4 ]
  br label %contb0
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__x__body(%Qubit*)

declare void @__quantum__qis__z__body(%Qubit*)

declare void @__quantum__qis__y__body(%Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="4" "required_num_results"="4" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
