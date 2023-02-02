; ModuleID = 'test'
source_filename = "test"

declare i1 @source()

define void @main() #0 {
entry:
  %0 = call i1 @source()
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="10" }
