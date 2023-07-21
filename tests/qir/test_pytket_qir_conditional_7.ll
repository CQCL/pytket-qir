; ModuleID = 'test_pytket_qir_conditional_7'
source_filename = "test_pytket_qir_conditional_7"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"syn\00"
@1 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %2 = icmp eq i64 1, %0
  call void @set_one_bit_in_reg(i64 %1, i64 0, i1 %2)
  %3 = icmp eq i64 2, %0
  call void @set_one_bit_in_reg(i64 %1, i64 1, i1 %3)
  %4 = icmp eq i64 2, %0
  call void @set_one_bit_in_reg(i64 %1, i64 2, i1 %4)
  %5 = icmp eq i64 3, %0
  call void @set_one_bit_in_reg(i64 %1, i64 3, i1 %5)
  %6 = icmp eq i64 4, %0
  call void @set_one_bit_in_reg(i64 %1, i64 4, i1 %6)
  %7 = icmp eq i64 4, %0
  call void @set_one_bit_in_reg(i64 %1, i64 5, i1 %7)
  %8 = call i1 @read_bit_from_reg(i64 %1, i64 0)
  br i1 %8, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %9 = call i1 @read_bit_from_reg(i64 %1, i64 1)
  br i1 %9, label %then1, label %else2

then1:                                            ; preds = %continue
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue3

else2:                                            ; preds = %continue
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %10 = call i1 @read_bit_from_reg(i64 %1, i64 2)
  br i1 %10, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %11 = call i1 @read_bit_from_reg(i64 %1, i64 3)
  br i1 %11, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %12 = call i1 @read_bit_from_reg(i64 %1, i64 4)
  br i1 %12, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %13 = call i1 @read_bit_from_reg(i64 %1, i64 5)
  br i1 %13, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %1, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="7" "num_required_results"="7" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
