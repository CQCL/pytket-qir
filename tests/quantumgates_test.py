# Copyright Quantinuum
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

from utilities import run_qir_gen_and_check  # type: ignore

from pytket.circuit import Circuit


def test_pytket_qir_quantum() -> None:
    circ = Circuit(1)
    circ.H(0)

    run_qir_gen_and_check(circ, "test_pytket_qir_quantum")


def test_pytket_qir_quantum_2() -> None:
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

    run_qir_gen_and_check(circ, "test_pytket_qir_quantum_2")


def test_pytket_qir_quantum_3() -> None:
    circ = Circuit(2).H(0).CX(0, 1).measure_all()

    run_qir_gen_and_check(circ, "test_pytket_qir_quantum_3")


def test_pytket_qir_quantum_4() -> None:
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

    run_qir_gen_and_check(circ, "test_pytket_qir_quantum_4")


def test_pytket_qir_quantum_5() -> None:
    circ = Circuit(4, 4)
    circ.H(0)
    circ.X(0)
    circ.Y(0)
    circ.Z(0)
    circ.Rx(0.5, 0)
    circ.ZZPhase(0.5, 0, 1)
    circ.PhasedX(0.5, 0.4, 1)

    circ.TK2(0.5, 0.4, 0.3, 0, 1)
    circ.TK2(1.5, 1.4, 1.3, 2, 1)

    circ.CX(1, 2)
    circ.CX(1, 3)
    circ.H(1)
    circ.Measure(1, 1)

    run_qir_gen_and_check(circ, "test_pytket_qir_quantum_5")


if __name__ == "__main__":
    test_pytket_qir_quantum()
    test_pytket_qir_quantum_2()
    test_pytket_qir_quantum_3()
    test_pytket_qir_quantum_4()
    test_pytket_qir_quantum_5()
