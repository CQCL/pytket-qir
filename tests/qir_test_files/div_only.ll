; ModuleID = './div_only.bc'
source_filename = "qat-link"

define void @classical_div_only() local_unnamed_addr #0 {
entry:
  %0 = sdiv i64 2, 1
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
