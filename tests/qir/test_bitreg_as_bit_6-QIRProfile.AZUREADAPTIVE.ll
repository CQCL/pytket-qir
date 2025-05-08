; ModuleID = 'test_bitreg_as_bit_6'
source_filename = "test_bitreg_as_bit_6"

%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"

define void @main() #0 {
entry:
  call void @__quantum__rt__array_record_output(i64 2, i8* null)
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__array_record_output(i64, i8*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="0" "required_num_results"="0" }

!llvm.module.flags = !{!0, !1, !2, !3, !4, !5, !6, !7, !8, !9, !10}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
!4 = !{i32 1, !"classical_ints", i1 true}
!5 = !{i32 1, !"qubit_resetting", i1 true}
!6 = !{i32 1, !"classical_floats", i1 false}
!7 = !{i32 1, !"backwards_branching", i1 false}
!8 = !{i32 1, !"classical_fixed_points", i1 false}
!9 = !{i32 1, !"user_functions", i1 false}
!10 = !{i32 1, !"multiple_target_branching", i1 false}
