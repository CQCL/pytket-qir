; ModuleID = './phasedx_only.bc'
source_filename = "qat-link"

%Qubit = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__u1q__body(double 0xC015FDBBE9BBA775, double 0xC015FDBBE9BBA775, %Qubit* null)
  ret void
}

declare void @__quantum__qis__u1q__body(double, double, %Qubit*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="0" }
