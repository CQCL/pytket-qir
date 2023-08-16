; ModuleID = 'test_pytket_qir_wasm_ii'
source_filename = "test_pytket_qir_wasm_ii"

%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"
@1 = internal constant [3 x i8] c"c0\00"
@2 = internal constant [3 x i8] c"c1\00"
@3 = internal constant [3 x i8] c"c2\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i32 6)
  %1 = call i1* @create_creg(i32 3)
  %2 = call i1* @create_creg(i32 4)
  %3 = call i1* @create_creg(i32 5)
  %4 = call i32 @get_int_from_creg(i1* %1)
  %5 = call i32 @get_int_from_creg(i1* %2)
  %6 = call i32 @multi(i32 %4, i32 %5)
  call void @set_creg_to_int(i1* %3, i32 %6)
  %7 = call i32 @get_int_from_creg(i1* %3)
  %8 = call i32 @add_one(i32 %7)
  call void @set_creg_to_int(i1* %3, i32 %8)
  %9 = call i32 @get_int_from_creg(i1* %3)
  call void @no_return(i32 %9)
  call void @init()
  %10 = call i32 @no_parameters()
  call void @set_creg_to_int(i1* %3, i32 %10)
  call void @__quantum__rt__tuple_start_record_output()
  %11 = call i32 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i32 %11, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %12 = call i32 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i32 %12, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @1, i32 0, i32 0))
  %13 = call i32 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i32 %13, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @2, i32 0, i32 0))
  %14 = call i32 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i32 %14, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i32)

declare void @set_creg_bit(i1*, i32, i1)

declare void @set_creg_to_int(i1*, i32)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i32)

declare i32 @get_int_from_creg(i1*)

declare void @__quantum__rt__int_record_output(i32, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @init() #1

declare i32 @add_one(i32)

declare i32 @multi(i32, i32)

declare i32 @add_two(i32)

declare i32 @add_eleven(i32)

declare void @no_return(i32) #1

declare i32 @no_parameters()

declare i32 @new_function()

attributes #0 = { "entry_point" "num_required_qubits"="6" "num_required_results"="6" "output_labeling_schema" "qir_profiles"="custom" }

attributes #1 = { "wasm" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
