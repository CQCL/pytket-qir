; ModuleID = 'test_pytket_qir_wasm_4-QIRProfile.PYTKET'
source_filename = "test_pytket_qir_wasm_4-QIRProfile.PYTKET"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"
@1 = internal constant [3 x i8] c"c0\00"
@2 = internal constant [3 x i8] c"c1\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 6)
  %1 = call i1* @create_creg(i64 3)
  %2 = call i1* @create_creg(i64 4)
  %3 = call i64 @get_int_from_creg(i1* %1)
  %4 = call i64 @add_something(i64 %3)
  call void @set_creg_to_int(i1* %2, i64 %4)
  call void @mz_to_creg_bit(%Qubit* null, i1* %0, i64 0)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 1 to %Qubit*), i1* %0, i64 1)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 2 to %Qubit*), i1* %0, i64 2)
  %5 = call i64 @get_int_from_creg(i1* %2)
  %6 = call i64 @add_something(i64 %5)
  call void @set_creg_to_int(i1* %2, i64 %6)
  %7 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %7, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %8 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %8, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @1, i32 0, i32 0))
  %9 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %9, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @2, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @init() #1

declare i64 @add_something(i64) #1

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i64)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="6" "required_num_results"="6" }

attributes #1 = { "wasm" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
