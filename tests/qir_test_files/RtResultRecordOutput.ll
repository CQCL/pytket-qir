source_filename = "test"

%Result = type opaque

define void @main() #0 {
entry:
  call void @__quantum__rt__result__record_output(%Result* null)
  ret void
}

declare void @__quantum__rt__result__record_output(%Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="1" }
