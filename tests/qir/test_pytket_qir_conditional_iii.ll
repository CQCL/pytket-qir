; ModuleID = 'test_pytket_qir_conditional_iii'
source_filename = "test_pytket_qir_conditional_iii"

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
  %0 = call i1* @create_creg(i64 15)
  %1 = call i1* @create_creg(i64 15)
  %2 = call i1* @create_creg(i64 15)
  %3 = call i1* @create_creg(i64 15)
  %4 = call i1* @create_creg(i64 15)
  %5 = call i1* @create_creg(i64 1)
  call void @__quantum__qis__h__body(%Qubit* null)
  %6 = call i1 @get_creg_bit(i1* %2, i64 4)
  %7 = call i1 @get_creg_bit(i1* %2, i64 5)
  %8 = call i1 @get_creg_bit(i1* %2, i64 6)
  %9 = xor i1 %7, %8
  %10 = or i1 %6, %9
  %11 = call i1 @get_creg_bit(i1* %2, i64 7)
  %12 = call i1 @get_creg_bit(i1* %2, i64 8)
  %13 = and i1 %11, %12
  %14 = or i1 %10, %13
  call void @set_creg_bit(i1* %5, i64 0, i1 %14)
  %15 = call i64 @get_int_from_creg(i1* %0)
  %16 = call i64 @get_int_from_creg(i1* %1)
  %17 = add i64 %15, %16
  %18 = call i64 @get_int_from_creg(i1* %3)
  %19 = sub i64 %17, %18
  call void @set_creg_to_int(i1* %2, i64 %19)
  %20 = call i1 @get_creg_bit(i1* %5, i64 0)
  br i1 %20, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %21 = call i64 @get_int_from_creg(i1* %0)
  %22 = call i64 @get_int_from_creg(i1* %1)
  %23 = mul i64 %21, %22
  %24 = call i64 @get_int_from_creg(i1* %3)
  %25 = mul i64 %23, %24
  %26 = call i64 @get_int_from_creg(i1* %2)
  %27 = mul i64 %25, %26
  call void @set_creg_to_int(i1* %4, i64 %27)
  call void @__quantum__rt__tuple_start_record_output()
  %28 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %28, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %29 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %29, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %30 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %30, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %31 = call i64 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %31, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  %32 = call i64 @get_int_from_creg(i1* %4)
  call void @__quantum__rt__int_record_output(i64 %32, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @4, i32 0, i32 0))
  %33 = call i64 @get_int_from_creg(i1* %5)
  call void @__quantum__rt__int_record_output(i64 %33, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @5, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="1" "num_required_results"="1" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
