; ModuleID = './mul_only.bc'
source_filename = "qat-link"

define void @classical_mul_only() local_unnamed_addr #0 {
entry:
  %0 = mul i64 2, 1
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
