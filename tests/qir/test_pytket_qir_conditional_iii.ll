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
  %6 = call i64 @get_int_from_creg(i1* %0)
  %7 = call i64 @get_int_from_creg(i1* %0)
  %8 = call i1 @get_creg_bit(i1* %2, i64 4)
  %9 = call i1 @get_creg_bit(i1* %2, i64 5)
  %10 = call i1 @get_creg_bit(i1* %2, i64 6)
  %11 = xor i1 %9, %10
  %12 = or i1 %8, %11
  %13 = call i1 @get_creg_bit(i1* %2, i64 7)
  %14 = call i1 @get_creg_bit(i1* %2, i64 8)
  %15 = and i1 %13, %14
  %16 = or i1 %12, %15
  call void @set_creg_bit(i1* %5, i64 0, i1 %16)
  %17 = call i64 @get_int_from_creg(i1* %0)
  %18 = call i64 @get_int_from_creg(i1* %0)
  %19 = call i64 @get_int_from_creg(i1* %0)
  %20 = call i64 @get_int_from_creg(i1* %1)
  %21 = add i64 %19, %20
  %22 = call i64 @get_int_from_creg(i1* %3)
  %23 = sub i64 %21, %22
  call void @set_creg_to_int(i1* %2, i64 %23)
  %24 = call i1 @get_creg_bit(i1* %5, i64 0)
  br i1 %24, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %25 = call i64 @get_int_from_creg(i1* %0)
  %26 = call i64 @get_int_from_creg(i1* %0)
  %27 = call i64 @get_int_from_creg(i1* %0)
  %28 = call i64 @get_int_from_creg(i1* %1)
  %29 = mul i64 %27, %28
  %30 = call i64 @get_int_from_creg(i1* %3)
  %31 = mul i64 %29, %30
  %32 = call i64 @get_int_from_creg(i1* %2)
  %33 = mul i64 %31, %32
  call void @set_creg_to_int(i1* %4, i64 %33)
  call void @__quantum__rt__tuple_start_record_output()
  %34 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %34, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %35 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %35, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %36 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %36, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %37 = call i64 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %37, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  %38 = call i64 @get_int_from_creg(i1* %4)
  call void @__quantum__rt__int_record_output(i64 %38, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @4, i32 0, i32 0))
  %39 = call i64 @get_int_from_creg(i1* %5)
  call void @__quantum__rt__int_record_output(i64 %39, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @5, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg(%Qubit*, i1*, i64)

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
