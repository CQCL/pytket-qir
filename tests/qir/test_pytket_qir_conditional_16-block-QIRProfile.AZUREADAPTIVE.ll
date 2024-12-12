; ModuleID = 'test_pytket_qir_conditional_16-block'
source_filename = "test_pytket_qir_conditional_16-block"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %1 = zext i1 %0 to i64
  %2 = mul i64 %1, 1
  %3 = or i64 %2, 0
  %4 = sub i64 1, %1
  %5 = mul i64 %4, 1
  %6 = xor i64 9223372036854775807, %5
  %7 = and i64 %6, %3
  %8 = and i64 1, %7
  %9 = icmp eq i64 1, %8
  br i1 %9, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %10 = phi i64 [ 3, %condb0 ], [ 0, %entry ]
  %11 = and i64 1, %7
  %12 = icmp eq i64 1, %11
  br i1 %12, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  %13 = or i64 1, %10
  %14 = and i64 9223372036854775807, %13
  %15 = or i64 2, %14
  %16 = and i64 9223372036854775807, %15
  %17 = or i64 0, %16
  %18 = and i64 9223372036854775803, %17
  %19 = or i64 0, %18
  %20 = and i64 9223372036854775799, %19
  %21 = or i64 0, %20
  %22 = and i64 9223372036854775791, %21
  %23 = or i64 0, %22
  %24 = and i64 9223372036854775775, %23
  %25 = or i64 0, %24
  %26 = and i64 9223372036854775743, %25
  %27 = or i64 0, %26
  %28 = and i64 9223372036854775679, %27
  %29 = or i64 0, %28
  %30 = and i64 9223372036854775551, %29
  %31 = or i64 0, %30
  %32 = and i64 9223372036854775295, %31
  %33 = or i64 0, %32
  %34 = and i64 9223372036854774783, %33
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %35 = phi i64 [ %34, %condb1 ], [ %10, %contb0 ]
  %36 = and i64 1, %7
  %37 = icmp eq i64 1, %36
  br i1 %37, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  %38 = add i64 %7, %35
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %39 = phi i64 [ %38, %condb2 ], [ 0, %contb1 ]
  call void @__quantum__rt__array_record_output(i64 3, i8* null)
  call void @__quantum__rt__int_record_output(i64 %7, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %35, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %39, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__array_record_output(i64, i8*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3, !4, !5, !6, !7, !8, !9, !10}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
!4 = !{i32 1, !"classical_ints", i1 true}
!5 = !{i32 1, !"qubit_resetting", i1 true}
!6 = !{i32 1, !"classical_floats", i1 false}
!7 = !{i32 1, !"backwards_branching", i1 false}
!8 = !{i32 1, !"classical_fixed_points", i1 false}
!9 = !{i32 1, !"user_functions", i1 false}
!10 = !{i32 1, !"multiple_target_branching", i1 false}
