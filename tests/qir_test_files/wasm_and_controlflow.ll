; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

declare i1 @__quantum__qir__read_result(%Result*)

declare i32 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare i32 @__quantum__hybrid__add_one__body(i32)

define void @classical_and_controlflow() local_unnamed_addr #0 {
entry:
  %0 = call i32 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = add i64 3, 4
  %2 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %2, label %then, label %continue

then:                                     ; preds = %entry
  %3 = call i32 @__quantum__hybrid__add_one__body(i32 %0)
  br label %continue

continue:                                   ; preds = %then0__1.i.i, %entry
  %4 = add i64 %1, 2 ; 3
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="2" }
