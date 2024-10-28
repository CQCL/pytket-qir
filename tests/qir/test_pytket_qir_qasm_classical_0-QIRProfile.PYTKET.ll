; ModuleID = 'test_pytket_qir_qasm_classical_0'
source_filename = "test_pytket_qir_qasm_classical_0"

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
  %4 = call i1* @create_creg(i64 2)
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
  call void @set_creg_to_int(i1* %2, i64 %17)
  %18 = call i64 @get_int_from_creg(i1* %0)
  %19 = call i64 @get_int_from_creg(i1* %1)
  %20 = add i64 %18, %19
  call void @set_creg_to_int(i1* %1, i64 %20)
  %21 = call i1 @get_creg_bit(i1* %1, i64 0)
  %22 = call i1 @get_creg_bit(i1* %1, i64 2)
  %23 = sub i1 true, %22
  %24 = xor i1 %21, %23
  call void @set_creg_bit(i1* %1, i64 1, i1 %24)
  %25 = call i64 @get_int_from_creg(i1* %0)
  %26 = call i64 @get_int_from_creg(i1* %1)
  %27 = call i64 @get_int_from_creg(i1* %2)
  %28 = mul i64 %26, %27
  %29 = sub i64 %25, %28
  call void @set_creg_to_int(i1* %2, i64 %29)
  %30 = call i64 @get_int_from_creg(i1* %0)
  %31 = shl i64 %30, 1
  call void @set_creg_to_int(i1* %3, i64 %31)
  %32 = call i64 @get_int_from_creg(i1* %2)
  %33 = lshr i64 %32, 2
  call void @set_creg_to_int(i1* %3, i64 %33)
  call void @set_creg_bit(i1* %2, i64 0, i1 true)
  %34 = call i64 @get_int_from_creg(i1* %0)
  %35 = call i64 @get_int_from_creg(i1* %2)
  %36 = mul i64 %34, %35
  %37 = call i64 @get_int_from_creg(i1* %1)
  %38 = mul i64 %36, %37
  call void @set_creg_to_int(i1* %1, i64 %38)
  %39 = call i1 @get_creg_bit(i1* %0, i64 0)
  %40 = xor i1 %39, true
  call void @set_creg_bit(i1* %3, i64 0, i1 %40)
  %41 = call i64 @get_int_from_creg(i1* %2)
  %42 = icmp sgt i64 2, %41
  %43 = call i64 @get_int_from_creg(i1* %2)
  %44 = icmp sgt i64 %43, 4294967295
  %45 = and i1 %42, %44
  call void @set_creg_bit(i1* %4, i64 1, i1 %45)
  %46 = call i1 @get_creg_bit(i1* %4, i64 1)
  br i1 %46, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %47 = call i1 @get_creg_bit(i1* %3, i64 0)
  br i1 %47, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__rx__body(double 0x400921FB54442D18, %Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %48 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %48, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %49 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %49, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %50 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %50, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %51 = call i64 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %51, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  %52 = call i64 @get_int_from_creg(i1* %4)
  call void @__quantum__rt__int_record_output(i64 %52, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @4, i32 0, i32 0))
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
