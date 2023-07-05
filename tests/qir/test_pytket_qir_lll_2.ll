; ModuleID = "test_pytket_qir_ll_2"
target triple = "unknown-unknown-unknown"
target datalayout = ""

%"Qubit" = type opaque
define void @"main"()
{
entry:
  call void @"__quantum__qis__h__body"(%"Qubit"* 0)
}

@"__quantum__qis__h__body" = external global void (%"Qubit"*)
!llvm.module.flags = !{ !0, !1, !2, !3 }
!0 = !{ !"qir_major_version", i32 1 }
!1 = !{ !"qir_minor_version", i32 0 }
!2 = !{ !"dynamic_qubit_management", i1 0 }
!3 = !{ !"dynamic_result_management", i1 0 }