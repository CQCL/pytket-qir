; ModuleID = 'ptest_pytket_qir_8'
source_filename = "ptest_pytket_qir_8"

%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"

define void @main() #0 {
entry:
  br i1 true, label %sb_1_0, label %sb_0_0

sb_0_0:                                           ; preds = %entry
  br label %entry_0

sb_1_0:                                           ; preds = %entry
  br label %entry_0

entry_0:                                          ; preds = %sb_0_0, %sb_1_0
  %0 = phi i64 [ 0, %sb_0_0 ], [ 1, %sb_1_0 ]
  br i1 true, label %sb_1_1, label %sb_0_1

sb_0_1:                                           ; preds = %entry_0
  %1 = and i64 9223372036854775805, %0
  br label %entry_1

sb_1_1:                                           ; preds = %entry_0
  %2 = or i64 2, %0
  br label %entry_1

entry_1:                                          ; preds = %sb_0_1, %sb_1_1
  %3 = phi i64 [ %1, %sb_0_1 ], [ %2, %sb_1_1 ]
  br i1 true, label %sb_1_2, label %sb_0_2

sb_0_2:                                           ; preds = %entry_1
  %4 = and i64 9223372036854775803, %3
  br label %entry_2

sb_1_2:                                           ; preds = %entry_1
  %5 = or i64 4, %3
  br label %entry_2

entry_2:                                          ; preds = %sb_0_2, %sb_1_2
  %6 = phi i64 [ %4, %sb_0_2 ], [ %5, %sb_1_2 ]
  br i1 true, label %sb_1_3, label %sb_0_3

sb_0_3:                                           ; preds = %entry_2
  %7 = and i64 9223372036854775679, %6
  br label %entry_3

sb_1_3:                                           ; preds = %entry_2
  %8 = or i64 128, %6
  br label %entry_3

entry_3:                                          ; preds = %sb_0_3, %sb_1_3
  %9 = phi i64 [ %7, %sb_0_3 ], [ %8, %sb_1_3 ]
  br i1 false, label %sb_1_4, label %sb_0_4

sb_0_4:                                           ; preds = %entry_3
  %10 = and i64 9223372036854775806, %9
  br label %entry_4

sb_1_4:                                           ; preds = %entry_3
  %11 = or i64 1, %9
  br label %entry_4

entry_4:                                          ; preds = %sb_0_4, %sb_1_4
  %12 = phi i64 [ %10, %sb_0_4 ], [ %11, %sb_1_4 ]
  br i1 true, label %sb_1_5, label %sb_0_5

sb_0_5:                                           ; preds = %entry_4
  %13 = and i64 9223372036854775805, %12
  br label %entry_5

sb_1_5:                                           ; preds = %entry_4
  %14 = or i64 2, %12
  br label %entry_5

entry_5:                                          ; preds = %sb_0_5, %sb_1_5
  %15 = phi i64 [ %13, %sb_0_5 ], [ %14, %sb_1_5 ]
  br i1 false, label %sb_1_6, label %sb_0_6

sb_0_6:                                           ; preds = %entry_5
  %16 = and i64 9223372036854775803, %15
  br label %entry_6

sb_1_6:                                           ; preds = %entry_5
  %17 = or i64 4, %15
  br label %entry_6

entry_6:                                          ; preds = %sb_0_6, %sb_1_6
  %18 = phi i64 [ %16, %sb_0_6 ], [ %17, %sb_1_6 ]
  br i1 false, label %sb_1_7, label %sb_0_7

sb_0_7:                                           ; preds = %entry_6
  %19 = and i64 9223372036854775799, %18
  br label %entry_7

sb_1_7:                                           ; preds = %entry_6
  %20 = or i64 8, %18
  br label %entry_7

entry_7:                                          ; preds = %sb_0_7, %sb_1_7
  %21 = phi i64 [ %19, %sb_0_7 ], [ %20, %sb_1_7 ]
  br i1 false, label %sb_1_8, label %sb_0_8

sb_0_8:                                           ; preds = %entry_7
  %22 = and i64 9223372036854775791, %21
  br label %entry_8

sb_1_8:                                           ; preds = %entry_7
  %23 = or i64 16, %21
  br label %entry_8

entry_8:                                          ; preds = %sb_0_8, %sb_1_8
  %24 = phi i64 [ %22, %sb_0_8 ], [ %23, %sb_1_8 ]
  br i1 false, label %sb_1_9, label %sb_0_9

sb_0_9:                                           ; preds = %entry_8
  %25 = and i64 9223372036854775775, %24
  br label %entry_9

sb_1_9:                                           ; preds = %entry_8
  %26 = or i64 32, %24
  br label %entry_9

entry_9:                                          ; preds = %sb_0_9, %sb_1_9
  %27 = phi i64 [ %25, %sb_0_9 ], [ %26, %sb_1_9 ]
  br i1 false, label %sb_1_10, label %sb_0_10

sb_0_10:                                          ; preds = %entry_9
  %28 = and i64 9223372036854775743, %27
  br label %entry_10

sb_1_10:                                          ; preds = %entry_9
  %29 = or i64 64, %27
  br label %entry_10

entry_10:                                         ; preds = %sb_0_10, %sb_1_10
  %30 = phi i64 [ %28, %sb_0_10 ], [ %29, %sb_1_10 ]
  br i1 false, label %sb_1_11, label %sb_0_11

sb_0_11:                                          ; preds = %entry_10
  %31 = and i64 9223372036854775679, %30
  br label %entry_11

sb_1_11:                                          ; preds = %entry_10
  %32 = or i64 128, %30
  br label %entry_11

entry_11:                                         ; preds = %sb_0_11, %sb_1_11
  %33 = phi i64 [ %31, %sb_0_11 ], [ %32, %sb_1_11 ]
  call void @__quantum__rt__int_record_output(i64 %33, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
