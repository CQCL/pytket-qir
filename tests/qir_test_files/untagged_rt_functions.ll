; ModuleID = 'untag_examples.bc'
source_filename = "RTCircuit"

%Qubit = type opaque
%Result = type opaque


declare void @__quantum__qis__y__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__x__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

declare void @__quantum__rt__result_record_output(%Result*) local_unnamed_addr

declare void @__quantum__rt__tuple_start_record_output() local_unnamed_addr

declare void @__quantum__rt__tuple_end_record_output() local_unnamed_addr

declare void @__quantum__rt__integer_record_output(i64) local_unnamed_addr

declare void @__quantum__rt__bool_record_output(i1) local_unnamed_addr

define void @Quantinuum__EntangledState() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  call void @__quantum__qis__reset__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__rt__result_record_output(%Result* null)
  call void @__quantum__rt__result_record_output(%Result* nonnull inttoptr (i64 1 to %Result*))
  %0 = add i64 1, 2 ; 3
  call void @__quantum__rt__integer_record_output(i64 %0)
  %1 = xor i1 1, 1 ; 0
  call void @__quantum__rt__bool_record_output(i1 %1)
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="2" }
