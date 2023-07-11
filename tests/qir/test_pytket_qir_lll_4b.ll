; ModuleID = 'test_pytket_qir_ll_4'
source_filename = "test_pytket_qir_ll_4"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  %".3" = call i64 @"__something__"(i64 0)
  %".4" = call i64 @"__something__"(i64 0)
  br i64 %".4", label %"entry.if", label %"entry.else"
entry.if:
  %".6" = call i64 @"__something__"(i64 0)
  br label %"entry.endif"
entry.else:
  %".8" = call i64 @"__something__"(i64 0)
  br label %"entry.endif"
entry.endif:
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__int_record_output(i64 0, i8* c)
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

@"__something__" = external global i64 (i64)
@__quantum__rt__tuple_start_record_output = external global void ()
@__quantum__rt__int_record_output = external global void (i64, i8*)
@"__quantum__rt__tuple_end_record_output" = external global void ()

attributes #0 = { "entry_point" "num_required_qubits"="1" "num_required_results"="1" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
