; ModuleID = './t_only.bc'
source_filename = "qat-link"

%Qubit = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__t__body(%Qubit* null)
  ret void
}

declare void @__quantum__qis__t__body(%Qubit*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="0" }
