; ModuleID = 'test_example_qir'
source_filename = "test_example_qir"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  %0 = call i64 @set_one_bit_in_int(i64 0, i64 0, i1 true)
  %1 = call i64 @set_one_bit_in_int(i64 0, i64 0, i1 true)
  %1 = call i64 @set_one_bit_in_int(i64 %0, i64 1, i1 false)
  %2 = call i64 @set_one_bit_in_int(i64 %1, i64 2, i1 false)
  %3 = call i64 @set_one_bit_in_int(i64 %2, i64 3, i1 true)
  %4 = call i64 @set_one_bit_in_int(i64 %3, i64 4, i1 true)
  %5 = call i64 @set_one_bit_in_int(i64 %4 i64 5, i1 true)
  %6 = call i64 @set_one_bit_in_int(i64 %5, i64 6, i1 true) # reg c
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %7 = call i1 @__quantum__qis__read_result__body(%Result* null) # 
  %8 = call i64 @set_one_bit_in_int(i64 0, i64 0, i1 %7) # reg a
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %9 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  %10 = call i64 @set_one_bit_in_int(i64 %8, i64 1, i1 %4) # reg a
  %11 = call i1 @read_bit_from_int(i64 %10, i64 0)
  br i1 %11, label %then, label %continue

then:                                             ; preds = %entry
  %12 = sub i64 %6, %10 # reg c 
  br label %continue

continue:                                         ; preds = %entry, %then
  %13 = phi i64 [%12, %then], [%6, %entry] # reg c
  %14 = call i1 @read_bit_from_int(i64 %10, i64 1)
  br i1 %14, label %then1, label %continue3

then1:                                            ; preds = %continue
  %15 = sub i64 %2, %0 # reg b
  br label %continue3

continue3:                                        ; preds = %continue, %then1
  %16 = phi i64 [%15, %then1], [0] # reg b
  %17 = sub i64 %13, %10 # reg a
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__int_record_output(i64 %17, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %16, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %13, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @read_bit_from_int(i64, i64)

declare i64 @set_one_bit_in_int(i64, i64, i1)

declare i64 @set_all_bits_in_reg(i64, i64)

declare i64 @resize_int(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

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
