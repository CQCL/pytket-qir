; ModuleID = 'test_pytket_qir_8'
source_filename = "test_pytket_qir_8"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"d\00"
@3 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"
@4 = internal constant [20 x i8] c"tk_SCRATCH_BITREG_0\00"
@5 = internal constant [20 x i8] c"tk_SCRATCH_BITREG_1\00"
@6 = internal constant [20 x i8] c"tk_SCRATCH_BITREG_2\00"

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %2 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %3 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %4 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %5 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %6 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 0, i1 true)
  call void @set_one_bit_in_reg(i64 %1, i64 0, i1 true)
  call void @set_one_bit_in_reg(i64 %1, i64 1, i1 true)
  call void @set_one_bit_in_reg(i64 %1, i64 2, i1 false)
  call void @set_one_bit_in_reg(i64 %1, i64 3, i1 false)
  call void @set_one_bit_in_reg(i64 %1, i64 4, i1 false)
  call void @set_one_bit_in_reg(i64 %1, i64 5, i1 false)
  call void @set_one_bit_in_reg(i64 %1, i64 6, i1 false)
  call void @set_one_bit_in_reg(i64 %1, i64 7, i1 false)
  call void @set_one_bit_in_reg(i64 %1, i64 8, i1 false)
  call void @set_one_bit_in_reg(i64 %1, i64 9, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 0, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 1, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 2, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 3, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 4, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 5, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 6, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 7, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 0, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 1, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 2, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 3, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 4, i1 true)
  call void @set_one_bit_in_reg(i64 %0, i64 5, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 6, i1 false)
  call void @set_one_bit_in_reg(i64 %0, i64 7, i1 false)
  %7 = call i1 @read_bit_from_reg(i64 %0, i64 0)
  call void @set_one_bit_in_reg(i64 %1, i64 0, i1 %7)
  %8 = call i1 @read_bit_from_reg(i64 %0, i64 1)
  call void @set_one_bit_in_reg(i64 %1, i64 1, i1 %8)
  %9 = call i1 @read_bit_from_reg(i64 %0, i64 2)
  call void @set_one_bit_in_reg(i64 %1, i64 2, i1 %9)
  %10 = call i1 @read_bit_from_reg(i64 %0, i64 3)
  call void @set_one_bit_in_reg(i64 %1, i64 3, i1 %10)
  %11 = call i1 @read_bit_from_reg(i64 %0, i64 4)
  call void @set_one_bit_in_reg(i64 %1, i64 4, i1 %11)
  %12 = call i1 @read_bit_from_reg(i64 %0, i64 5)
  call void @set_one_bit_in_reg(i64 %1, i64 5, i1 %12)
  %13 = call i1 @read_bit_from_reg(i64 %0, i64 6)
  call void @set_one_bit_in_reg(i64 %1, i64 6, i1 %13)
  %14 = call i1 @read_bit_from_reg(i64 %0, i64 7)
  call void @set_one_bit_in_reg(i64 %1, i64 7, i1 %14)
  %15 = add i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %15)
  %16 = sub i64 %0, %1
  call void @set_all_bits_in_reg(i64 %2, i64 %16)
  %17 = shl i64 %0, 1
  call void @set_all_bits_in_reg(i64 %0, i64 %17)
  %18 = lshr i64 %0, 1
  call void @set_all_bits_in_reg(i64 %1, i64 %18)
  %19 = icmp sgt i64 1, %0
  %20 = icmp sgt i64 %0, 1
  %21 = and i1 %19, %20
  call void @set_one_bit_in_reg(i64 %3, i64 4, i1 %21)
  %22 = icmp sgt i64 2, %0
  %23 = icmp sgt i64 %0, 4294967295
  %24 = and i1 %22, %23
  call void @set_one_bit_in_reg(i64 %3, i64 5, i1 %24)
  %25 = icmp sgt i64 0, %0
  %26 = icmp sgt i64 %0, 0
  %27 = and i1 %25, %26
  call void @set_one_bit_in_reg(i64 %3, i64 6, i1 %27)
  %28 = icmp sgt i64 1, %0
  %29 = icmp sgt i64 %0, 4294967295
  %30 = and i1 %28, %29
  call void @set_one_bit_in_reg(i64 %3, i64 7, i1 %30)
  %31 = icmp sgt i64 0, %0
  %32 = icmp sgt i64 %0, 1
  %33 = and i1 %31, %32
  call void @set_one_bit_in_reg(i64 %3, i64 8, i1 %33)
  %34 = call i1 @read_bit_from_reg(i64 %0, i64 0)
  br i1 %34, label %then, label %else

then:                                             ; preds = %entry
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %35 = call i1 @read_bit_from_reg(i64 %0, i64 0)
  %36 = call i1 @read_bit_from_reg(i64 %1, i64 0)
  %37 = xor i1 %35, %36
  call void @set_one_bit_in_reg(i64 %3, i64 1, i1 %37)
  %38 = xor i64 %0, %1
  call void @set_all_bits_in_reg(i64 %4, i64 %38)
  %39 = and i64 %0, %1
  call void @set_all_bits_in_reg(i64 %5, i64 %39)
  %40 = or i64 %0, %1
  call void @set_all_bits_in_reg(i64 %6, i64 %40)
  %41 = icmp sgt i64 1, %4
  %42 = icmp sgt i64 %4, 1
  %43 = and i1 %41, %42
  call void @set_one_bit_in_reg(i64 %3, i64 0, i1 %43)
  %44 = icmp sgt i64 1, %5
  %45 = icmp sgt i64 %5, 1
  %46 = and i1 %44, %45
  call void @set_one_bit_in_reg(i64 %3, i64 2, i1 %46)
  %47 = icmp sgt i64 1, %6
  %48 = icmp sgt i64 %6, 1
  %49 = and i1 %47, %48
  call void @set_one_bit_in_reg(i64 %3, i64 3, i1 %49)
  %50 = call i1 @read_bit_from_reg(i64 %3, i64 0)
  br i1 %50, label %then1, label %else2

then1:                                            ; preds = %continue
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue3

else2:                                            ; preds = %continue
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %51 = call i1 @read_bit_from_reg(i64 %3, i64 1)
  br i1 %51, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %52 = call i1 @read_bit_from_reg(i64 %3, i64 2)
  br i1 %52, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %53 = call i1 @read_bit_from_reg(i64 %3, i64 3)
  br i1 %53, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %54 = call i1 @read_bit_from_reg(i64 %0, i64 0)
  br i1 %54, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  %55 = call i1 @read_bit_from_reg(i64 %3, i64 4)
  br i1 %55, label %then16, label %else17

then16:                                           ; preds = %continue15
  br label %continue18

else17:                                           ; preds = %continue15
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue18

continue18:                                       ; preds = %else17, %then16
  %56 = call i1 @read_bit_from_reg(i64 %0, i64 0)
  br i1 %56, label %then19, label %else20

then19:                                           ; preds = %continue18
  br label %continue21

else20:                                           ; preds = %continue18
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue21

continue21:                                       ; preds = %else20, %then19
  %57 = call i1 @read_bit_from_reg(i64 %3, i64 5)
  br i1 %57, label %then22, label %else23

then22:                                           ; preds = %continue21
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue24

else23:                                           ; preds = %continue21
  br label %continue24

continue24:                                       ; preds = %else23, %then22
  %58 = call i1 @read_bit_from_reg(i64 %3, i64 6)
  br i1 %58, label %then25, label %else26

then25:                                           ; preds = %continue24
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue27

else26:                                           ; preds = %continue24
  br label %continue27

continue27:                                       ; preds = %else26, %then25
  %59 = call i1 @read_bit_from_reg(i64 %3, i64 7)
  br i1 %59, label %then28, label %else29

then28:                                           ; preds = %continue27
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue30

else29:                                           ; preds = %continue27
  br label %continue30

continue30:                                       ; preds = %else29, %then28
  %60 = call i1 @read_bit_from_reg(i64 %3, i64 8)
  br i1 %60, label %then31, label %else32

then31:                                           ; preds = %continue30
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue33

else32:                                           ; preds = %continue30
  br label %continue33

continue33:                                       ; preds = %else32, %then31
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %1, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %2, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %3, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %4, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @4, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %5, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @5, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %6, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @6, i32 0, i32 0))
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

attributes #0 = { "entry_point" "num_required_qubits"="1" "num_required_results"="1" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
