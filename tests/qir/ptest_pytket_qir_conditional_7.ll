; ModuleID = 'ptest_pytket_qir_conditional_7'
source_filename = "ptest_pytket_qir_conditional_7"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"syn\00"
@1 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

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
  br i1 false, label %sb_1_5, label %sb_0_5

sb_0_5:                                           ; preds = %entry_4
  %13 = and i64 9223372036854775775, %12
  br label %entry_5

sb_1_5:                                           ; preds = %entry_4
  %14 = or i64 32, %12
  br label %entry_5

entry_5:                                          ; preds = %sb_0_5, %sb_1_5
  %15 = phi i64 [ %13, %sb_0_5 ], [ %14, %sb_1_5 ]
  %16 = and i64 1, %15
  %17 = icmp eq i64 1, %16
  br i1 %17, label %condb0, label %contb0

condb0:                                           ; preds = %entry_5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry_5
  %18 = and i64 2, %15
  %19 = icmp eq i64 2, %18
  br i1 %19, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %20 = and i64 4, %15
  %21 = icmp eq i64 4, %20
  br i1 %21, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %22 = and i64 8, %15
  %23 = icmp eq i64 8, %22
  br i1 %23, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %24 = and i64 16, %15
  %25 = icmp eq i64 16, %24
  br i1 %25, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %26 = and i64 32, %15
  %27 = icmp eq i64 32, %26
  br i1 %27, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %15, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @1, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="7" "required_num_results"="7" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
