; ModuleID = './uge_only.bc'
source_filename = "qat-link"

define void @classical_uge_only() local_unnamed_addr #0 {
entry:
  %0 = icmp uge i64 2, 3
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
