; ModuleID = 'ptest_pytket_qir_14'
source_filename = "ptest_pytket_qir_14"

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
  %0 = call i64 @create_int(i64 8)
  %1 = call i64 @create_int(i64 10)
  %2 = call i64 @create_int(i64 10)
  %3 = call i64 @create_int(i64 9)
  %4 = call i64 @create_int(i64 64)
  %5 = call i64 @create_int(i64 64)
  %6 = call i64 @create_int(i64 64)
  %7 = call i64 @set_bit_in_int(i64 %0, i64 0, i1 true)
  %8 = call i64 @set_bit_in_int(i64 %1, i64 0, i1 true)
  %9 = call i64 @set_bit_in_int(i64 %8, i64 1, i1 true)
  %10 = call i64 @set_bit_in_int(i64 %9, i64 2, i1 false)
  %11 = call i64 @set_bit_in_int(i64 %10, i64 3, i1 false)
  %12 = call i64 @set_bit_in_int(i64 %11, i64 4, i1 false)
  %13 = call i64 @set_bit_in_int(i64 %12, i64 5, i1 false)
  %14 = call i64 @set_bit_in_int(i64 %13, i64 6, i1 false)
  %15 = call i64 @set_bit_in_int(i64 %14, i64 7, i1 false)
  %16 = call i64 @set_bit_in_int(i64 %15, i64 8, i1 false)
  %17 = call i64 @set_bit_in_int(i64 %16, i64 9, i1 false)
  %18 = call i64 @set_bit_in_int(i64 %7, i64 0, i1 false)
  %19 = call i64 @set_bit_in_int(i64 %18, i64 1, i1 true)
  %20 = call i64 @set_bit_in_int(i64 %19, i64 2, i1 false)
  %21 = call i64 @set_bit_in_int(i64 %20, i64 3, i1 false)
  %22 = call i64 @set_bit_in_int(i64 %21, i64 4, i1 false)
  %23 = call i64 @set_bit_in_int(i64 %22, i64 5, i1 false)
  %24 = call i64 @set_bit_in_int(i64 %23, i64 6, i1 false)
  %25 = call i64 @set_bit_in_int(i64 %24, i64 7, i1 false)
  %26 = call i64 @set_bit_in_int(i64 %25, i64 0, i1 true)
  %27 = call i64 @set_bit_in_int(i64 %26, i64 1, i1 true)
  %28 = call i64 @set_bit_in_int(i64 %27, i64 2, i1 true)
  %29 = call i64 @set_bit_in_int(i64 %28, i64 3, i1 false)
  %30 = call i64 @set_bit_in_int(i64 %29, i64 4, i1 true)
  %31 = call i64 @set_bit_in_int(i64 %30, i64 5, i1 false)
  %32 = call i64 @set_bit_in_int(i64 %31, i64 6, i1 false)
  %33 = call i64 @set_bit_in_int(i64 %32, i64 7, i1 false)
  %34 = call i1 @get_bit_from_int(i64 %33, i64 0)
  %35 = call i64 @set_bit_in_int(i64 %17, i64 0, i1 %34)
  %36 = call i1 @get_bit_from_int(i64 %33, i64 1)
  %37 = call i64 @set_bit_in_int(i64 %35, i64 1, i1 %36)
  %38 = call i1 @get_bit_from_int(i64 %33, i64 2)
  %39 = call i64 @set_bit_in_int(i64 %37, i64 2, i1 %38)
  %40 = call i1 @get_bit_from_int(i64 %33, i64 3)
  %41 = call i64 @set_bit_in_int(i64 %39, i64 3, i1 %40)
  %42 = call i1 @get_bit_from_int(i64 %33, i64 4)
  %43 = call i64 @set_bit_in_int(i64 %41, i64 4, i1 %42)
  %44 = call i1 @get_bit_from_int(i64 %33, i64 5)
  %45 = call i64 @set_bit_in_int(i64 %43, i64 5, i1 %44)
  %46 = call i1 @get_bit_from_int(i64 %33, i64 6)
  %47 = call i64 @set_bit_in_int(i64 %45, i64 6, i1 %46)
  %48 = call i1 @get_bit_from_int(i64 %33, i64 7)
  %49 = call i64 @set_bit_in_int(i64 %47, i64 7, i1 %48)
  %50 = add i64 %33, %49
  %51 = sub i64 %33, %49
  %52 = shl i64 %33, 1
  %53 = lshr i64 %52, 1
  %54 = icmp eq i64 1, %52
  %55 = call i64 @set_bit_in_int(i64 %3, i64 4, i1 %54)
  %56 = icmp sgt i64 2, %52
  %57 = icmp sgt i64 %52, -1
  %58 = and i1 %56, %57
  %59 = call i64 @set_bit_in_int(i64 %55, i64 5, i1 %58)
  %60 = icmp eq i64 0, %52
  %61 = call i64 @set_bit_in_int(i64 %59, i64 6, i1 %60)
  %62 = icmp sgt i64 1, %52
  %63 = icmp sgt i64 %52, -1
  %64 = and i1 %62, %63
  %65 = call i64 @set_bit_in_int(i64 %61, i64 7, i1 %64)
  %66 = icmp sgt i64 0, %52
  %67 = icmp sgt i64 %52, 1
  %68 = and i1 %66, %67
  %69 = call i64 @set_bit_in_int(i64 %65, i64 8, i1 %68)
  %70 = call i1 @get_bit_from_int(i64 %52, i64 0)
  br i1 %70, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %71 = call i1 @get_bit_from_int(i64 %52, i64 0)
  %72 = call i1 @get_bit_from_int(i64 %53, i64 0)
  %73 = xor i1 %71, %72
  %74 = call i64 @set_bit_in_int(i64 %69, i64 1, i1 %73)
  %75 = xor i64 %52, %53
  %76 = and i64 %52, %53
  %77 = or i64 %52, %53
  %78 = icmp eq i64 1, %75
  %79 = call i64 @set_bit_in_int(i64 %74, i64 0, i1 %78)
  %80 = icmp eq i64 1, %76
  %81 = call i64 @set_bit_in_int(i64 %79, i64 2, i1 %80)
  %82 = icmp eq i64 1, %77
  %83 = call i64 @set_bit_in_int(i64 %81, i64 3, i1 %82)
  %84 = call i1 @get_bit_from_int(i64 %83, i64 0)
  br i1 %84, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %85 = call i1 @get_bit_from_int(i64 %83, i64 1)
  br i1 %85, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %86 = call i1 @get_bit_from_int(i64 %83, i64 2)
  br i1 %86, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %87 = call i1 @get_bit_from_int(i64 %83, i64 3)
  br i1 %87, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %88 = call i1 @get_bit_from_int(i64 %52, i64 0)
  br i1 %88, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %89 = call i1 @get_bit_from_int(i64 %83, i64 4)
  br i1 %89, label %contb6, label %condb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %90 = call i1 @get_bit_from_int(i64 %52, i64 0)
  br i1 %90, label %contb7, label %condb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %91 = call i1 @get_bit_from_int(i64 %83, i64 5)
  br i1 %91, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %92 = call i1 @get_bit_from_int(i64 %83, i64 6)
  br i1 %92, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %93 = call i1 @get_bit_from_int(i64 %83, i64 7)
  br i1 %93, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %94 = call i1 @get_bit_from_int(i64 %83, i64 8)
  br i1 %94, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
  call void @__quantum__rt__int_record_output(i64 %52, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %53, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %51, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %83, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %75, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @4, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %76, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @5, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %77, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @6, i32 0, i32 0))
  ret void
}

declare i1 @get_bit_from_int(i64, i64)

declare i64 @set_bit_in_int(i64, i64, i1)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @create_int(i64)

declare i64 @mz_to_int(%Qubit*, i64, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
