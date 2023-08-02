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
from pytket.qasm import circuit_to_qasm_str # type: ignore

from pytket.circuit import (
    Circuit,
    reg_eq,
    reg_neq,
    reg_lt,
    reg_gt,
    reg_leq,
    reg_geq,
)


def get_circ() -> Circuit:

    circ = Circuit()
    q = circ.add_q_register("q", 2)
    a = circ.add_c_register("a", 2)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 7)
    circ.H(q[0])
    circ.CX(q[0], q[1])
    circ.Measure(q[0], a[0])
    circ.Measure(q[1], a[1])
    circ.add_c_setbits([True, False, False] + [True] * 4, list(c))
    circ.add_classicalexpbox_register(c - b, c, condition=a[0])
    circ.add_classicalexpbox_register(c - a, b, condition=a[1])
    circ.add_classicalexpbox_register(c - b, a)

    return circ
    

def test_example() -> None:

    circ = get_circ()
    
    print(circ)

    for g in circ:
        print(g)

    # assert 1 == 2

def test_example_qir() -> None:

    circ = get_circ()

    result = pytket_to_qir(
        circ, name="test_example_qir", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_example_qir")


def test_example_qasm() -> None:

    circ = get_circ()

    result = circuit_to_qasm_str(
        circ, header="hqslib1"
    )

    check_qir_result(result, "test_example_qasm")


if __name__ == "__main__":
    test_example()
