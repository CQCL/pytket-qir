; ModuleID = 'test_pytket_qir_15'
source_filename = "test_pytket_qir_15"

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
  br i1 %68, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
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
  br i1 %87, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %88 = call i1 @get_creg_bit(i1* %3, i64 1)
  br i1 %88, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %89 = call i1 @get_creg_bit(i1* %3, i64 2)
  br i1 %89, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %90 = call i1 @get_creg_bit(i1* %3, i64 3)
  br i1 %90, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %91 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %91, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %92 = call i1 @get_creg_bit(i1* %3, i64 4)
  br i1 %92, label %contb6, label %condb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %93 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %93, label %contb7, label %condb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %94 = call i1 @get_creg_bit(i1* %3, i64 5)
  br i1 %94, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %95 = call i1 @get_creg_bit(i1* %3, i64 6)
  br i1 %95, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %96 = call i1 @get_creg_bit(i1* %3, i64 7)
  br i1 %96, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %97 = call i1 @get_creg_bit(i1* %3, i64 8)
  br i1 %97, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
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
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i64)

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
