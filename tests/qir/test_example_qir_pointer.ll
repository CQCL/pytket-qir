; ModuleID = 'test_example_qir'
source_filename = "test_example_qir"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_reg(2)
  %1 = call i1* @create_reg(5)
  %2 = call i1* @create_reg(7)
  call void @set_one_bit_in_reg(i1* %2, i64 0, i1 true)
  call void @set_one_bit_in_reg(i1* %2, i64 1, i1 false)
  call void @set_one_bit_in_reg(i1* %2, i64 2, i1 false)
  call void @set_one_bit_in_reg(i1* %2, i64 3, i1 true)
  call void @set_one_bit_in_reg(i1* %2, i64 4, i1 true)
  call void @set_one_bit_in_reg(i1* %2, i64 5, i1 true)
  call void @set_one_bit_in_reg(i1* %2, i64 6, i1 true)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %3 = call i1 @__quantum__qis__read_result__body(%Result* null)
  call void @set_one_bit_in_reg(i1* %0, i64 0, i1 %3)
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %4 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  call void @set_one_bit_in_reg(i1* %0, i64 1, i1 %4)
  %5 = call i1 @read_bit_from_reg(i64 %0, i64 0)
  br i1 %5, label %then, label %else

then:                                             ; preds = %entry
  %6 = call i64 @read_all_bits_from_reg(i1* %2)
  %7 = call i64 @read_all_bits_from_reg(i1* %1)
  %8 = sub i64 %6, %7
  call void @set_all_bits_in_reg(i1* %2, i64 %8)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %9 = call i1 @read_bit_from_reg(i1* %0, i64 1)
  br i1 %9, label %then1, label %else2

then1:                                            ; preds = %continue
  %10 = call i64 @read_all_bits_from_reg(i1* %2)
  %11 = call i64 @read_all_bits_from_reg(i1* %0)
  %12 = sub i64 %10, %11
  call void @set_all_bits_in_reg(i1* %1, i64 %)
  br label %continue3

else2:                                            ; preds = %continue
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %13 = call i64 @read_all_bits_from_reg(i1* %2)
  %14 = call i64 @read_all_bits_from_reg(i1* %1)
  %15 = sub i64 %13, %14
  call void @set_all_bits_in_reg(i1* %0, i64 %15)
  %16 = call i64 @read_all_bits_from_reg(i1* %0)
  %17 = call i64 @read_all_bits_from_reg(i1* %1)
  %18 = call i64 @read_all_bits_from_reg(i1* %2)
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__int_record_output(i64 %16, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %17, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %18, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @read_bit_from_reg(i1*, i64)

declare void @set_one_bit_in_reg(i1*, i64, i1)

declare void @set_all_bits_in_reg(i1*, i64)

declare i64 @read_all_bits_from_reg(i1*)

declare i1* @create_reg(i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "num_required_qubits"="2" "num_required_results"="2" "output_labeling_schema" "qir_profiles"="custom" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
