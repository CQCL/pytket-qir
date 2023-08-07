; ModuleID = 'test_pytket_qir_conditional'
source_filename = "test_pytket_qir_conditional"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"
@3 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_reg(i64 5)
  %1 = call i1* @create_reg(i64 5)
  %2 = call i1* @create_reg(i64 5)
  %3 = call i1* @create_reg(i64 5)
  %4 = call i64 @read_all_bits_from_reg(i1* %0)
  %5 = call i64 @read_all_bits_from_reg(i1* %0)
  %6 = call i64 @read_all_bits_from_reg(i1* %0)
  %7 = call i64 @read_all_bits_from_reg(i1* %1)
  %8 = or i64 %6, %7
  call void @set_all_bits_in_reg(i1* %2, i64 %8)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  %9 = call i64 @read_all_bits_from_reg(i1* %0)
  %10 = call i64 @read_all_bits_from_reg(i1* %0)
  %11 = call i64 @read_all_bits_from_reg(i1* %2)
  %12 = call i64 @read_all_bits_from_reg(i1* %1)
  %13 = or i64 %11, %12
  call void @set_all_bits_in_reg(i1* %3, i64 %13)
  call void @__quantum__qis__h__body(%Qubit* null)
  %14 = call i1 @read_bit_from_reg(i1* %0, i64 4)
  br i1 %14, label %then, label %else

then:                                             ; preds = %entry
  %15 = call i64 @read_all_bits_from_reg(i1* %0)
  %16 = call i64 @read_all_bits_from_reg(i1* %0)
  %17 = call i64 @read_all_bits_from_reg(i1* %2)
  %18 = call i64 @read_all_bits_from_reg(i1* %1)
  %19 = or i64 %17, %18
  call void @set_all_bits_in_reg(i1* %3, i64 %19)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 2 to %Qubit*), %Result* inttoptr (i64 2 to %Result*))
  %20 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 2 to %Result*))
  call void @set_one_bit_in_reg(i1* %3, i64 2, i1 %20)
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %21 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  call void @set_one_bit_in_reg(i1* %3, i64 3, i1 %21)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %22 = call i1 @__quantum__qis__read_result__body(%Result* null)
  call void @set_one_bit_in_reg(i1* %3, i64 4, i1 %22)
  call void @__quantum__rt__tuple_start_record_output()
  %23 = call i64 @read_all_bits_from_reg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %23, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %24 = call i64 @read_all_bits_from_reg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %24, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %25 = call i64 @read_all_bits_from_reg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %25, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %26 = call i64 @read_all_bits_from_reg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %26, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @read_bit_from_reg(i1*, i64)

declare void @set_one_bit_in_reg(i1*, i64, i1)

declare void @set_all_bits_in_reg(i1*, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_reg(i64)

declare i64 @read_all_bits_from_reg(i1*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
