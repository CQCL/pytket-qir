; ModuleID = './h_only_test.bc'
source_filename = "qat-link"

%Qubit.1 = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__h__body(%Qubit.1* null)
  ret void
}

declare void @__quantum__qis__h__body(%Qubit.1*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="0" }
