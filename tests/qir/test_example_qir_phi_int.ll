; ModuleID = 'test_example_qir'
source_filename = "test_example_qir"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %1 = zext i1 %0 to i2 
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %2 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  %3 = zext i1 %2 to i2
  %4 = shl i2 %3, 1
  %5 = or i2 %1, %4 
  %6 = trunc i2 %5 to i1

  br i1 %6, label %then, label %continue

then:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %entry, %then
  %7 = and i2 2, %5
  %8 = lshr i2 %7, 1
  %9 = trunc i2 %8 to i1
  br i1 %9, label %then1, label %continue3

then1:                                            ; preds = %continue
  %10 = zext i2 %5 to i7
  %11 = sub i7 125, %10
  %12 = trunc i7 %11 to i5 
  br label %continue3

continue3:                                        ; preds = %continue, %then1
  %13 = phi i5 [%12, %then1], [0,%continue] ; b
  %14 = zext i5 %13 to i7
  %15 = sub i7 125, %14
  %16 = trunc i7 %15 to i2 
  %17 = zext i2 %16 to i64
  %18 = zext i5 %13 to i64 
  %19 = zext i7 125 to i64 
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__int_record_output(i64 %17, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %18, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %19, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

declare i1 @__quantum__qis__read_result__body(%Result*)

attributes #0 = { "entry_point" "num_required_qubits"="2" "num_required_results"="2" "output_labeling_schema" "qir_profiles"="custom" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
