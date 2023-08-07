; ModuleID = 'test_pytket_qir_17'
source_filename = "test_pytket_qir_17"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [3 x i8] c"c1\00"
@1 = internal constant [3 x i8] c"c2\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_reg(i64 1)
  %1 = call i1* @create_reg(i64 1)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %2 = call i1 @__quantum__qis__read_result__body(%Result* null)
  call void @set_one_bit_in_reg(i1* %0, i64 0, i1 %2)
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %3 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  call void @set_one_bit_in_reg(i1* %1, i64 0, i1 %3)
  call void @__quantum__rt__tuple_start_record_output()
  %4 = call i64 @read_all_bits_from_reg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %4, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @0, i32 0, i32 0))
  %5 = call i64 @read_all_bits_from_reg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %5, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @1, i32 0, i32 0))
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

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "num_required_qubits"="2" "num_required_results"="2" "output_labeling_schema" "qir_profiles"="custom" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
