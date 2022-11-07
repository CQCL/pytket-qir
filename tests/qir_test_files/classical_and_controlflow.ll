; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

declare i1 @__quantum__qir__read_result(%Result*)

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

define void @classical_and_controlflow() local_unnamed_addr #0 {
entry:
  %0 = add i64 1, 2 ; 3
  %1 = add i64 %0, 3 ; 6
  %2 = sub i64 4, 2 ; 2
  %3 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %3, label %then, label %continue

then:                                     ; preds = %entry
  %4 = add i64 %2, 1 ; 3
  %5 = add i64 %4, %1 ; 9
  %6 = sub i64 %1, %5 ; 3
  tail call void @__quantum__qis__z__body(%Qubit* null)
  br label %continue

continue:                                   ; preds = %then0__1.i.i, %entry
  %7 = sub i64 %1, %2 ; 3
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 1 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %8 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="2" }
