source_filename = "Generated from input pytket circuit"

%Result = type opaque

declare i1 @__quantum__qis__read_result__body(%Result*)

define void @main() #0 {
entry:
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %1 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="4" }
