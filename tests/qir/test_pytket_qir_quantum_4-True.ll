; ModuleID = 'test_pytket_qir_quantum_4'
source_filename = "test_pytket_qir_quantum_4"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__x__body(%Qubit* null)
  call void @__quantum__qis__y__body(%Qubit* null)
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__rx__body(double 0x3FF921FB54442D18, %Qubit* null)
  call void @__quantum__qis__rzz__body(double 0x3FF921FB54442D18, %Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__phasedx__body(double 0x3FF921FB54442D18, double 0x3FF41B2F769CF0E0, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__zzmax__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %0 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  %1 = zext i1 %0 to i64
  %2 = mul i64 %1, 2
  %3 = or i64 %2, 0
  %4 = sub i64 1, %1
  %5 = mul i64 %4, 2
  %6 = xor i64 9223372036854775807, %5
  %7 = and i64 %6, %3
  call void @__quantum__rt__int_record_output(i64 %7, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__x__body(%Qubit*)

declare void @__quantum__qis__y__body(%Qubit*)

declare void @__quantum__qis__z__body(%Qubit*)

declare void @__quantum__qis__rx__body(double, %Qubit*)

declare void @__quantum__qis__rzz__body(double, %Qubit*, %Qubit*)

declare void @__quantum__qis__phasedx__body(double, double, %Qubit*)

declare void @__quantum__qis__zzmax__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="4" "required_num_results"="4" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
