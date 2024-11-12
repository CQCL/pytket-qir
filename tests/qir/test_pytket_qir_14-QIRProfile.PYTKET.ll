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
  %4 = call i1* @create_creg(i64 8)
  %5 = call i1* @create_creg(i64 8)
  %6 = call i1* @create_creg(i64 8)
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
  %26 = call i64 @get_int_from_creg(i1* %1)
  %27 = xor i64 %25, %26
  call void @set_creg_to_int(i1* %4, i64 %27)
  %28 = call i1 @get_creg_bit(i1* %0, i64 0)
  %29 = call i1 @get_creg_bit(i1* %1, i64 0)
  %30 = xor i1 %28, %29
  call void @set_creg_bit(i1* %3, i64 1, i1 %30)
  %31 = call i64 @get_int_from_creg(i1* %4)
  %32 = icmp eq i64 1, %31
  call void @set_creg_bit(i1* %3, i64 0, i1 %32)
  %33 = call i64 @get_int_from_creg(i1* %0)
  %34 = call i64 @get_int_from_creg(i1* %1)
  %35 = and i64 %33, %34
  call void @set_creg_to_int(i1* %5, i64 %35)
  %36 = call i1 @get_creg_bit(i1* %3, i64 0)
  br i1 %36, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %37 = call i64 @get_int_from_creg(i1* %0)
  %38 = call i64 @get_int_from_creg(i1* %1)
  %39 = or i64 %37, %38
  call void @set_creg_to_int(i1* %6, i64 %39)
  %40 = call i1 @get_creg_bit(i1* %3, i64 1)
  br i1 %40, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %41 = call i64 @get_int_from_creg(i1* %5)
  %42 = icmp eq i64 1, %41
  call void @set_creg_bit(i1* %3, i64 2, i1 %42)
  %43 = call i1 @get_creg_bit(i1* %3, i64 2)
  br i1 %43, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %44 = call i64 @get_int_from_creg(i1* %6)
  %45 = icmp eq i64 1, %44
  call void @set_creg_bit(i1* %3, i64 3, i1 %45)
  %46 = call i64 @get_int_from_creg(i1* %0)
  %47 = icmp eq i64 1, %46
  call void @set_creg_bit(i1* %3, i64 4, i1 %47)
  %48 = call i64 @get_int_from_creg(i1* %0)
  %49 = icmp sgt i64 2, %48
  %50 = call i64 @get_int_from_creg(i1* %0)
  %51 = icmp sgt i64 %50, -1
  %52 = and i1 %49, %51
  call void @set_creg_bit(i1* %3, i64 5, i1 %52)
  %53 = call i64 @get_int_from_creg(i1* %0)
  %54 = icmp eq i64 0, %53
  call void @set_creg_bit(i1* %3, i64 6, i1 %54)
  %55 = call i64 @get_int_from_creg(i1* %0)
  %56 = icmp sgt i64 1, %55
  %57 = call i64 @get_int_from_creg(i1* %0)
  %58 = icmp sgt i64 %57, -1
  %59 = and i1 %56, %58
  call void @set_creg_bit(i1* %3, i64 7, i1 %59)
  %60 = call i64 @get_int_from_creg(i1* %0)
  %61 = icmp sgt i64 0, %60
  %62 = call i64 @get_int_from_creg(i1* %0)
  %63 = icmp sgt i64 %62, 1
  %64 = and i1 %61, %63
  call void @set_creg_bit(i1* %3, i64 8, i1 %64)
  %65 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %65, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %66 = call i1 @get_creg_bit(i1* %3, i64 3)
  br i1 %66, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %67 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %67, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %68 = call i1 @get_creg_bit(i1* %3, i64 4)
  br i1 %68, label %contb6, label %condb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %69 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %69, label %contb7, label %condb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %70 = call i1 @get_creg_bit(i1* %3, i64 5)
  br i1 %70, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %71 = call i1 @get_creg_bit(i1* %3, i64 6)
  br i1 %71, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %72 = call i1 @get_creg_bit(i1* %3, i64 7)
  br i1 %72, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %73 = call i1 @get_creg_bit(i1* %3, i64 8)
  br i1 %73, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
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
