source_filename = "Generated from input pytket circuit"

%Result = type opaque

declare void @__quantum__rt__result__record_output(%Result*)

define void @main() #0 {
entry:
  call void @__quantum__rt__result__record_output(%Result* null)
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="1" }
