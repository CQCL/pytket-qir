; ModuleID = './and_only.bc'
source_filename = "qat-link"

define void @classical_and_only() local_unnamed_addr #0 {
entry:
  %0 = and i64 1, 2
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
