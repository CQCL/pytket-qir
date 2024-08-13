; ModuleID = 'ptest_pytket_qir_15'
source_filename = "ptest_pytket_qir_15"

%Result = type opaque
%Qubit = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  %0 = call i64 @create_int(i64 8)
  %1 = call i64 @create_int(i64 1)
  %2 = call i64 @set_bit_in_int(i64 %0, i64 0, i1 false)
  %3 = call i64 @set_bit_in_int(i64 %2, i64 1, i1 false)
  %4 = call i64 @set_bit_in_int(i64 %3, i64 2, i1 false)
  %5 = call i64 @set_bit_in_int(i64 %4, i64 3, i1 false)
  %6 = call i64 @set_bit_in_int(i64 %5, i64 4, i1 false)
  %7 = call i64 @set_bit_in_int(i64 %6, i64 5, i1 true)
  %8 = call i64 @set_bit_in_int(i64 %7, i64 6, i1 false)
  %9 = call i64 @set_bit_in_int(i64 %8, i64 7, i1 false)
  call void @__quantum__rt__int_record_output(i64 %9, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %1, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  ret void
}

declare i1 @get_bit_from_int(i64, i64)

declare i64 @set_bit_in_int(i64, i64, i1)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @create_int(i64)

declare i64 @mz_to_int(%Qubit*, i64, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="0" "required_num_results"="0" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
