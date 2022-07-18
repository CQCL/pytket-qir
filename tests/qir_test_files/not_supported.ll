; ModuleID = './not_supported.bc'
source_filename = "qat-link"

define void @not_supported() local_unnamed_addr #0 {
entry:
  %0 = icmp eq i64 2, 3
  %1 = sext i1 %0 to i8
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
