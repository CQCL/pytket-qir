source_filename = "Generated from input pytket circuit"

%Result = type opaque
%Qubit = type opaque

declare void @__quantum__rt__result__record_output(%Result*)

define void @main() #0 {
entry:
  call void @__quantum__qis__rz__body(double 3.500000e+00, %Qubit* null)
  call void @__quantum__qis__rx__body(double 2.500000e+00, %Qubit* null)
  call void @__quantum__qis__rz__body(double 2.500000e-01, %Qubit* null)
  call void @__quantum__qis__rz__body(double 3.500000e+00, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 3.500000e+00, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 2.500000e-01, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 1.000000e+00, %Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 2 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rz__body(double 2.500000e-01, %Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rz__body(double 2.500000e-01, %Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rz__body(double 3.750000e+00, %Qubit* null)
  call void @__quantum__qis__rx__body(double 1.000000e+00, %Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 5.000000e-01, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 3.750000e+00, %Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__rx__body(double 1.000000e+00, %Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 2 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__rz__body(double 2.500000e-01, %Qubit* null)
  call void @__quantum__qis__rx__body(double 2.500000e+00, %Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  call void @__quantum__qis__rx__body(double 5.000000e-01, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__rt__result__record_output(%Result* null)
  call void @__quantum__qis__mz__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Result* inttoptr (i64 1 to %Result*))
  call void @__quantum__rt__result__record_output(%Result* inttoptr (i64 1 to %Result*))
  ret void
}

declare void @__quantum__qis__rz__body(double, %Qubit*)

declare void @__quantum__qis__rx__body(double, %Qubit*)

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="3" "requiredResults"="2" }
