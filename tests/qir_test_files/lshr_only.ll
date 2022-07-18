; ModuleID = './lshr_only.bc'
source_filename = "qat-link"

define void @classical_lshr_only() local_unnamed_addr #0 {
entry:
  %0 = lshr i64 2, 2
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
