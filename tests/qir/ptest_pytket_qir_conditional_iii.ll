; ModuleID = 'ptest_pytket_qir_conditional_iii'
source_filename = "ptest_pytket_qir_conditional_iii"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"
@3 = internal constant [2 x i8] c"d\00"
@4 = internal constant [2 x i8] c"e\00"
@5 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  %0 = call i64 @create_int(i64 15)
  %1 = call i64 @create_int(i64 15)
  %2 = call i64 @create_int(i64 15)
  %3 = call i64 @create_int(i64 15)
  %4 = call i64 @create_int(i64 15)
  %5 = call i64 @create_int(i64 1)
  call void @__quantum__qis__h__body(%Qubit* null)
  %6 = call i1 @get_bit_from_int(i64 %2, i64 4)
  %7 = call i1 @get_bit_from_int(i64 %2, i64 5)
  %8 = call i1 @get_bit_from_int(i64 %2, i64 6)
  %9 = xor i1 %7, %8
  %10 = or i1 %6, %9
  %11 = call i1 @get_bit_from_int(i64 %2, i64 7)
  %12 = call i1 @get_bit_from_int(i64 %2, i64 8)
  %13 = and i1 %11, %12
  %14 = or i1 %10, %13
  %15 = call i64 @set_bit_in_int(i64 %5, i64 0, i1 %14)
  %16 = add i64 %0, %1
  %17 = sub i64 %16, %3
  %18 = call i1 @get_bit_from_int(i64 %15, i64 0)
  br i1 %18, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %19 = mul i64 %0, %1
  %20 = mul i64 %19, %3
  %21 = mul i64 %20, %17
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %1, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %17, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %3, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %21, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @4, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %15, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @5, i32 0, i32 0))
  ret void
}

declare i1 @get_bit_from_int(i64, i64)

declare i64 @set_bit_in_int(i64, i64, i1)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @create_int(i64)

declare i64 @mz_to_int(%Qubit*, i64, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
