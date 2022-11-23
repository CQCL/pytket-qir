; ModuleID = './teleportchain_baseprofile.bc'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque
%Array = type opaque
%String = type opaque

define void @TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__Interop() local_unnamed_addr #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %0, label %then, label %continue

then:                                   ; preds = %entry
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %continue

continue:                                ; preds = %then, %entry
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  %1 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %1, label %then1, label %TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i

then1:                                   ; preds = %continue__1.i.i.i
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i

TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i: ; preds = %then0__2.i.i.i, %continue__1.i.i.i
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Result* nonnull inttoptr (i64 2 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  %2 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %2, label %then2, label %continue2

then2:                                  ; preds = %TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  br label %continue2

continue2:                               ; preds = %then0__1.i.i1.i, %TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Result* nonnull inttoptr (i64 3 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  %3 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %3, label %then3, label %TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__body.1.exit

then3:                                  ; preds = %continue__1.i.i2.i
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  br label %TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__body.1.exit

TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__body.1.exit: ; preds = %then0__2.i.i3.i, %continue__1.i.i2.i
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 4 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 5 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  ret void
}

declare %Result* @__quantum__qis__m__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__x__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

declare i1 @__quantum__qis__read_result__body(%Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="6" "requiredResults"="6" }
