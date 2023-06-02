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
from pytket.circuit import Circuit, Qubit, Bit, BitRegister  # type: ignore
from pytket.circuit.logic_exp import (  # type: ignore
    reg_eq,
    reg_neq,
    reg_geq,
    reg_gt,
    reg_lt,
    reg_leq,
)


def test_pytket_qir() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(circ, name="test_pytket_qir", qir_format=QIRFormat.STRING)

    check_qir_result(result, "test_pytket_qir")


def test_pytket_qir_2() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(circ, name="test_pytket_qir_2", qir_format=QIRFormat.STRING)

    check_qir_result(result, "test_pytket_qir_2")


def test_pytket_qir_3() -> None:
    circ = Circuit(3, 3)
    circ.H(0)
    circ.H(1)
    circ.H(2)

    result = pytket_to_qir(circ, name="test_pytket_qir_3", qir_format=QIRFormat.STRING)

    check_qir_result(result, "test_pytket_qir_3")


def test_pytket_qir_4() -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_classicalexpbox_register(a | b, c)
    circ.H(0)
    circ.H(0, condition=b[4])
    circ.H(0)

    result = pytket_to_qir(circ, name="test_pytket_qir_4", qir_format=QIRFormat.STRING)

    check_qir_result(result, "test_pytket_qir_4")


def test_pytket_qir_5() -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_c_register("d", 5)
    circ.add_classicalexpbox_register(a | b, c)
    circ.H(0)
    circ.H(0, condition=Bit(3))
    circ.H(0)

    result = pytket_to_qir(circ, name="test_pytket_qir_5", qir_format=QIRFormat.STRING)

    check_qir_result(result, "test_pytket_qir_5")

    assert circ.c_registers == [
        BitRegister("a", 5),
        BitRegister("b", 5),
        BitRegister("c", 5),
        BitRegister("d", 5),
    ]


def test_pytket_qir_6() -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_c_register("d", 5)
    circ.add_classicalexpbox_register(a | b, c)
    circ.H(2)
    circ.H(1)
    circ.X(0)
    circ.Measure(Qubit(0), c[4])
    circ.Z(0, condition=c[4])
    circ.H(0)

    assert circ.n_qubits == 3
    assert circ.n_bits == 20

    result = pytket_to_qir(circ, name="test_pytket_qir_6", qir_format=QIRFormat.STRING)

    check_qir_result(result, "test_pytket_qir_6")


def test_pytket_qir_7() -> None:
    # test calssical exp box handling
    circ = Circuit(2)
    a = circ.add_c_register("a", 3)
    b = circ.add_c_register("b", 3)
    c = circ.add_c_register("c", 3)
    d = circ.add_c_register("d", 3)
    circ.add_classicalexpbox_register(a & d, c)
    circ.add_classicalexpbox_register(a | b, c)
    circ.add_classicalexpbox_register(a ^ b, c)
    circ.add_classicalexpbox_register(a + b, c)
    circ.add_classicalexpbox_register(a - b, c)
    circ.add_classicalexpbox_register(a * b, c)
    # circ.add_classicalexpbox_register(a // b, c) No division yet.
    circ.add_classicalexpbox_register(a << b, c)
    circ.add_classicalexpbox_register(a >> b, c)
    circ.add_classicalexpbox_register(reg_eq(a, b), c)
    circ.add_classicalexpbox_register(reg_neq(a, b), c)
    circ.add_classicalexpbox_register(reg_gt(a, b), c)
    circ.add_classicalexpbox_register(reg_geq(a, b), c)
    circ.add_classicalexpbox_register(reg_lt(a, b), c)
    circ.add_classicalexpbox_register(reg_leq(a, b), c)

    assert circ.n_qubits == 2
    assert circ.n_bits == 12

    result = pytket_to_qir(circ, name="test_pytket_qir_7", qir_format=QIRFormat.STRING)

    check_qir_result(result, "test_pytket_qir_7")


if __name__ == "__main__":
    test_pytket_qir()
    test_pytket_qir_2()
    test_pytket_qir_3()
    test_pytket_qir_4()
    test_pytket_qir_5()
    test_pytket_qir_6()
    test_pytket_qir_7()
