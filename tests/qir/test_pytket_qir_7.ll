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
  %0 = call i1* @create_creg(i64 3)
  %1 = call i1* @create_creg(i64 3)
  %2 = call i1* @create_creg(i64 3)
  %3 = call i1* @create_creg(i64 3)
  %4 = call i64 @get_int_from_creg(i1* %0)
  %5 = call i64 @get_int_from_creg(i1* %0)
  %6 = call i64 @get_int_from_creg(i1* %0)
  %7 = call i64 @get_int_from_creg(i1* %3)
  %8 = and i64 %6, %7
  call void @set_creg_to_int(i1* %2, i64 %8)
  %9 = call i64 @get_int_from_creg(i1* %0)
  %10 = call i64 @get_int_from_creg(i1* %0)
  %11 = call i64 @get_int_from_creg(i1* %0)
  %12 = call i64 @get_int_from_creg(i1* %1)
  %13 = or i64 %11, %12
  call void @set_creg_to_int(i1* %2, i64 %13)
  %14 = call i64 @get_int_from_creg(i1* %0)
  %15 = call i64 @get_int_from_creg(i1* %0)
  %16 = call i64 @get_int_from_creg(i1* %0)
  %17 = call i64 @get_int_from_creg(i1* %1)
  %18 = xor i64 %16, %17
  call void @set_creg_to_int(i1* %2, i64 %18)
  %19 = call i64 @get_int_from_creg(i1* %0)
  %20 = call i64 @get_int_from_creg(i1* %0)
  %21 = call i64 @get_int_from_creg(i1* %0)
  %22 = call i64 @get_int_from_creg(i1* %1)
  %23 = add i64 %21, %22
  call void @set_creg_to_int(i1* %2, i64 %23)
  %24 = call i64 @get_int_from_creg(i1* %0)
  %25 = call i64 @get_int_from_creg(i1* %0)
  %26 = call i64 @get_int_from_creg(i1* %0)
  %27 = call i64 @get_int_from_creg(i1* %1)
  %28 = sub i64 %26, %27
  call void @set_creg_to_int(i1* %2, i64 %28)
  %29 = call i64 @get_int_from_creg(i1* %0)
  %30 = call i64 @get_int_from_creg(i1* %0)
  %31 = call i64 @get_int_from_creg(i1* %0)
  %32 = call i64 @get_int_from_creg(i1* %1)
  %33 = mul i64 %31, %32
  call void @set_creg_to_int(i1* %2, i64 %33)
  %34 = call i64 @get_int_from_creg(i1* %0)
  %35 = call i64 @get_int_from_creg(i1* %0)
  %36 = call i64 @get_int_from_creg(i1* %0)
  %37 = call i64 @get_int_from_creg(i1* %1)
  %38 = shl i64 %36, %37
  call void @set_creg_to_int(i1* %2, i64 %38)
  %39 = call i64 @get_int_from_creg(i1* %0)
  %40 = call i64 @get_int_from_creg(i1* %0)
  %41 = call i64 @get_int_from_creg(i1* %0)
  %42 = call i64 @get_int_from_creg(i1* %1)
  %43 = lshr i64 %41, %42
  call void @set_creg_to_int(i1* %2, i64 %43)
  %44 = call i64 @get_int_from_creg(i1* %0)
  %45 = call i64 @get_int_from_creg(i1* %0)
  %46 = call i64 @get_int_from_creg(i1* %0)
  %47 = call i64 @get_int_from_creg(i1* %1)
  %48 = icmp eq i64 %46, %47
  call void @set_creg_bit(i1* %2, i64 0, i1 %48)
  %49 = call i64 @get_int_from_creg(i1* %0)
  %50 = call i64 @get_int_from_creg(i1* %0)
  %51 = call i64 @get_int_from_creg(i1* %0)
  %52 = call i64 @get_int_from_creg(i1* %1)
  %53 = icmp ne i64 %51, %52
  call void @set_creg_bit(i1* %2, i64 0, i1 %53)
  %54 = call i64 @get_int_from_creg(i1* %0)
  %55 = call i64 @get_int_from_creg(i1* %0)
  %56 = call i64 @get_int_from_creg(i1* %0)
  %57 = call i64 @get_int_from_creg(i1* %1)
  %58 = icmp ugt i64 %56, %57
  call void @set_creg_bit(i1* %2, i64 0, i1 %58)
  %59 = call i64 @get_int_from_creg(i1* %0)
  %60 = call i64 @get_int_from_creg(i1* %0)
  %61 = call i64 @get_int_from_creg(i1* %0)
  %62 = call i64 @get_int_from_creg(i1* %1)
  %63 = icmp uge i64 %61, %62
  call void @set_creg_bit(i1* %2, i64 0, i1 %63)
  %64 = call i64 @get_int_from_creg(i1* %0)
  %65 = call i64 @get_int_from_creg(i1* %0)
  %66 = call i64 @get_int_from_creg(i1* %0)
  %67 = call i64 @get_int_from_creg(i1* %1)
  %68 = icmp ult i64 %66, %67
  call void @set_creg_bit(i1* %2, i64 0, i1 %68)
  %69 = call i64 @get_int_from_creg(i1* %0)
  %70 = call i64 @get_int_from_creg(i1* %0)
  %71 = call i64 @get_int_from_creg(i1* %0)
  %72 = call i64 @get_int_from_creg(i1* %1)
  %73 = icmp ule i64 %71, %72
  call void @set_creg_bit(i1* %2, i64 0, i1 %73)
  call void @__quantum__rt__tuple_start_record_output()
  %74 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %74, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %75 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %75, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %76 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %76, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  %77 = call i64 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i64 %77, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg(%Qubit*, i1*, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

attributes #0 = { "entry_point" "num_required_qubits"="2" "num_required_results"="2" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
