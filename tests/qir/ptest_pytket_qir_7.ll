; ModuleID = 'ptest_pytket_qir_7'
source_filename = "ptest_pytket_qir_7"

%Result = type opaque
%Qubit = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"
@3 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  %0 = call i64 @create_int(i64 3)
  %1 = call i64 @create_int(i64 3)
  %2 = call i64 @create_int(i64 3)
  %3 = call i64 @create_int(i64 3)
  %4 = and i64 %0, %3
  %5 = or i64 %0, %1
  %6 = xor i64 %0, %1
  %7 = add i64 %0, %1
  %8 = sub i64 %0, %1
  %9 = mul i64 %0, %1
  %10 = shl i64 %0, %1
  %11 = lshr i64 %0, %1
  %12 = icmp eq i64 %0, %1
  %13 = call i64 @set_bit_in_int(i64 %11, i64 0, i1 %12)
  %14 = icmp ne i64 %0, %1
  %15 = call i64 @set_bit_in_int(i64 %13, i64 0, i1 %14)
  %16 = icmp ugt i64 %0, %1
  %17 = call i64 @set_bit_in_int(i64 %15, i64 0, i1 %16)
  %18 = icmp uge i64 %0, %1
  %19 = call i64 @set_bit_in_int(i64 %17, i64 0, i1 %18)
  %20 = icmp ult i64 %0, %1
  %21 = call i64 @set_bit_in_int(i64 %19, i64 0, i1 %20)
  %22 = icmp ule i64 %0, %1
  %23 = call i64 @set_bit_in_int(i64 %21, i64 0, i1 %22)
  call void @__quantum__rt__int_record_output(i64 %0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %1, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %23, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %3, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  ret void
}

declare i1 @get_bit_from_int(i64, i64)

declare i64 @set_bit_in_int(i64, i64, i1)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @create_int(i64)

declare i64 @mz_to_int(%Qubit*, i64, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="2" "required_num_results"="2" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
