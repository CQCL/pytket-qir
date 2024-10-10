; ModuleID = 'test_pytket_qir_conditional_7'
source_filename = "test_pytket_qir_conditional_7"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"syn\00"
@1 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  br i1 false, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  br i1 false, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  br i1 false, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  br i1 false, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  br i1 false, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  br i1 false, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @1, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="7" "required_num_results"="7" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
