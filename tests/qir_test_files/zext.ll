; ModuleID = 'zext.bc'
source_filename = "qat-link"

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  %0 = zext i1 true to i64
  call void @__quantum__rt__int_record_output(i64 %0)
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
