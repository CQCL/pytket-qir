source_filename = "Generated from input pytket circuit and wasm_empty_adder.wasm file."

declare i32 @__quantum__hybrid__empty_add_one__body()

define void @main() #0 {
entry:
  %0 = call i32 @__quantum__hybrid__empty_add_one__body()
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="64" }
