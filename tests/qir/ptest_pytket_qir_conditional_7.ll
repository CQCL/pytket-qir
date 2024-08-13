; ModuleID = 'ptest_pytket_qir_conditional_7'
source_filename = "ptest_pytket_qir_conditional_7"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"syn\00"
@1 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  %0 = call i64 @create_int(i64 4)
  %1 = call i64 @create_int(i64 6)
  %2 = icmp eq i64 1, %0
  %3 = call i64 @set_bit_in_int(i64 %1, i64 0, i1 %2)
  %4 = icmp eq i64 2, %0
  %5 = call i64 @set_bit_in_int(i64 %3, i64 1, i1 %4)
  %6 = icmp eq i64 2, %0
  %7 = call i64 @set_bit_in_int(i64 %5, i64 2, i1 %6)
  %8 = icmp eq i64 3, %0
  %9 = call i64 @set_bit_in_int(i64 %7, i64 3, i1 %8)
  %10 = icmp eq i64 4, %0
  %11 = call i64 @set_bit_in_int(i64 %9, i64 4, i1 %10)
  %12 = icmp eq i64 4, %0
  %13 = call i64 @set_bit_in_int(i64 %11, i64 5, i1 %12)
  %14 = call i1 @get_bit_from_int(i64 %13, i64 0)
  br i1 %14, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %15 = call i1 @get_bit_from_int(i64 %13, i64 1)
  br i1 %15, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %16 = call i1 @get_bit_from_int(i64 %13, i64 2)
  br i1 %16, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %17 = call i1 @get_bit_from_int(i64 %13, i64 3)
  br i1 %17, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %18 = call i1 @get_bit_from_int(i64 %13, i64 4)
  br i1 %18, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %19 = call i1 @get_bit_from_int(i64 %13, i64 5)
  br i1 %19, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %13, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @1, i32 0, i32 0))
  ret void
}

declare i1 @get_bit_from_int(i64, i64)

declare i64 @set_bit_in_int(i64, i64, i1)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @create_int(i64)

declare i64 @mz_to_int(%Qubit*, i64, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="7" "required_num_results"="7" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
