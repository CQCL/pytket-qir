; ModuleID = 'test_pytket_qir_21'
source_filename = "test_pytket_qir_21"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"c\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %1 = zext i1 %0 to i64
  %2 = mul i64 %1, 1
  %3 = or i64 %2, 0
  %4 = sub i64 1, %1
  %5 = mul i64 %4, 1
  %6 = xor i64 9223372036854775807, %5
  %7 = and i64 %6, %3
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  %8 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  %9 = zext i1 %8 to i64
  %10 = mul i64 %9, 1
  %11 = or i64 %10, 0
  %12 = sub i64 1, %9
  %13 = mul i64 %12, 1
  %14 = xor i64 9223372036854775807, %13
  %15 = and i64 %14, %11
  %16 = icmp eq i64 %7, %15
  %17 = zext i1 %16 to i64
  %18 = mul i64 %17, 1
  %19 = or i64 %18, 0
  %20 = sub i64 1, %17
  %21 = mul i64 %20, 1
  %22 = xor i64 9223372036854775807, %21
  %23 = and i64 %22, %19
  %24 = icmp ne i64 %7, %15
  %25 = zext i1 %24 to i64
  %26 = mul i64 %25, 1
  %27 = or i64 %26, %23
  %28 = sub i64 1, %25
  %29 = mul i64 %28, 1
  %30 = xor i64 9223372036854775807, %29
  %31 = and i64 %30, %27
  %32 = icmp ugt i64 %7, %15
  %33 = zext i1 %32 to i64
  %34 = mul i64 %33, 1
  %35 = or i64 %34, %31
  %36 = sub i64 1, %33
  %37 = mul i64 %36, 1
  %38 = xor i64 9223372036854775807, %37
  %39 = and i64 %38, %35
  %40 = icmp uge i64 %7, %15
  %41 = zext i1 %40 to i64
  %42 = mul i64 %41, 1
  %43 = or i64 %42, %39
  %44 = sub i64 1, %41
  %45 = mul i64 %44, 1
  %46 = xor i64 9223372036854775807, %45
  %47 = and i64 %46, %43
  %48 = icmp ult i64 %7, %15
  %49 = zext i1 %48 to i64
  %50 = mul i64 %49, 1
  %51 = or i64 %50, %47
  %52 = sub i64 1, %49
  %53 = mul i64 %52, 1
  %54 = xor i64 9223372036854775807, %53
  %55 = and i64 %54, %51
  %56 = icmp ule i64 %7, %15
  %57 = zext i1 %56 to i64
  %58 = mul i64 %57, 1
  %59 = or i64 %58, %55
  %60 = sub i64 1, %57
  %61 = mul i64 %60, 1
  %62 = xor i64 9223372036854775807, %61
  %63 = and i64 %62, %59
  call void @__quantum__rt__int_record_output(i64 %7, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %15, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %63, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="2" "required_num_results"="2" }
attributes #1 = { "irreversible" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
