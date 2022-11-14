source_filename = "Generated from input pytket circuit and wasm_empty_adder.wasm file."

define void @main() #0 {
entry:
  %0 = call i32 @__quantum__hybrid__empty_add_one__body()
  ret void
}

declare i32 @__quantum__hybrid__empty_add_one__body()

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="64" }
