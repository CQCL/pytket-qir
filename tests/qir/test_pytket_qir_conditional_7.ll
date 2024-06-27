; ModuleID = 'test_pytket_qir_conditional_7'
source_filename = "test_pytket_qir_conditional_7"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"syn\00"
@1 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i32 4)
  %1 = call i1* @create_creg(i32 6)
  %2 = call i32 @get_int_from_creg(i1* %0)
  %3 = icmp eq i32 1, %2
  call void @set_creg_bit(i1* %1, i32 0, i1 %3)
  %4 = call i32 @get_int_from_creg(i1* %0)
  %5 = icmp eq i32 2, %4
  call void @set_creg_bit(i1* %1, i32 1, i1 %5)
  %6 = call i32 @get_int_from_creg(i1* %0)
  %7 = icmp eq i32 2, %6
  call void @set_creg_bit(i1* %1, i32 2, i1 %7)
  %8 = call i32 @get_int_from_creg(i1* %0)
  %9 = icmp eq i32 3, %8
  call void @set_creg_bit(i1* %1, i32 3, i1 %9)
  %10 = call i32 @get_int_from_creg(i1* %0)
  %11 = icmp eq i32 4, %10
  call void @set_creg_bit(i1* %1, i32 4, i1 %11)
  %12 = call i32 @get_int_from_creg(i1* %0)
  %13 = icmp eq i32 4, %12
  call void @set_creg_bit(i1* %1, i32 5, i1 %13)
  %14 = call i1 @get_creg_bit(i1* %1, i32 0)
  br i1 %14, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %15 = call i1 @get_creg_bit(i1* %1, i32 1)
  br i1 %15, label %then1, label %else2

then1:                                            ; preds = %continue
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue3

else2:                                            ; preds = %continue
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %16 = call i1 @get_creg_bit(i1* %1, i32 2)
  br i1 %16, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %17 = call i1 @get_creg_bit(i1* %1, i32 3)
  br i1 %17, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %18 = call i1 @get_creg_bit(i1* %1, i32 4)
  br i1 %18, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %19 = call i1 @get_creg_bit(i1* %1, i32 5)
  br i1 %19, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  call void @__quantum__rt__tuple_start_record_output()
  %20 = call i32 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i32 %20, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @0, i32 0, i32 0))
  %21 = call i32 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i32 %21, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i32)

declare void @set_creg_bit(i1*, i32, i1)

declare void @set_creg_to_int(i1*, i32)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i32)

declare i32 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i32)

declare void @__quantum__rt__int_record_output(i32, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="7" "required_num_results"="7" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
