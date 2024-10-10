; ModuleID = 'test_pytket_qir_12'
source_filename = "test_pytket_qir_12"

%Result = type opaque
%Qubit = type opaque

@0 = internal constant [2 x i8] c"a\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 8)
  %1 = call i64 @get_int_from_creg(i1* %0)
  %2 = shl i64 %1, 1
  call void @set_creg_to_int(i1* %0, i64 %2)
  %3 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %3, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i64)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}