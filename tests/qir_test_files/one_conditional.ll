; ModuleID = './one_conditional.bc'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__Interop() local_unnamed_addr #0 {
entry:
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Result* nonnull inttoptr (i64 2 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Result* nonnull inttoptr (i64 3 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %0, label %then0__2.i.i.i, label %Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit

then0__2.i.i.i:                                   ; preds = %entry
  call void @__quantum__qis__reset__body(%Qubit* null)
  call void @__quantum__qis__ry__body(double 0x3FEE91F42805715E, %Qubit* null)
  call void @__quantum__qis__rz__body(double 0xC015FDBBE9BBA775, %Qubit* null)
  call void @__quantum__qis__ry__body(double 0x3FEE91F42805715E, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0xC015FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__ry__body(double 0x3FEE91F42805715E, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0xC015FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__ry__body(double 0x3FEE91F42805715E, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0xC015FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__ry__body(double 0x3FEE91F42805715E, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__rz__body(double 0xC015FDBBE9BBA775, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 8 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 9 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Result* nonnull inttoptr (i64 10 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Result* nonnull inttoptr (i64 11 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit

Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit: ; preds = %then0__2.i.i.i, %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__y__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 12 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* null)
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
