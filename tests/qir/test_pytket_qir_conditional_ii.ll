; ModuleID = 'test_pytket_qir_conditional_ii'
source_filename = "test_pytket_qir_conditional_ii"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"
@3 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 5)
  %1 = call i1* @create_creg(i64 5)
  %2 = call i1* @create_creg(i64 5)
  %3 = call i1* @create_creg(i64 5)
  %4 = call i64 @get_int_from_creg(i1* %0)
  %5 = call i64 @get_int_from_creg(i1* %1)
  %6 = or i64 %4, %5
  call void @set_creg_to_int(i1* %2, i64 %6)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  %7 = call i64 @get_int_from_creg(i1* %2)
  %8 = call i64 @get_int_from_creg(i1* %1)
  %9 = or i64 %7, %8
  call void @set_creg_to_int(i1* %3, i64 %9)
  call void @__quantum__qis__h__body(%Qubit* null)
  %10 = call i1 @get_creg_bit(i1* %0, i64 4)
  br i1 %10, label %contb0, label %condb0

condb0:                                           ; preds = %entry
  %11 = call i64 @get_int_from_creg(i1* %2)
  %12 = call i64 @get_int_from_creg(i1* %1)
  %13 = or i64 %11, %12
  call void @set_creg_to_int(i1* %3, i64 %13)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 2 to %Qubit*), i1* %3, i64 2)
  call void @mz_to_creg_bit(%Qubit* inttoptr (i64 1 to %Qubit*), i1* %3, i64 3)
  call void @mz_to_creg_bit(%Qubit* null, i1* %3, i64 4)
  call void @__quantum__rt__tuple_start_record_output()
  %14 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %14, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %15 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %15, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %16 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %16, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %17 = call i64 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %17, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
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

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="3" "required_num_results"="3" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
