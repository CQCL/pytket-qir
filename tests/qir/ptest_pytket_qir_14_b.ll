; ModuleID = 'ptest_pytket_qir_14_b'
source_filename = "ptest_pytket_qir_14_b"

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
  %0 = call i1* @create_creg(i64 32)
  %1 = call i1* @create_creg(i64 32)
  %2 = call i1* @create_creg(i64 32)
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
  call void @set_creg_bit(i1* %1, i64 10, i1 false)
  call void @set_creg_bit(i1* %1, i64 11, i1 false)
  call void @set_creg_bit(i1* %1, i64 12, i1 false)
  call void @set_creg_bit(i1* %1, i64 13, i1 false)
  call void @set_creg_bit(i1* %1, i64 14, i1 false)
  call void @set_creg_bit(i1* %1, i64 15, i1 false)
  call void @set_creg_bit(i1* %1, i64 16, i1 false)
  call void @set_creg_bit(i1* %1, i64 17, i1 false)
  call void @set_creg_bit(i1* %1, i64 18, i1 false)
  call void @set_creg_bit(i1* %1, i64 19, i1 false)
  call void @set_creg_bit(i1* %1, i64 20, i1 false)
  call void @set_creg_bit(i1* %1, i64 21, i1 false)
  call void @set_creg_bit(i1* %1, i64 22, i1 false)
  call void @set_creg_bit(i1* %1, i64 23, i1 false)
  call void @set_creg_bit(i1* %1, i64 24, i1 false)
  call void @set_creg_bit(i1* %1, i64 25, i1 false)
  call void @set_creg_bit(i1* %1, i64 26, i1 false)
  call void @set_creg_bit(i1* %1, i64 27, i1 false)
  call void @set_creg_bit(i1* %1, i64 28, i1 false)
  call void @set_creg_bit(i1* %1, i64 29, i1 false)
  call void @set_creg_bit(i1* %1, i64 30, i1 false)
  call void @set_creg_bit(i1* %1, i64 31, i1 false)
  call void @set_creg_bit(i1* %0, i64 0, i1 false)
  call void @set_creg_bit(i1* %0, i64 1, i1 true)
  call void @set_creg_bit(i1* %0, i64 2, i1 false)
  call void @set_creg_bit(i1* %0, i64 3, i1 false)
  call void @set_creg_bit(i1* %0, i64 4, i1 false)
  call void @set_creg_bit(i1* %0, i64 5, i1 false)
  call void @set_creg_bit(i1* %0, i64 6, i1 false)
  call void @set_creg_bit(i1* %0, i64 7, i1 false)
  call void @set_creg_bit(i1* %0, i64 8, i1 false)
  call void @set_creg_bit(i1* %0, i64 9, i1 false)
  call void @set_creg_bit(i1* %0, i64 10, i1 false)
  call void @set_creg_bit(i1* %0, i64 11, i1 false)
  call void @set_creg_bit(i1* %0, i64 12, i1 false)
  call void @set_creg_bit(i1* %0, i64 13, i1 false)
  call void @set_creg_bit(i1* %0, i64 14, i1 false)
  call void @set_creg_bit(i1* %0, i64 15, i1 false)
  call void @set_creg_bit(i1* %0, i64 16, i1 false)
  call void @set_creg_bit(i1* %0, i64 17, i1 false)
  call void @set_creg_bit(i1* %0, i64 18, i1 false)
  call void @set_creg_bit(i1* %0, i64 19, i1 false)
  call void @set_creg_bit(i1* %0, i64 20, i1 false)
  call void @set_creg_bit(i1* %0, i64 21, i1 false)
  call void @set_creg_bit(i1* %0, i64 22, i1 false)
  call void @set_creg_bit(i1* %0, i64 23, i1 false)
  call void @set_creg_bit(i1* %0, i64 24, i1 false)
  call void @set_creg_bit(i1* %0, i64 25, i1 false)
  call void @set_creg_bit(i1* %0, i64 26, i1 false)
  call void @set_creg_bit(i1* %0, i64 27, i1 false)
  call void @set_creg_bit(i1* %0, i64 28, i1 false)
  call void @set_creg_bit(i1* %0, i64 29, i1 false)
  call void @set_creg_bit(i1* %0, i64 30, i1 false)
  call void @set_creg_bit(i1* %0, i64 31, i1 false)
  call void @set_creg_bit(i1* %0, i64 0, i1 true)
  call void @set_creg_bit(i1* %0, i64 1, i1 true)
  call void @set_creg_bit(i1* %0, i64 2, i1 true)
  call void @set_creg_bit(i1* %0, i64 3, i1 false)
  call void @set_creg_bit(i1* %0, i64 4, i1 true)
  call void @set_creg_bit(i1* %0, i64 5, i1 false)
  call void @set_creg_bit(i1* %0, i64 6, i1 false)
  call void @set_creg_bit(i1* %0, i64 7, i1 false)
  call void @set_creg_bit(i1* %0, i64 8, i1 false)
  call void @set_creg_bit(i1* %0, i64 9, i1 false)
  call void @set_creg_bit(i1* %0, i64 10, i1 false)
  call void @set_creg_bit(i1* %0, i64 11, i1 false)
  call void @set_creg_bit(i1* %0, i64 12, i1 false)
  call void @set_creg_bit(i1* %0, i64 13, i1 false)
  call void @set_creg_bit(i1* %0, i64 14, i1 false)
  call void @set_creg_bit(i1* %0, i64 15, i1 false)
  call void @set_creg_bit(i1* %0, i64 16, i1 false)
  call void @set_creg_bit(i1* %0, i64 17, i1 false)
  call void @set_creg_bit(i1* %0, i64 18, i1 false)
  call void @set_creg_bit(i1* %0, i64 19, i1 false)
  call void @set_creg_bit(i1* %0, i64 20, i1 false)
  call void @set_creg_bit(i1* %0, i64 21, i1 false)
  call void @set_creg_bit(i1* %0, i64 22, i1 false)
  call void @set_creg_bit(i1* %0, i64 23, i1 false)
  call void @set_creg_bit(i1* %0, i64 24, i1 false)
  call void @set_creg_bit(i1* %0, i64 25, i1 false)
  call void @set_creg_bit(i1* %0, i64 26, i1 false)
  call void @set_creg_bit(i1* %0, i64 27, i1 false)
  call void @set_creg_bit(i1* %0, i64 28, i1 false)
  call void @set_creg_bit(i1* %0, i64 29, i1 false)
  call void @set_creg_bit(i1* %0, i64 30, i1 false)
  call void @set_creg_bit(i1* %0, i64 31, i1 false)
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
  %15 = call i1 @get_creg_bit(i1* %0, i64 8)
  call void @set_creg_bit(i1* %1, i64 8, i1 %15)
  %16 = call i1 @get_creg_bit(i1* %0, i64 9)
  call void @set_creg_bit(i1* %1, i64 9, i1 %16)
  %17 = call i1 @get_creg_bit(i1* %0, i64 10)
  call void @set_creg_bit(i1* %1, i64 10, i1 %17)
  %18 = call i1 @get_creg_bit(i1* %0, i64 11)
  call void @set_creg_bit(i1* %1, i64 11, i1 %18)
  %19 = call i1 @get_creg_bit(i1* %0, i64 12)
  call void @set_creg_bit(i1* %1, i64 12, i1 %19)
  %20 = call i1 @get_creg_bit(i1* %0, i64 13)
  call void @set_creg_bit(i1* %1, i64 13, i1 %20)
  %21 = call i1 @get_creg_bit(i1* %0, i64 14)
  call void @set_creg_bit(i1* %1, i64 14, i1 %21)
  %22 = call i1 @get_creg_bit(i1* %0, i64 15)
  call void @set_creg_bit(i1* %1, i64 15, i1 %22)
  %23 = call i1 @get_creg_bit(i1* %0, i64 16)
  call void @set_creg_bit(i1* %1, i64 16, i1 %23)
  %24 = call i1 @get_creg_bit(i1* %0, i64 17)
  call void @set_creg_bit(i1* %1, i64 17, i1 %24)
  %25 = call i1 @get_creg_bit(i1* %0, i64 18)
  call void @set_creg_bit(i1* %1, i64 18, i1 %25)
  %26 = call i1 @get_creg_bit(i1* %0, i64 19)
  call void @set_creg_bit(i1* %1, i64 19, i1 %26)
  %27 = call i1 @get_creg_bit(i1* %0, i64 20)
  call void @set_creg_bit(i1* %1, i64 20, i1 %27)
  %28 = call i1 @get_creg_bit(i1* %0, i64 21)
  call void @set_creg_bit(i1* %1, i64 21, i1 %28)
  %29 = call i1 @get_creg_bit(i1* %0, i64 22)
  call void @set_creg_bit(i1* %1, i64 22, i1 %29)
  %30 = call i1 @get_creg_bit(i1* %0, i64 23)
  call void @set_creg_bit(i1* %1, i64 23, i1 %30)
  %31 = call i1 @get_creg_bit(i1* %0, i64 24)
  call void @set_creg_bit(i1* %1, i64 24, i1 %31)
  %32 = call i1 @get_creg_bit(i1* %0, i64 25)
  call void @set_creg_bit(i1* %1, i64 25, i1 %32)
  %33 = call i1 @get_creg_bit(i1* %0, i64 26)
  call void @set_creg_bit(i1* %1, i64 26, i1 %33)
  %34 = call i1 @get_creg_bit(i1* %0, i64 27)
  call void @set_creg_bit(i1* %1, i64 27, i1 %34)
  %35 = call i1 @get_creg_bit(i1* %0, i64 28)
  call void @set_creg_bit(i1* %1, i64 28, i1 %35)
  %36 = call i1 @get_creg_bit(i1* %0, i64 29)
  call void @set_creg_bit(i1* %1, i64 29, i1 %36)
  %37 = call i1 @get_creg_bit(i1* %0, i64 30)
  call void @set_creg_bit(i1* %1, i64 30, i1 %37)
  %38 = call i1 @get_creg_bit(i1* %0, i64 31)
  call void @set_creg_bit(i1* %1, i64 31, i1 %38)
  %39 = call i64 @get_int_from_creg(i1* %0)
  %40 = call i64 @get_int_from_creg(i1* %1)
  %41 = add i64 %39, %40
  call void @set_creg_to_int(i1* %2, i64 %41)
  %42 = call i64 @get_int_from_creg(i1* %0)
  %43 = call i64 @get_int_from_creg(i1* %1)
  %44 = sub i64 %42, %43
  call void @set_creg_to_int(i1* %2, i64 %44)
  %45 = call i64 @get_int_from_creg(i1* %0)
  %46 = shl i64 %45, 1
  call void @set_creg_to_int(i1* %0, i64 %46)
  %47 = call i64 @get_int_from_creg(i1* %0)
  %48 = lshr i64 %47, 1
  call void @set_creg_to_int(i1* %1, i64 %48)
  %49 = call i64 @get_int_from_creg(i1* %0)
  %50 = icmp eq i64 1, %49
  call void @set_creg_bit(i1* %3, i64 4, i1 %50)
  %51 = call i64 @get_int_from_creg(i1* %0)
  %52 = icmp sgt i64 2, %51
  %53 = call i64 @get_int_from_creg(i1* %0)
  %54 = icmp sgt i64 %53, -1
  %55 = and i1 %52, %54
  call void @set_creg_bit(i1* %3, i64 5, i1 %55)
  %56 = call i64 @get_int_from_creg(i1* %0)
  %57 = icmp eq i64 0, %56
  call void @set_creg_bit(i1* %3, i64 6, i1 %57)
  %58 = call i64 @get_int_from_creg(i1* %0)
  %59 = icmp sgt i64 1, %58
  %60 = call i64 @get_int_from_creg(i1* %0)
  %61 = icmp sgt i64 %60, -1
  %62 = and i1 %59, %61
  call void @set_creg_bit(i1* %3, i64 7, i1 %62)
  %63 = call i64 @get_int_from_creg(i1* %0)
  %64 = icmp sgt i64 0, %63
  %65 = call i64 @get_int_from_creg(i1* %0)
  %66 = icmp sgt i64 %65, 1
  %67 = and i1 %64, %66
  call void @set_creg_bit(i1* %3, i64 8, i1 %67)
  %68 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %68, label %then, label %else

then:                                             ; preds = %entry
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %69 = call i1 @get_creg_bit(i1* %0, i64 0)
  %70 = call i1 @get_creg_bit(i1* %1, i64 0)
  %71 = xor i1 %69, %70
  call void @set_creg_bit(i1* %3, i64 1, i1 %71)
  %72 = call i64 @get_int_from_creg(i1* %0)
  %73 = call i64 @get_int_from_creg(i1* %1)
  %74 = xor i64 %72, %73
  call void @set_creg_to_int(i1* %4, i64 %74)
  %75 = call i64 @get_int_from_creg(i1* %0)
  %76 = call i64 @get_int_from_creg(i1* %1)
  %77 = and i64 %75, %76
  call void @set_creg_to_int(i1* %5, i64 %77)
  %78 = call i64 @get_int_from_creg(i1* %0)
  %79 = call i64 @get_int_from_creg(i1* %1)
  %80 = or i64 %78, %79
  call void @set_creg_to_int(i1* %6, i64 %80)
  %81 = call i64 @get_int_from_creg(i1* %4)
  %82 = icmp eq i64 1, %81
  call void @set_creg_bit(i1* %3, i64 0, i1 %82)
  %83 = call i64 @get_int_from_creg(i1* %5)
  %84 = icmp eq i64 1, %83
  call void @set_creg_bit(i1* %3, i64 2, i1 %84)
  %85 = call i64 @get_int_from_creg(i1* %6)
  %86 = icmp eq i64 1, %85
  call void @set_creg_bit(i1* %3, i64 3, i1 %86)
  %87 = call i1 @get_creg_bit(i1* %3, i64 0)
  br i1 %87, label %then1, label %else2

then1:                                            ; preds = %continue
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue3

else2:                                            ; preds = %continue
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %88 = call i1 @get_creg_bit(i1* %3, i64 1)
  br i1 %88, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %89 = call i1 @get_creg_bit(i1* %3, i64 2)
  br i1 %89, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %90 = call i1 @get_creg_bit(i1* %3, i64 3)
  br i1 %90, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %91 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %91, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  %92 = call i1 @get_creg_bit(i1* %3, i64 4)
  br i1 %92, label %then16, label %else17

then16:                                           ; preds = %continue15
  br label %continue18

else17:                                           ; preds = %continue15
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue18

continue18:                                       ; preds = %else17, %then16
  %93 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %93, label %then19, label %else20

then19:                                           ; preds = %continue18
  br label %continue21

else20:                                           ; preds = %continue18
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue21

continue21:                                       ; preds = %else20, %then19
  %94 = call i1 @get_creg_bit(i1* %3, i64 5)
  br i1 %94, label %then22, label %else23

then22:                                           ; preds = %continue21
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue24

else23:                                           ; preds = %continue21
  br label %continue24

continue24:                                       ; preds = %else23, %then22
  %95 = call i1 @get_creg_bit(i1* %3, i64 6)
  br i1 %95, label %then25, label %else26

then25:                                           ; preds = %continue24
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue27

else26:                                           ; preds = %continue24
  br label %continue27

continue27:                                       ; preds = %else26, %then25
  %96 = call i1 @get_creg_bit(i1* %3, i64 7)
  br i1 %96, label %then28, label %else29

then28:                                           ; preds = %continue27
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue30

else29:                                           ; preds = %continue27
  br label %continue30

continue30:                                       ; preds = %else29, %then28
  %97 = call i1 @get_creg_bit(i1* %3, i64 8)
  br i1 %97, label %then31, label %else32

then31:                                           ; preds = %continue30
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue33

else32:                                           ; preds = %continue30
  br label %continue33

continue33:                                       ; preds = %else32, %then31
  call void @__quantum__rt__tuple_start_record_output()
  %98 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %98, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %99 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %99, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %100 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %100, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %101 = call i64 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %101, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @3, i32 0, i32 0))
  %102 = call i64 @get_int_from_creg(i1* %4)
  call void @__quantum__rt__int_record_output(i64 %102, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @4, i32 0, i32 0))
  %103 = call i64 @get_int_from_creg(i1* %5)
  call void @__quantum__rt__int_record_output(i64 %103, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @5, i32 0, i32 0))
  %104 = call i64 @get_int_from_creg(i1* %6)
  call void @__quantum__rt__int_record_output(i64 %104, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @6, i32 0, i32 0))
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
