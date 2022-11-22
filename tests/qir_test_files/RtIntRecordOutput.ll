source_filename = "Generated from input pytket circuit"

declare void @__quantum__rt__integer__record_output(i64)

define void @main() #0 {
entry:
  call void @__quantum__rt__integer__record_output(i64 3)
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="192" }
