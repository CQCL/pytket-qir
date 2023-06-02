# Copyright 2020-2023 Cambridge Quantum Computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from utilities import check_qir_result  # type: ignore

from pytket.qir.conversion.api import pytket_to_qir, QIRFormat
from pytket.circuit import Circuit  # type: ignore


def test_pytket_qir_quantum() -> None:
    circ = Circuit(1)
    circ.H(0)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_quantum", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_quantum")


def test_pytket_qir_quantum_ii() -> None:
    circ = Circuit(4, 4)
    circ.H(0)
    circ.X(0)
    circ.Y(0)
    circ.Z(0)
    circ.Rx(0.5, 0)
    circ.CX(1, 2)
    circ.CX(1, 3)
    circ.H(1)
    circ.Measure(1, 1)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_quantum", qir_format=QIRFormat.STRING
    )

    assert "call void @__quantum__qis__mz__body" in str(result)
    assert "call void @__quantum__qis__h__body" in str(result)
    assert "call void @__quantum__qis__cnot__body" in str(result)
    assert "call void @__quantum__qis__rx__body" in str(result)


def test_pytket_qir_quantum_iii() -> None:
    circ = Circuit(2).H(0).CX(0, 1).measure_all()

    result = pytket_to_qir(
        circ, name="test_pytket_qir_quantum", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_quantum_iii")


def test_pytket_qir_quantum_iv() -> None:
    circ = Circuit(4, 4)
    circ.H(0)
    circ.X(0)
    circ.Y(0)
    circ.Z(0)
    circ.Rx(0.5, 0)
    circ.ZZPhase(0.5, 0, 1)
    circ.PhasedX(0.5, 0.4, 1)
    circ.ZZMax(0, 1)

    circ.CX(1, 2)
    circ.CX(1, 3)
    circ.H(1)
    circ.Measure(1, 1)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_quantum_iv", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_quantum_iv")


if __name__ == "__main__":
    test_pytket_qir_quantum()
    test_pytket_qir_quantum_ii()
    test_pytket_qir_quantum_iii()
