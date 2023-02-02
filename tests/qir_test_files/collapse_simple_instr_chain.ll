; ModuleID = './one_conditional.bc'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__Interop() local_unnamed_addr #0 {
entry:
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue1

continue1:
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue2

continue2:
  call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue3

continue3: ; preds = %then0__2.i.i.i, %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue4

continue4:
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue5

continue5:
  call void @__quantum__qis__h__body(%Qubit* null)
  br label %continue6

continue6:
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__z__body(%Qubit* null)
  br label %continue7

continue7:
  call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %continue8

continue8:
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %exit1

exit1:
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %exit2

exit2:
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  ret void
}

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__y__body(%Qubit*) local_unnamed_addr

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__x__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__rz__body(double, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__ry__body(double, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="5" "requiredResults"="13" }
