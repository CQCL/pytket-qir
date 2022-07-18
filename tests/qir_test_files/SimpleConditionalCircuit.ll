; ModuleID = 'SimpleConditionalCircuit'
source_filename = "SimpleConditionalCircuit"

%Qubit = type opaque
%Result = type opaque

declare void @__quantum__qis__y__body(%Qubit*)

declare void @__quantum__qis__z__body(%Qubit*)

declare void @__quantum__qis__x__body(%Qubit*)

declare void @__quantum__qis__h__body(%Qubit*)

define void @main() #0 {
entry:
  call void @__quantum__qis__x__body(%Qubit* null)
  call void @__quantum__qis__x__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  %equal = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %equal, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  call void @__quantum__qis__y__body(%Qubit* null)
  call void @__quantum__qis__y__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  %equal1 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  br i1 %equal1, label %then2, label %else3

then2:                                            ; preds = %continue
  br label %continue4

else3:                                            ; preds = %continue
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  br label %continue4

continue4:                                        ; preds = %else3, %then2
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__z__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="2" }
