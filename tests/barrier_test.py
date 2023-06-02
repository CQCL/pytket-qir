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

from pytket.circuit import (
    Circuit,
)


def test_pytket_qir_barrier() -> None:
    # test barrier handling

    circ = Circuit(5)
    circ.H(0)
    circ.add_barrier([0, 1])
    circ.H(1)
    circ.add_barrier([0])
    circ.H(1)
    circ.add_barrier([0, 1, 3, 4])
    circ.H(4)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_barrier", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_barrier")


def test_pytket_qir_barrier_ii() -> None:
    # test barrier handling

    circ = Circuit(5)
    circ.H(0)
    circ.add_barrier([0, 1], data="order2")
    circ.add_barrier([0, 1, 4], data="order3")
    circ.H(1)
    circ.add_barrier([0, 1], data="group2")
    circ.add_barrier([0, 1, 4], data="group3")
    circ.H(1)
    circ.add_barrier([1], data="sleep(5.1)")
    circ.add_barrier([0], data="sleep(10000)")

    result = pytket_to_qir(
        circ, name="test_pytket_qir_barrier_ii", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_barrier_ii")


if __name__ == "__main__":
    test_pytket_qir_barrier()
    test_pytket_qir_barrier_ii()
