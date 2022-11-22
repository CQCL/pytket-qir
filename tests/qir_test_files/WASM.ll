source_filename = "Generated from input pytket circuit and wasm_adder.wasm file."

define void @main() #0 {
entry:
  %0 = call i32 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i32 @__quantum__hybrid__add_one__body(i32 %0)
  ret void
}

declare i32 @__quantum__hybrid__add_one__body(i32)

declare i32 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

attributes #0 = { "EntryPoint" "requiredQubits"="0" "requiredResults"="128" }
