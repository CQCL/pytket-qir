; ModuleID = 'test'
source_filename = "test"

declare i1 @source()

define void @main() #0 {
entry:
  %0 = call i1 @source()
  %1 = xor i1 %0, true
  %2 = or i1 %1, true
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="10" }
