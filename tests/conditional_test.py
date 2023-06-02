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

from utilities import check_qir_result

from pytket.qir.conversion.api import pytket_to_qir, QIRFormat

from pytket.circuit import Circuit, Qubit, if_not_bit, Bit, OpType  # type: ignore


def test_pytket_qir_conditional() -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    d = circ.add_c_register("d", 5)
    circ.H(0)
    circ.add_classicalexpbox_register(a | b, c)
    circ.add_classicalexpbox_register(c | b, d)
    circ.add_classicalexpbox_register(c | b, d, condition=a[4])
    circ.H(0)
    circ.Measure(Qubit(0), d[4])
    circ.H(1)
    circ.Measure(Qubit(1), d[3])
    circ.H(2)
    circ.Measure(Qubit(2), d[2])

    result = pytket_to_qir(
        circ, name="test_pytket_qir_conditional", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_conditional")


def test_pytket_qir_conditional_ii() -> None:
    # test conditional handling with else case

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    d = circ.add_c_register("d", 5)
    circ.H(0)
    circ.add_classicalexpbox_register(a | b, c)
    circ.add_classicalexpbox_register(c | b, d)
    circ.add_classicalexpbox_register(c | b, d, condition=if_not_bit(a[4]))
    circ.H(0)
    circ.Measure(Qubit(0), d[4])
    circ.H(1)
    circ.Measure(Qubit(1), d[3])
    circ.H(2)
    circ.Measure(Qubit(2), d[2])

    result = pytket_to_qir(
        circ, name="test_pytket_qir_conditional_ii", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_conditional_ii")


def test_pytket_qir_conditional_iii() -> None:
    # test complicated conditions and recursive classical op

    circ = Circuit(1)

    a = circ.add_c_register("a", 15)
    b = circ.add_c_register("b", 15)
    c = circ.add_c_register("c", 15)
    d = circ.add_c_register("d", 15)
    e = circ.add_c_register("e", 15)

    circ.H(0)
    bits = [Bit(i) for i in range(10)]
    big_exp = bits[4] | bits[5] ^ bits[6] | bits[7] & bits[8]
    circ.H(0, condition=big_exp)

    circ.add_classicalexpbox_register(a + b - d, c)
    circ.add_classicalexpbox_register(a * b * d * c, e)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_conditional_iii", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_conditional_iii")


def test_pytket_qir_conditional_iv() -> None:
    # test complicated conditions and recursive classical op

    circ = Circuit(2, 2).H(0).H(1).measure_all()

    circ.add_gate(OpType.H, [0], condition_bits=[0, 1], condition_value=3)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_conditional_iv", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_conditional_iv")


def test_pytket_qir_conditional_v() -> None:
    # test complicated conditions and recursive classical op

    circ = Circuit(2, 3).H(0).H(1).measure_all()

    circ.add_gate(OpType.H, [0], condition_bits=[0, 1, 2], condition_value=3)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_conditional_v", qir_format=QIRFormat.STRING
    )

    circ = Circuit(2, 2).H(0).H(1).measure_all()

    circ.add_gate(OpType.H, [0], condition_bits=[0, 1], condition_value=3)

    result_2 = pytket_to_qir(
        circ, name="test_pytket_qir_conditional_v", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_conditional_v")

    check_qir_result(result_2, "test_pytket_qir_conditional_v")


if __name__ == "__main__":
    test_pytket_qir_conditional()
    test_pytket_qir_conditional_ii()
    test_pytket_qir_conditional_iii()
    test_pytket_qir_conditional_iv()
