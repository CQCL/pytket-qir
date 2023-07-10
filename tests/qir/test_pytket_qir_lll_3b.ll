; ModuleID = "test_pytket_qir_ll_3"

%Result = type opaque
%Qubit = type opaque

define void @main() #0 {
entry:
  call void @"__quantum__qis__h__body"(%Qubit* inttoptr (i32 0 to %Qubit*))
  call void @__quantum__rt__tuple_start_record_output()
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

@"__quantum__qis__h__body" = external global void (%Qubit*)


declare void @set_one_bit_in_reg(i64, i64, i1)


declare i1 @__quantum__qis__read_result__body(%Result*)


declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()
!llvm.module.flags = !{ !0, !1, !2, !3 }
!0 = !{ !"qir_major_version", i32 1 }
!1 = !{ !"qir_minor_version", i32 0 }
!2 = !{ !"dynamic_qubit_management", i1 0 }
!3 = !{ !"dynamic_result_management", i1 0 }