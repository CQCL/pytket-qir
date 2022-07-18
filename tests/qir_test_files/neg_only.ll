; ModuleID = './neg_only.bc'
source_filename = "qat-link"

define void @classical_neg_only() local_unnamed_addr #0 {
entry:
  %0 = sub i64 0, 2
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
