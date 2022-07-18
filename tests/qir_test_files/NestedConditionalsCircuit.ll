; ModuleID = 'NestedConditionalsCircuit'
source_filename = "NestedConditionalsCircuit"

%Qubit = type opaque
%Result = type opaque

declare void @__quantum__qis__z__body(%Qubit*)

declare void @__quantum__qis__y__body(%Qubit*)

declare void @__quantum__qis__x__body(%Qubit*)

define void @main() #0 {
entry:
  call void @__quantum__qis__x__body(%Qubit* null)
  call void @__quantum__qis__x__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  %equal = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %equal, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__y__body(%Qubit* null)
  call void @__quantum__qis__y__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  %equal1 = call i1 @__quantum__qis__read_result__body(%Result* inttoptr (i64 1 to %Result*))
  br i1 %equal1, label %then2, label %else3

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %continue4
  ret void

then2:                                            ; preds = %then
  br label %continue4

else3:                                            ; preds = %then
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__z__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  br label %continue4

continue4:                                        ; preds = %else3, %then2
  br label %continue
}

declare i1 @__quantum__qis__read_result__body(%Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="2" }
