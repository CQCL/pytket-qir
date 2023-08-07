; ModuleID = 'test_pytket_qir_11'
source_filename = "test_pytket_qir_11"

%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_reg(i64 2)
  %1 = call i1* @create_reg(i64 4)
  %2 = call i1 @read_bit_from_reg(i1* %0, i64 0)
  call void @set_one_bit_in_reg(i1* %1, i64 0, i1 %2)
  %3 = call i1 @read_bit_from_reg(i1* %0, i64 1)
  call void @set_one_bit_in_reg(i1* %1, i64 1, i1 %3)
  call void @__quantum__rt__tuple_start_record_output()
  %4 = call i64 @read_all_bits_from_reg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %4, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %5 = call i64 @read_all_bits_from_reg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %5, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
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

attributes #0 = { "entry_point" "num_required_qubits"="1" "num_required_results"="1" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
