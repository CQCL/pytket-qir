; ModuleID = 'test_pytket_qir_conditional'
source_filename = "test_pytket_qir_conditional"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"
@3 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* null)
  br i1 false, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %0 = phi i64 [ 0, %condb0 ], [ 0, %entry ]
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 2 to %Qubit*), %Result* inttoptr (i64 2 to %Result*))
  %1 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 2 to %Result*))
  %2 = zext i1 %1 to i64
  %3 = mul i64 %2, 4
  %4 = or i64 %3, %0
  %5 = sub i64 1, %2
  %6 = mul i64 %5, 4
  %7 = xor i64 9223372036854775807, %6
  %8 = and i64 %7, %4
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %9 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  %10 = zext i1 %9 to i64
  %11 = mul i64 %10, 8
  %12 = or i64 %11, %8
  %13 = sub i64 1, %10
  %14 = mul i64 %13, 8
  %15 = xor i64 9223372036854775807, %14
  %16 = and i64 %15, %12
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %17 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %18 = zext i1 %17 to i64
  %19 = mul i64 %18, 16
  %20 = or i64 %19, %16
  %21 = sub i64 1, %18
  %22 = mul i64 %21, 16
  %23 = xor i64 9223372036854775807, %22
  %24 = and i64 %23, %20
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %24, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="3" "required_num_results"="3" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
