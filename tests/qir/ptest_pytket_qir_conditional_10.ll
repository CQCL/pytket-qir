; ModuleID = 'ptest_pytket_qir_conditional_10'
source_filename = "ptest_pytket_qir_conditional_10"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 4)
  %1 = call i1* @create_creg(i64 5)
  %2 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %2, label %condb0, label %continueb0

condb0:                                           ; preds = %entry
  %3 = call i64 @get_int_from_creg(i1* %1)
  %4 = call i64 @get_int_from_creg(i1* %1)
  %5 = or i64 %3, %4
  call void @set_creg_to_int(i1* %1, i64 %5)
  call void @__quantum__qis__x__body(%Qubit* null)
  call void @__quantum__qis__z__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__y__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continueb0

continueb0:                                       ; preds = %condb0, %entry
  call void @__quantum__rt__tuple_start_record_output()
  %6 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %6, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %7 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %7, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__x__body(%Qubit*)

declare void @__quantum__qis__z__body(%Qubit*)

declare void @__quantum__qis__y__body(%Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="4" "required_num_results"="4" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
