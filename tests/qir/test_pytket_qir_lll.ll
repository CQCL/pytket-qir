; ModuleID = "test_pytket_qir_ll"
target triple = "unknown-unknown-unknown"
target datalayout = ""

%"Qubit" = type opaque
define void @"main"()
{
entry:
}

!llvm.module.flags = !{ !0, !1, !2, !3 }
!0 = !{ !"qir_major_version", i32 1 }
!1 = !{ !"qir_minor_version", i32 0 }
!2 = !{ !"dynamic_qubit_management", i1 0 }
!3 = !{ !"dynamic_result_management", i1 0 }