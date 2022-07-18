; ModuleID = './cx_only.bc'
source_filename = "qat-link"

%Qubit = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  ret void
}

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="0" }
