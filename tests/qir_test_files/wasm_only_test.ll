; ModuleID = './wasm_only_test.bc'
source_filename = "qat-link"


define void @test_wasm_op_integration() local_unnamed_addr #0 {
entry:
  %res = call i64 @__quantum__hybrid__add_one__body(i64 5)
  ret void
}

declare i64 @__quantum__hybrid__add_one__body(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="0" }
