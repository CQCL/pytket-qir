; ModuleID = 'test_pytket_qir_wasm_ii'
source_filename = "test_pytket_qir_wasm_ii"

%Result = type opaque

@0 = internal constant [2 x i8] c"c\00"
@1 = internal constant [3 x i8] c"c0\00"
@2 = internal constant [3 x i8] c"c1\00"
@3 = internal constant [3 x i8] c"c2\00"

define void @main() #0 {
entry:
  %0 = call i32 @multi(i32 0, i32 0)
  %1 = call i32 @add_one(i32 %0)
  call void @no_return(i32 %1)
  call void @init()
  %2 = call i32 @no_parameters()
  call void @__quantum__rt__int_record_output(i32 0, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i32 0, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i32 0, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i32 %2, i8* getelementptr inbounds ([3 x i8], [3 x i8]* @3, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i32, i8*)

declare void @init() #1

declare i32 @add_one(i32) #1

declare i32 @multi(i32, i32) #1

declare i32 @add_two(i32) #1

declare i32 @add_eleven(i32) #1

declare void @no_return(i32) #1

declare i32 @no_parameters() #1

declare i32 @new_function() #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="6" "required_num_results"="6" }

attributes #1 = { "wasm" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
