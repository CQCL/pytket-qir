; ModuleID = 'test_pytket_qir_20'
source_filename = "test_pytket_qir_20"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 10)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 5 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 6 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 7 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 8 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 9 to %Qubit*))
  call void @mz_to_creg_bit(%Qubit* null, i1* %0, i64 0)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 1 to %Qubit*), i1* %0, i64 1)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 2 to %Qubit*), i1* %0, i64 2)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 3 to %Qubit*), i1* %0, i64 3)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 4 to %Qubit*), i1* %0, i64 4)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 5 to %Qubit*), i1* %0, i64 5)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 6 to %Qubit*), i1* %0, i64 6)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 7 to %Qubit*), i1* %0, i64 7)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 8 to %Qubit*), i1* %0, i64 8)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 9 to %Qubit*), i1* %0, i64 9)
  %1 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %1, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
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

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="10" "required_num_results"="10" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
