; ModuleID = 'test_pytket_qir_rangepredicate'
source_filename = "test_pytket_qir_rangepredicate"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 5)
  %1 = call i1* @create_creg(i64 6)
  %2 = call i64 @get_int_from_creg(i1* %0)
  %3 = icmp eq i64 1, %2
  call void @set_creg_bit(i1* %1, i64 0, i1 %3)
  %4 = call i64 @get_int_from_creg(i1* %0)
  %5 = icmp eq i64 1, %4
  call void @set_creg_bit(i1* %1, i64 1, i1 %5)
  %6 = call i64 @get_int_from_creg(i1* %0)
  %7 = icmp eq i64 0, %6
  call void @set_creg_bit(i1* %1, i64 2, i1 %7)
  %8 = call i64 @get_int_from_creg(i1* %0)
  %9 = icmp sgt i64 2, %8
  %10 = call i64 @get_int_from_creg(i1* %0)
  %11 = icmp sgt i64 %10, 4294967295
  %12 = and i1 %9, %11
  call void @set_creg_bit(i1* %1, i64 3, i1 %12)
  %13 = call i64 @get_int_from_creg(i1* %0)
  %14 = icmp sgt i64 0, %13
  %15 = call i64 @get_int_from_creg(i1* %0)
  %16 = icmp sgt i64 %15, 1
  %17 = and i1 %14, %16
  call void @set_creg_bit(i1* %1, i64 4, i1 %17)
  %18 = call i64 @get_int_from_creg(i1* %0)
  %19 = icmp sgt i64 1, %18
  %20 = call i64 @get_int_from_creg(i1* %0)
  %21 = icmp sgt i64 %20, 4294967295
  %22 = and i1 %19, %21
  call void @set_creg_bit(i1* %1, i64 5, i1 %22)
  %23 = call i1 @get_creg_bit(i1* %1, i64 0)
  br i1 %23, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %24 = call i1 @get_creg_bit(i1* %1, i64 1)
  br i1 %24, label %then1, label %else2

then1:                                            ; preds = %continue
  br label %continue3

else2:                                            ; preds = %continue
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %25 = call i1 @get_creg_bit(i1* %1, i64 2)
  br i1 %25, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %26 = call i1 @get_creg_bit(i1* %1, i64 3)
  br i1 %26, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %27 = call i1 @get_creg_bit(i1* %1, i64 4)
  br i1 %27, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %28 = call i1 @get_creg_bit(i1* %1, i64 5)
  br i1 %28, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  call void @__quantum__rt__tuple_start_record_output()
  %29 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %29, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %30 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %30, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
