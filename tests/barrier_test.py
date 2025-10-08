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

    run_qir_gen_and_check(circ, "test_pytket_qir_barrier")


def test_pytket_qir_barrier_2() -> None:
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

    run_qir_gen_and_check(circ, "test_pytket_qir_barrier_2")


def test_pytket_qir_barrier_3() -> None:
    # test barrier handling

    circ = Circuit(5)
    circ.H(0)
    circ.H(1)
    circ.H(1)
    circ.add_barrier([1], data="something")
    circ.add_barrier([0], data="nothing")
    circ.H(0)
    circ.H(1)

    run_qir_gen_and_check(circ, "test_pytket_qir_barrier_3")



if __name__ == "__main__":
    test_pytket_qir_barrier()
    test_pytket_qir_barrier_2()
