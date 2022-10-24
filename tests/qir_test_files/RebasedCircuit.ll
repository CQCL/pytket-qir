; ModuleID = 'Generated from input pytket circuit'
source_filename = "Generated from input pytket circuit"

%Qubit = type opaque

define void @main() #0 {
entry:
  call void @__quantum__qis__rz__body(double 3.500000e+00, %Qubit* null)
  call void @__quantum__qis__rz__body(double 3.500000e+00, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 5.000000e-01, %Qubit* null)
  call void @__quantum__qis__rx__body(double 5.000000e-01, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 1.500000e+00, %Qubit* null)
  call void @__quantum__qis__rx__body(double 5.000000e-01, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 1.500000e+00, %Qubit* null)
  call void @__quantum__qis__rx__body(double 1.500000e+00, %Qubit* null)
  call void @__quantum__qis__rz__body(double 5.000000e-01, %Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rx__body(double 5.000000e-01, %Qubit* null)
  call void @__quantum__qis__rz__body(double 5.000000e-01, %Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__rz__body(double 5.000000e-01, %Qubit* null)
  call void @__quantum__qis__rz__body(double 3.500000e+00, %Qubit* null)
  call void @__quantum__qis__rx__body(double 5.000000e-01, %Qubit* null)
  ret void
}

declare void @__quantum__qis__rz__body(double, %Qubit*)

declare void @__quantum__qis__rx__body(double, %Qubit*)

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="0" }
