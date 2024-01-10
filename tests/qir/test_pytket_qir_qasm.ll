; ModuleID = 'test_pytket_qir_qasm'
source_filename = "test_pytket_qir_qasm"

%Result = type opaque
%Qubit = type opaque

@0 = internal constant [2 x i8] c"p\00"
@1 = internal constant [2 x i8] c"s\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 1)
  %1 = call i1* @create_creg(i64 3)
  %2 = call i64 @get_int_from_creg(i1* %1)
  %3 = icmp eq i64 2, %2
  br i1 %3, label %then, label %else

then:                                             ; preds = %entry
  %4 = call i1 @get_creg_bit(i1* %0, i64 0)
  %5 = xor i1 %4, true
  call void @set_creg_bit(i1* %0, i64 0, i1 %5)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
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

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="10" "required_num_results"="10" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
