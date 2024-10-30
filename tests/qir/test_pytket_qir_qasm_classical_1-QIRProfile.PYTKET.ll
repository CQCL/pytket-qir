; ModuleID = 'test_pytket_qir_qasm_classical_1'
source_filename = "test_pytket_qir_qasm_classical_1"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"
@3 = internal constant [2 x i8] c"d\00"
@4 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 2)
  %1 = call i1* @create_creg(i64 3)
  %2 = call i1* @create_creg(i64 4)
  %3 = call i1* @create_creg(i64 1)
  %4 = call i1* @create_creg(i64 6)
  call void @set_creg_bit(i1* %2, i64 0, i1 false)
  call void @set_creg_bit(i1* %2, i64 1, i1 true)
  call void @set_creg_bit(i1* %2, i64 2, i1 false)
  call void @set_creg_bit(i1* %2, i64 3, i1 false)
  %5 = call i64 @get_int_from_creg(i1* %1)
  %6 = icmp eq i64 2, %5
  call void @set_creg_bit(i1* %4, i64 0, i1 %6)
  %7 = call i1 @get_creg_bit(i1* %0, i64 0)
  call void @set_creg_bit(i1* %2, i64 0, i1 %7)
  %8 = call i1 @get_creg_bit(i1* %0, i64 1)
  call void @set_creg_bit(i1* %2, i64 1, i1 %8)
  %9 = call i1 @get_creg_bit(i1* %4, i64 0)
  br i1 %9, label %contb0, label %condb0

condb0:                                           ; preds = %entry
  %10 = call i1 @get_creg_bit(i1* %1, i64 1)
  %11 = call i1 @get_creg_bit(i1* %0, i64 1)
  %12 = and i1 %10, %11
  %13 = call i1 @get_creg_bit(i1* %0, i64 0)
  %14 = or i1 %12, %13
  call void @set_creg_bit(i1* %2, i64 1, i1 %14)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %15 = call i64 @get_int_from_creg(i1* %1)
  %16 = call i64 @get_int_from_creg(i1* %0)
  %17 = and i64 %15, %16
  %18 = call i64 @get_int_from_creg(i1* %3)
  %19 = or i64 %17, %18
  call void @set_creg_to_int(i1* %2, i64 %19)
  %20 = call i1 @get_creg_bit(i1* %0, i64 0)
  %21 = xor i1 %20, true
  call void @set_creg_bit(i1* %3, i64 0, i1 %21)
  %22 = call i64 @get_int_from_creg(i1* %2)
  %23 = icmp sgt i64 2, %22
  %24 = call i64 @get_int_from_creg(i1* %2)
  %25 = icmp sgt i64 %24, 4294967295
  %26 = and i1 %23, %25
  call void @set_creg_bit(i1* %4, i64 1, i1 %26)
  %27 = call i64 @get_int_from_creg(i1* %2)
  %28 = icmp sgt i64 0, %27
  %29 = call i64 @get_int_from_creg(i1* %2)
  %30 = icmp sgt i64 %29, 2
  %31 = and i1 %28, %30
  call void @set_creg_bit(i1* %4, i64 2, i1 %31)
  %32 = call i64 @get_int_from_creg(i1* %2)
  %33 = icmp sgt i64 0, %32
  %34 = call i64 @get_int_from_creg(i1* %2)
  %35 = icmp sgt i64 %34, 1
  %36 = and i1 %33, %35
  call void @set_creg_bit(i1* %4, i64 3, i1 %36)
  %37 = call i64 @get_int_from_creg(i1* %2)
  %38 = icmp sgt i64 3, %37
  %39 = call i64 @get_int_from_creg(i1* %2)
  %40 = icmp sgt i64 %39, 4294967295
  %41 = and i1 %38, %40
  call void @set_creg_bit(i1* %4, i64 4, i1 %41)
  %42 = call i64 @get_int_from_creg(i1* %2)
  %43 = icmp eq i64 2, %42
  call void @set_creg_bit(i1* %4, i64 5, i1 %43)
  %44 = call i1 @get_creg_bit(i1* %4, i64 1)
  br i1 %44, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %45 = call i1 @get_creg_bit(i1* %4, i64 2)
  br i1 %45, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %46 = call i1 @get_creg_bit(i1* %4, i64 3)
  br i1 %46, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %47 = call i1 @get_creg_bit(i1* %4, i64 4)
  br i1 %47, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %48 = call i1 @get_creg_bit(i1* %4, i64 5)
  br i1 %48, label %contb5, label %condb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %49 = call i1 @get_creg_bit(i1* %3, i64 0)
  br i1 %49, label %condb6, label %contb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__rx__body(double 0x400921FB54442D18, %Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %50 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %50, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %51 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %51, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %52 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %52, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %53 = call i64 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %53, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  %54 = call i64 @get_int_from_creg(i1* %4)
  call void @__quantum__rt__int_record_output(i64 %54, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @4, i32 0, i32 0))
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

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__rx__body(double, %Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
