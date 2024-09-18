; ModuleID = 'test_pytket_qir_conditional_13'
source_filename = "test_pytket_qir_conditional_13"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  br i1 true, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  br i1 false, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  call void @__quantum__rt__int_record_output(i64 1, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @0, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="7" "required_num_results"="7" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
