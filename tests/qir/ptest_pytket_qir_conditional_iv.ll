; ModuleID = 'ptest_pytket_qir_conditional_iv'
source_filename = "ptest_pytket_qir_conditional_iv"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  %0 = call i64 @create_int(i64 2)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  %1 = call i64 @mz_to_int(%Qubit* null, i64 %0, i64 0)
  %2 = call i64 @mz_to_int(%Qubit* inttoptr (i64 1 to %Qubit*), i64 %1, i64 1)
  %3 = icmp eq i64 3, %2
  br i1 %3, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  call void @__quantum__rt__int_record_output(i64 %2, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  ret void
}

declare i1 @get_bit_from_int(i64, i64)

declare i64 @set_bit_in_int(i64, i64, i1)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @create_int(i64)

declare i64 @mz_to_int(%Qubit*, i64, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="2" "required_num_results"="2" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
