# Copyright 2020-2024 Quantinuum
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

import pytest
from utilities import check_qir_result  # type: ignore

from pytket.circuit import (
    Bit,
    CircBox,
    Circuit,
    OpType,
    Qubit,
    if_not_bit,
    reg_eq,
)
from pytket.circuit.logic_exp import BitWiseOp, create_bit_logic_exp
from pytket.qir.conversion.api import QIRFormat, pytket_to_qir


def test_pytket_qir_conditional() -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    d = circ.add_c_register("d", 5)
    circ.H(0)
    circ.add_classicalexpbox_register(a | b, c)  # type: ignore
    circ.add_classicalexpbox_register(c | b, d)  # type: ignore
    circ.add_classicalexpbox_register(c | b, d, condition=a[4])  # type: ignore
    circ.H(0)
    circ.Measure(Qubit(0), d[4])
    circ.H(1)
    circ.Measure(Qubit(1), d[3])
    circ.H(2)
    circ.Measure(Qubit(2), d[2])

    result = pytket_to_qir(
        circ, name="ptest_pytket_qir_conditional", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional")


def test_pytket_qir_conditional_ii() -> None:
    # test conditional handling with else case

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    d = circ.add_c_register("d", 5)
    circ.H(0)
    circ.add_classicalexpbox_register(a | b, c)  # type: ignore
    circ.add_classicalexpbox_register(c | b, d)  # type: ignore
    circ.add_classicalexpbox_register(
        c | b, d, condition=if_not_bit(a[4])  # type: ignore
    )
    circ.H(0)
    circ.Measure(Qubit(0), d[4])
    circ.H(1)
    circ.Measure(Qubit(1), d[3])
    circ.H(2)
    circ.Measure(Qubit(2), d[2])

    result = pytket_to_qir(
        circ, name="ptest_pytket_qir_conditional_ii", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_ii")


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

    circ.add_classicalexpbox_register(a + b - d, c)  # type: ignore
    circ.add_classicalexpbox_register(a * b * d * c, e)  # type: ignore

    result = pytket_to_qir(
        circ, name="ptest_pytket_qir_conditional_iii", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_iii")


def test_pytket_qir_conditional_iv() -> None:
    # test complicated conditions and recursive classical op

    circ = Circuit(2, 2).H(0).H(1).measure_all()

    circ.add_gate(OpType.H, [0], condition_bits=[0, 1], condition_value=3)

    result = pytket_to_qir(
        circ, name="ptest_pytket_qir_conditional_iv", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_iv")


def test_pytket_qir_conditional_v() -> None:
    # test complicated conditions and recursive classical op

    circ = Circuit(2, 3).H(0).H(1).measure_all()

    circ.add_gate(OpType.H, [0], condition_bits=[0, 1, 2], condition_value=3)

    result = pytket_to_qir(
        circ, name="ptest_pytket_qir_conditional_v", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_v")


def test_pytket_qir_conditional_6() -> None:
    # test conditional for manual added gates

    circ = Circuit(2, 3).H(0).H(1)

    circ.add_gate(
        OpType.PhasedX, [0.1, 0.2], [0], condition_bits=[0, 1, 2], condition_value=3
    )

    result = pytket_to_qir(
        circ, name="ptest_pytket_qir_conditional_6", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_6")


def test_pytket_qir_conditional_7() -> None:
    circ = Circuit(7, name="testcirc")

    syn = circ.add_c_register("syn", 4)

    circ.X(0, condition=reg_eq(syn, 1))
    circ.X(0, condition=reg_eq(syn, 2))
    circ.X(0, condition=reg_eq(syn, 2))
    circ.X(0, condition=reg_eq(syn, 3))
    circ.X(0, condition=reg_eq(syn, 4))
    circ.X(0, condition=reg_eq(syn, 4))

    result = pytket_to_qir(
        circ, name="ptest_pytket_qir_conditional_7", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_7")


def test_pytket_qir_conditional_8() -> None:
    c = Circuit(4)
    c.H(0)
    c.H(1)
    c.H(2)
    c.H(3)
    cbox = CircBox(c)
    d = Circuit(4)
    a = d.add_c_register("a", 4)
    d.add_circbox(cbox, [0, 2, 1, 3], condition=a[0])

    result = pytket_to_qir(
        d, name="ptest_pytket_qir_conditional_8", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_8")


def test_pytket_qir_conditional_9() -> None:
    c = Circuit(4)
    c.X(0)
    c.Y(1)
    c.Z(2)
    c.H(3)
    cbox = CircBox(c)
    d = Circuit(4)
    a = d.add_c_register("a", 4)
    d.add_circbox(cbox, [0, 2, 1, 3], condition=a[0])

    result = pytket_to_qir(
        d, name="ptest_pytket_qir_conditional_9", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_9")


def test_pytket_qir_conditional_10() -> None:
    box_circ = Circuit(4)
    box_circ.X(0)
    box_circ.Y(1)
    box_circ.Z(2)
    box_circ.H(3)
    box_c = box_circ.add_c_register("c", 5)

    box_circ.H(0)
    box_circ.add_classicalexpbox_register(box_c | box_c, box_c)  # type: ignore

    cbox = CircBox(box_circ)
    d = Circuit(4, 5)
    a = d.add_c_register("a", 4)
    d.add_circbox(cbox, [0, 2, 1, 3, 0, 1, 2, 3, 4], condition=a[0])

    result = pytket_to_qir(
        d, name="ptest_pytket_qir_conditional_10", qir_format=QIRFormat.STRING, profile=True
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_10")


def test_pytket_qir_conditional_11() -> None:
    # test conditional with to big scratch register

    circ = Circuit(7, name="testcirc")

    syn = circ.add_c_register("syn", 4)

    for _ in range(11):
        circ.X(0, condition=reg_eq(syn, 1))
        circ.X(0, condition=reg_eq(syn, 2))
        circ.X(0, condition=reg_eq(syn, 2))
        circ.X(0, condition=reg_eq(syn, 3))
        circ.X(0, condition=reg_eq(syn, 4))
        circ.X(0, condition=reg_eq(syn, 4))

    with pytest.raises(Exception):
        pytket_to_qir(
            circ,
            name="ptest_pytket_qir_conditional_11",
            qir_format=QIRFormat.STRING,
            cut_pytket_register=False,
        )

    result = pytket_to_qir(
        circ,
        name="ptest_pytket_qir_conditional_11",
        qir_format=QIRFormat.STRING,
        cut_pytket_register=True,
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_11")


def test_pytket_qir_conditional_12() -> None:
    # test conditional with no register

    circ = Circuit(7, name="testcirc")

    exp = create_bit_logic_exp(BitWiseOp.ONE, [])
    circ.H(0, condition=exp)
    exp2 = create_bit_logic_exp(BitWiseOp.ZERO, [])
    circ.H(0, condition=exp2)

    result = pytket_to_qir(
        circ,
        name="ptest_pytket_qir_conditional_12",
        qir_format=QIRFormat.STRING,
    )

    check_qir_result(result, "ptest_pytket_qir_conditional_12")


if __name__ == "__main__":
    test_pytket_qir_conditional()
    test_pytket_qir_conditional_ii()
    test_pytket_qir_conditional_iii()
    test_pytket_qir_conditional_iv()
    test_pytket_qir_conditional_6()
    test_pytket_qir_conditional_7()
