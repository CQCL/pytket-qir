; ModuleID = 'test_pytket_qir_14'
source_filename = "test_pytket_qir_14"

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
  %0 = call i1* @create_creg(i64 8)
  %1 = call i1* @create_creg(i64 10)
  %2 = call i1* @create_creg(i64 10)
  %3 = call i1* @create_creg(i64 9)
  %4 = call i1* @create_creg(i64 64)
  %5 = call i1* @create_creg(i64 64)
  %6 = call i1* @create_creg(i64 64)
  call void @set_creg_bit(i1* %0, i64 0, i1 true)
  call void @set_creg_bit(i1* %1, i64 0, i1 true)
  call void @set_creg_bit(i1* %1, i64 1, i1 true)
  call void @set_creg_bit(i1* %1, i64 2, i1 false)
  call void @set_creg_bit(i1* %1, i64 3, i1 false)
  call void @set_creg_bit(i1* %1, i64 4, i1 false)
  call void @set_creg_bit(i1* %1, i64 5, i1 false)
  call void @set_creg_bit(i1* %1, i64 6, i1 false)
  call void @set_creg_bit(i1* %1, i64 7, i1 false)
  call void @set_creg_bit(i1* %1, i64 8, i1 false)
  call void @set_creg_bit(i1* %1, i64 9, i1 false)
  call void @set_creg_bit(i1* %0, i64 0, i1 false)
  call void @set_creg_bit(i1* %0, i64 1, i1 true)
  call void @set_creg_bit(i1* %0, i64 2, i1 false)
  call void @set_creg_bit(i1* %0, i64 3, i1 false)
  call void @set_creg_bit(i1* %0, i64 4, i1 false)
  call void @set_creg_bit(i1* %0, i64 5, i1 false)
  call void @set_creg_bit(i1* %0, i64 6, i1 false)
  call void @set_creg_bit(i1* %0, i64 7, i1 false)
  call void @set_creg_bit(i1* %0, i64 0, i1 true)
  call void @set_creg_bit(i1* %0, i64 1, i1 true)
  call void @set_creg_bit(i1* %0, i64 2, i1 true)
  call void @set_creg_bit(i1* %0, i64 3, i1 false)
  call void @set_creg_bit(i1* %0, i64 4, i1 true)
  call void @set_creg_bit(i1* %0, i64 5, i1 false)
  call void @set_creg_bit(i1* %0, i64 6, i1 false)
  call void @set_creg_bit(i1* %0, i64 7, i1 false)
  %7 = call i1 @get_creg_bit(i1* %0, i64 0)
  call void @set_creg_bit(i1* %1, i64 0, i1 %7)
  %8 = call i1 @get_creg_bit(i1* %0, i64 1)
  call void @set_creg_bit(i1* %1, i64 1, i1 %8)
  %9 = call i1 @get_creg_bit(i1* %0, i64 2)
  call void @set_creg_bit(i1* %1, i64 2, i1 %9)
  %10 = call i1 @get_creg_bit(i1* %0, i64 3)
  call void @set_creg_bit(i1* %1, i64 3, i1 %10)
  %11 = call i1 @get_creg_bit(i1* %0, i64 4)
  call void @set_creg_bit(i1* %1, i64 4, i1 %11)
  %12 = call i1 @get_creg_bit(i1* %0, i64 5)
  call void @set_creg_bit(i1* %1, i64 5, i1 %12)
  %13 = call i1 @get_creg_bit(i1* %0, i64 6)
  call void @set_creg_bit(i1* %1, i64 6, i1 %13)
  %14 = call i1 @get_creg_bit(i1* %0, i64 7)
  call void @set_creg_bit(i1* %1, i64 7, i1 %14)
  %15 = call i64 @get_int_from_creg(i1* %0)
  %16 = call i64 @get_int_from_creg(i1* %1)
  %17 = add i64 %15, %16
  call void @set_creg_to_int(i1* %2, i64 %17)
  %18 = call i64 @get_int_from_creg(i1* %0)
  %19 = call i64 @get_int_from_creg(i1* %1)
  %20 = sub i64 %18, %19
  call void @set_creg_to_int(i1* %2, i64 %20)
  %21 = call i64 @get_int_from_creg(i1* %0)
  %22 = shl i64 %21, 1
  call void @set_creg_to_int(i1* %0, i64 %22)
  %23 = call i64 @get_int_from_creg(i1* %0)
  %24 = lshr i64 %23, 1
  call void @set_creg_to_int(i1* %1, i64 %24)
  %25 = call i64 @get_int_from_creg(i1* %0)
  %26 = icmp eq i64 1, %25
  call void @set_creg_bit(i1* %3, i64 4, i1 %26)
  %27 = call i64 @get_int_from_creg(i1* %0)
  %28 = icmp sgt i64 2, %27
  %29 = call i64 @get_int_from_creg(i1* %0)
  %30 = icmp sgt i64 %29, -1
  %31 = and i1 %28, %30
  call void @set_creg_bit(i1* %3, i64 5, i1 %31)
  %32 = call i64 @get_int_from_creg(i1* %0)
  %33 = icmp eq i64 0, %32
  call void @set_creg_bit(i1* %3, i64 6, i1 %33)
  %34 = call i64 @get_int_from_creg(i1* %0)
  %35 = icmp sgt i64 1, %34
  %36 = call i64 @get_int_from_creg(i1* %0)
  %37 = icmp sgt i64 %36, -1
  %38 = and i1 %35, %37
  call void @set_creg_bit(i1* %3, i64 7, i1 %38)
  %39 = call i64 @get_int_from_creg(i1* %0)
  %40 = icmp sgt i64 0, %39
  %41 = call i64 @get_int_from_creg(i1* %0)
  %42 = icmp sgt i64 %41, 1
  %43 = and i1 %40, %42
  call void @set_creg_bit(i1* %3, i64 8, i1 %43)
  %44 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %44, label %then, label %else

then:                                             ; preds = %entry
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %45 = call i1 @get_creg_bit(i1* %0, i64 0)
  %46 = call i1 @get_creg_bit(i1* %1, i64 0)
  %47 = xor i1 %45, %46
  call void @set_creg_bit(i1* %3, i64 1, i1 %47)
  %48 = call i64 @get_int_from_creg(i1* %0)
  %49 = call i64 @get_int_from_creg(i1* %1)
  %50 = xor i64 %48, %49
  call void @set_creg_to_int(i1* %4, i64 %50)
  %51 = call i64 @get_int_from_creg(i1* %0)
  %52 = call i64 @get_int_from_creg(i1* %1)
  %53 = and i64 %51, %52
  call void @set_creg_to_int(i1* %5, i64 %53)
  %54 = call i64 @get_int_from_creg(i1* %0)
  %55 = call i64 @get_int_from_creg(i1* %1)
  %56 = or i64 %54, %55
  call void @set_creg_to_int(i1* %6, i64 %56)
  %57 = call i64 @get_int_from_creg(i1* %4)
  %58 = icmp eq i64 1, %57
  call void @set_creg_bit(i1* %3, i64 0, i1 %58)
  %59 = call i64 @get_int_from_creg(i1* %5)
  %60 = icmp eq i64 1, %59
  call void @set_creg_bit(i1* %3, i64 2, i1 %60)
  %61 = call i64 @get_int_from_creg(i1* %6)
  %62 = icmp eq i64 1, %61
  call void @set_creg_bit(i1* %3, i64 3, i1 %62)
  %63 = call i1 @get_creg_bit(i1* %3, i64 0)
  br i1 %63, label %then1, label %else2

then1:                                            ; preds = %continue
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue3

else2:                                            ; preds = %continue
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %64 = call i1 @get_creg_bit(i1* %3, i64 1)
  br i1 %64, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %65 = call i1 @get_creg_bit(i1* %3, i64 2)
  br i1 %65, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %66 = call i1 @get_creg_bit(i1* %3, i64 3)
  br i1 %66, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %67 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %67, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  %68 = call i1 @get_creg_bit(i1* %3, i64 4)
  br i1 %68, label %then16, label %else17

then16:                                           ; preds = %continue15
  br label %continue18

else17:                                           ; preds = %continue15
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue18

continue18:                                       ; preds = %else17, %then16
  %69 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %69, label %then19, label %else20

then19:                                           ; preds = %continue18
  br label %continue21

else20:                                           ; preds = %continue18
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue21

continue21:                                       ; preds = %else20, %then19
  %70 = call i1 @get_creg_bit(i1* %3, i64 5)
  br i1 %70, label %then22, label %else23

then22:                                           ; preds = %continue21
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue24

else23:                                           ; preds = %continue21
  br label %continue24

continue24:                                       ; preds = %else23, %then22
  %71 = call i1 @get_creg_bit(i1* %3, i64 6)
  br i1 %71, label %then25, label %else26

then25:                                           ; preds = %continue24
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue27

else26:                                           ; preds = %continue24
  br label %continue27

continue27:                                       ; preds = %else26, %then25
  %72 = call i1 @get_creg_bit(i1* %3, i64 7)
  br i1 %72, label %then28, label %else29

then28:                                           ; preds = %continue27
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue30

else29:                                           ; preds = %continue27
  br label %continue30

continue30:                                       ; preds = %else29, %then28
  %73 = call i1 @get_creg_bit(i1* %3, i64 8)
  br i1 %73, label %then31, label %else32

then31:                                           ; preds = %continue30
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue33

else32:                                           ; preds = %continue30
  br label %continue33

continue33:                                       ; preds = %else32, %then31
  call void @__quantum__rt__tuple_start_record_output()
  %74 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %74, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %75 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %75, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %76 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %76, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %77 = call i64 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %77, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @3, i32 0, i32 0))
  %78 = call i64 @get_int_from_creg(i1* %4)
  call void @__quantum__rt__int_record_output(i64 %78, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @4, i32 0, i32 0))
  %79 = call i64 @get_int_from_creg(i1* %5)
  call void @__quantum__rt__int_record_output(i64 %79, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @5, i32 0, i32 0))
  %80 = call i64 @get_int_from_creg(i1* %6)
  call void @__quantum__rt__int_record_output(i64 %80, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @6, i32 0, i32 0))
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

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
