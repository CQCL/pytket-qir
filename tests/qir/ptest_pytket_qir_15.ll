; ModuleID = 'ptest_pytket_qir_15'
source_filename = "ptest_pytket_qir_15"

%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  br i1 false, label %sb_1_0, label %sb_0_0

sb_0_0:                                           ; preds = %entry
  br label %entry_0

sb_1_0:                                           ; preds = %entry
  br label %entry_0

entry_0:                                          ; preds = %sb_0_0, %sb_1_0
  %0 = phi i64 [ 0, %sb_0_0 ], [ 1, %sb_1_0 ]
  br i1 false, label %sb_1_1, label %sb_0_1

sb_0_1:                                           ; preds = %entry_0
  %1 = and i64 9223372036854775805, %0
  br label %entry_1

sb_1_1:                                           ; preds = %entry_0
  %2 = or i64 2, %0
  br label %entry_1

entry_1:                                          ; preds = %sb_0_1, %sb_1_1
  %3 = phi i64 [ %1, %sb_0_1 ], [ %2, %sb_1_1 ]
  br i1 false, label %sb_1_2, label %sb_0_2

sb_0_2:                                           ; preds = %entry_1
  %4 = and i64 9223372036854775803, %3
  br label %entry_2

sb_1_2:                                           ; preds = %entry_1
  %5 = or i64 4, %3
  br label %entry_2

entry_2:                                          ; preds = %sb_0_2, %sb_1_2
  %6 = phi i64 [ %4, %sb_0_2 ], [ %5, %sb_1_2 ]
  br i1 false, label %sb_1_3, label %sb_0_3

sb_0_3:                                           ; preds = %entry_2
  %7 = and i64 9223372036854775799, %6
  br label %entry_3

sb_1_3:                                           ; preds = %entry_2
  %8 = or i64 8, %6
  br label %entry_3

entry_3:                                          ; preds = %sb_0_3, %sb_1_3
  %9 = phi i64 [ %7, %sb_0_3 ], [ %8, %sb_1_3 ]
  br i1 false, label %sb_1_4, label %sb_0_4

sb_0_4:                                           ; preds = %entry_3
  %10 = and i64 9223372036854775791, %9
  br label %entry_4

sb_1_4:                                           ; preds = %entry_3
  %11 = or i64 16, %9
  br label %entry_4

entry_4:                                          ; preds = %sb_0_4, %sb_1_4
  %12 = phi i64 [ %10, %sb_0_4 ], [ %11, %sb_1_4 ]
  br i1 true, label %sb_1_5, label %sb_0_5

sb_0_5:                                           ; preds = %entry_4
  %13 = and i64 9223372036854775775, %12
  br label %entry_5

sb_1_5:                                           ; preds = %entry_4
  %14 = or i64 32, %12
  br label %entry_5

entry_5:                                          ; preds = %sb_0_5, %sb_1_5
  %15 = phi i64 [ %13, %sb_0_5 ], [ %14, %sb_1_5 ]
  br i1 false, label %sb_1_6, label %sb_0_6

sb_0_6:                                           ; preds = %entry_5
  %16 = and i64 9223372036854775743, %15
  br label %entry_6

sb_1_6:                                           ; preds = %entry_5
  %17 = or i64 64, %15
  br label %entry_6

entry_6:                                          ; preds = %sb_0_6, %sb_1_6
  %18 = phi i64 [ %16, %sb_0_6 ], [ %17, %sb_1_6 ]
  br i1 false, label %sb_1_7, label %sb_0_7

sb_0_7:                                           ; preds = %entry_6
  %19 = and i64 9223372036854775679, %18
  br label %entry_7

sb_1_7:                                           ; preds = %entry_6
  %20 = or i64 128, %18
  br label %entry_7

entry_7:                                          ; preds = %sb_0_7, %sb_1_7
  %21 = phi i64 [ %19, %sb_0_7 ], [ %20, %sb_1_7 ]
  call void @__quantum__rt__int_record_output(i64 %21, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="0" "required_num_results"="0" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
