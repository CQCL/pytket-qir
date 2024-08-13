; ModuleID = 'ptest_pytket_qir_11'
source_filename = "ptest_pytket_qir_11"

%Result = type opaque
%Qubit = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"

define void @main() #0 {
entry:
  %0 = call i64 @create_int(i64 2)
  %1 = call i64 @create_int(i64 4)
  %2 = call i1 @get_bit_from_int(i64 %0, i64 0)
  %3 = call i64 @set_bit_in_int(i64 %1, i64 0, i1 %2)
  %4 = call i1 @get_bit_from_int(i64 %0, i64 1)
  %5 = call i64 @set_bit_in_int(i64 %3, i64 1, i1 %4)
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %5, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  ret void
}

declare i1 @get_bit_from_int(i64, i64)

declare i64 @set_bit_in_int(i64, i64, i1)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @create_int(i64)

declare i64 @mz_to_int(%Qubit*, i64, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
