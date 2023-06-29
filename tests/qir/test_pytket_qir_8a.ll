; ModuleID = 'test_pytket_qir_8a'
source_filename = "test_pytket_qir_8a"

%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 0, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 1, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 2, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 7, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 0, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 1, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 2, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 3, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 4, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 5, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 6, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 7, i1 false)
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

attributes #0 = { "entry_point" "num_required_qubits"="1" "num_required_results"="1" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
