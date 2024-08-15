; ModuleID = 'test_pytket_qir_wasm_iii_64'
source_filename = "test_pytket_qir_wasm_iii_64"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"
@1 = internal constant [3 x i8] c"c0\00"
@2 = internal constant [3 x i8] c"c1\00"

define void @main() #0 {
entry:
  %0 = call i64 @add_something(i64 0)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %1 = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %1, label %sb_1_0, label %sb_0_0

sb_0_0:                                           ; preds = %entry
  br label %entry_0

sb_1_0:                                           ; preds = %entry
  br label %entry_0

entry_0:                                          ; preds = %sb_0_0, %sb_1_0
  %2 = phi i64 [ 0, %sb_0_0 ], [ 1, %sb_1_0 ]
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %3 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  br i1 %3, label %sb_1_1, label %sb_0_1

sb_0_1:                                           ; preds = %entry_0
  %4 = and i64 9223372036854775805, %2
  br label %entry_1

sb_1_1:                                           ; preds = %entry_0
  %5 = or i64 2, %2
  br label %entry_1

entry_1:                                          ; preds = %sb_0_1, %sb_1_1
  %6 = phi i64 [ %4, %sb_0_1 ], [ %5, %sb_1_1 ]
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 2 to %Qubit*), %Result* inttoptr (i64 2 to %Result*))
  %7 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 2 to %Result*))
  br i1 %7, label %sb_1_2, label %sb_0_2

sb_0_2:                                           ; preds = %entry_1
  %8 = and i64 9223372036854775803, %6
  br label %entry_2

sb_1_2:                                           ; preds = %entry_1
  %9 = or i64 4, %6
  br label %entry_2

entry_2:                                          ; preds = %sb_0_2, %sb_1_2
  %10 = phi i64 [ %8, %sb_0_2 ], [ %9, %sb_1_2 ]
  %11 = call i64 @add_something(i64 %0)
  call void @__quantum__rt__int_record_output(i64 %10, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 0, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %11, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @2, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @init() #1

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
