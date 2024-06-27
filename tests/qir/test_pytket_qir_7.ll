; ModuleID = 'test_pytket_qir_7'
source_filename = "test_pytket_qir_7"

%Result = type opaque
%Qubit = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"
@3 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i32 3)
  %1 = call i1* @create_creg(i32 3)
  %2 = call i1* @create_creg(i32 3)
  %3 = call i1* @create_creg(i32 3)
  %4 = call i32 @get_int_from_creg(i1* %0)
  %5 = call i32 @get_int_from_creg(i1* %3)
  %6 = and i32 %4, %5
  call void @set_creg_to_int(i1* %2, i32 %6)
  %7 = call i32 @get_int_from_creg(i1* %0)
  %8 = call i32 @get_int_from_creg(i1* %1)
  %9 = or i32 %7, %8
  call void @set_creg_to_int(i1* %2, i32 %9)
  %10 = call i32 @get_int_from_creg(i1* %0)
  %11 = call i32 @get_int_from_creg(i1* %1)
  %12 = xor i32 %10, %11
  call void @set_creg_to_int(i1* %2, i32 %12)
  %13 = call i32 @get_int_from_creg(i1* %0)
  %14 = call i32 @get_int_from_creg(i1* %1)
  %15 = add i32 %13, %14
  call void @set_creg_to_int(i1* %2, i32 %15)
  %16 = call i32 @get_int_from_creg(i1* %0)
  %17 = call i32 @get_int_from_creg(i1* %1)
  %18 = sub i32 %16, %17
  call void @set_creg_to_int(i1* %2, i32 %18)
  %19 = call i32 @get_int_from_creg(i1* %0)
  %20 = call i32 @get_int_from_creg(i1* %1)
  %21 = mul i32 %19, %20
  call void @set_creg_to_int(i1* %2, i32 %21)
  %22 = call i32 @get_int_from_creg(i1* %0)
  %23 = call i32 @get_int_from_creg(i1* %1)
  %24 = shl i32 %22, %23
  call void @set_creg_to_int(i1* %2, i32 %24)
  %25 = call i32 @get_int_from_creg(i1* %0)
  %26 = call i32 @get_int_from_creg(i1* %1)
  %27 = lshr i32 %25, %26
  call void @set_creg_to_int(i1* %2, i32 %27)
  %28 = call i32 @get_int_from_creg(i1* %0)
  %29 = call i32 @get_int_from_creg(i1* %1)
  %30 = icmp eq i32 %28, %29
  call void @set_creg_bit(i1* %2, i32 0, i1 %30)
  %31 = call i32 @get_int_from_creg(i1* %0)
  %32 = call i32 @get_int_from_creg(i1* %1)
  %33 = icmp ne i32 %31, %32
  call void @set_creg_bit(i1* %2, i32 0, i1 %33)
  %34 = call i32 @get_int_from_creg(i1* %0)
  %35 = call i32 @get_int_from_creg(i1* %1)
  %36 = icmp ugt i32 %34, %35
  call void @set_creg_bit(i1* %2, i32 0, i1 %36)
  %37 = call i32 @get_int_from_creg(i1* %0)
  %38 = call i32 @get_int_from_creg(i1* %1)
  %39 = icmp uge i32 %37, %38
  call void @set_creg_bit(i1* %2, i32 0, i1 %39)
  %40 = call i32 @get_int_from_creg(i1* %0)
  %41 = call i32 @get_int_from_creg(i1* %1)
  %42 = icmp ult i32 %40, %41
  call void @set_creg_bit(i1* %2, i32 0, i1 %42)
  %43 = call i32 @get_int_from_creg(i1* %0)
  %44 = call i32 @get_int_from_creg(i1* %1)
  %45 = icmp ule i32 %43, %44
  call void @set_creg_bit(i1* %2, i32 0, i1 %45)
  call void @__quantum__rt__tuple_start_record_output()
  %46 = call i32 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i32 %46, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %47 = call i32 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i32 %47, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %48 = call i32 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i32 %48, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %49 = call i32 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i32 %49, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i32)

declare void @set_creg_bit(i1*, i32, i1)

declare void @set_creg_to_int(i1*, i32)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i32)

declare i32 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i32)

declare void @__quantum__rt__int_record_output(i32, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="2" "required_num_results"="2" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
