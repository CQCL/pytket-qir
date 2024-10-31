; ModuleID = 'test_pytket_qir_wasm_4-QIRProfile.ADAPTIVE_CREGSIZE'
source_filename = "test_pytket_qir_wasm_4-QIRProfile.ADAPTIVE_CREGSIZE"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"
@1 = internal constant [3 x i8] c"c0\00"
@2 = internal constant [3 x i8] c"c1\00"

define void @main() #0 {
entry:
  %0 = call i64 @add_something(i64 0)
  %1 = trunc i64 %0 to i4
  %2 = zext i4 %1 to i64
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %3 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %4 = zext i1 %3 to i64
  %5 = mul i64 %4, 1
  %6 = or i64 %5, 0
  %7 = sub i64 1, %4
  %8 = mul i64 %7, 1
  %9 = xor i64 9223372036854775807, %8
  %10 = and i64 %9, %6
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %11 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  %12 = zext i1 %11 to i64
  %13 = mul i64 %12, 2
  %14 = or i64 %13, %10
  %15 = sub i64 1, %12
  %16 = mul i64 %15, 2
  %17 = xor i64 9223372036854775807, %16
  %18 = and i64 %17, %14
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 2 to %Qubit*), %Result* inttoptr (i64 2 to %Result*))
  %19 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 2 to %Result*))
  %20 = zext i1 %19 to i64
  %21 = mul i64 %20, 4
  %22 = or i64 %21, %18
  %23 = sub i64 1, %20
  %24 = mul i64 %23, 4
  %25 = xor i64 9223372036854775807, %24
  %26 = and i64 %25, %22
  %27 = call i64 @add_something(i64 %2)
  %28 = trunc i64 %27 to i4
  %29 = zext i4 %28 to i64
  call void @__quantum__rt__int_record_output(i64 %26, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %29, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @2, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare i64 @add_something(i64) #1

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #2

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="6" "required_num_results"="6" }
attributes #1 = { "wasm" }
attributes #2 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
