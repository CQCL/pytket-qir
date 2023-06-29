; ModuleID = 'test_pytket_qir_rangepredicate'
source_filename = "test_pytket_qir_rangepredicate"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %2 = icmp sgt i64 1, %0
  %3 = icmp sgt i64 %0, 1
  %4 = and i1 %2, %3
  call void @set_one_bit_in_reg(i64 %1, i64 0, i1 %4)
  %5 = icmp sgt i64 1, %0
  %6 = icmp sgt i64 %0, 1
  %7 = and i1 %5, %6
  call void @set_one_bit_in_reg(i64 %1, i64 1, i1 %7)
  %8 = icmp sgt i64 0, %0
  %9 = icmp sgt i64 %0, 0
  %10 = and i1 %8, %9
  call void @set_one_bit_in_reg(i64 %1, i64 2, i1 %10)
  %11 = icmp sgt i64 2, %0
  %12 = icmp sgt i64 %0, 4294967295
  %13 = and i1 %11, %12
  call void @set_one_bit_in_reg(i64 %1, i64 3, i1 %13)
  %14 = icmp sgt i64 0, %0
  %15 = icmp sgt i64 %0, 1
  %16 = and i1 %14, %15
  call void @set_one_bit_in_reg(i64 %1, i64 4, i1 %16)
  %17 = icmp sgt i64 1, %0
  %18 = icmp sgt i64 %0, 4294967295
  %19 = and i1 %17, %18
  call void @set_one_bit_in_reg(i64 %1, i64 5, i1 %19)
  %20 = call i1 @read_bit_from_reg(i64 %1, i64 0)
  br i1 %20, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %21 = call i1 @read_bit_from_reg(i64 %1, i64 1)
  br i1 %21, label %then1, label %else2

then1:                                            ; preds = %continue
  br label %continue3

else2:                                            ; preds = %continue
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %22 = call i1 @read_bit_from_reg(i64 %1, i64 2)
  br i1 %22, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %23 = call i1 @read_bit_from_reg(i64 %1, i64 3)
  br i1 %23, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %24 = call i1 @read_bit_from_reg(i64 %1, i64 4)
  br i1 %24, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %25 = call i1 @read_bit_from_reg(i64 %1, i64 5)
  br i1 %25, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
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

declare void @__quantum__qis__h__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="3" "num_required_results"="3" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}