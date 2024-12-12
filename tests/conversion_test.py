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
from utilities import run_qir_gen_and_check  # type: ignore

from pytket.circuit import Bit, BitRegister, Circuit, Qubit, if_not_bit
from pytket.circuit.logic_exp import (
    reg_eq,
    reg_geq,
    reg_gt,
    reg_leq,
    reg_lt,
    reg_neq,
)
from pytket.passes import FlattenRelabelRegistersPass
from pytket.qir.conversion.api import QIRFormat, QIRProfile, pytket_to_qir


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.BASE,
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir(profile: QIRProfile) -> None:
    circ = Circuit(3)
    circ.H(0)

    run_qir_gen_and_check(circ, "test_pytket_qir", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.BASE,
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_2(profile: QIRProfile) -> None:
    circ = Circuit(3)
    circ.H(0)

    run_qir_gen_and_check(circ, "test_pytket_qir_2", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.BASE,
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_3(profile: QIRProfile) -> None:
    circ = Circuit(3, 3)
    circ.H(0)
    circ.H(1)
    circ.H(2)

    run_qir_gen_and_check(circ, "test_pytket_qir_3", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_4(profile: QIRProfile) -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_classicalexpbox_register(a | b, c)  # type: ignore
    circ.H(0)
    circ.H(0, condition=b[4])
    circ.H(0)

    run_qir_gen_and_check(circ, "test_pytket_qir_4", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_5(profile: QIRProfile) -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_c_register("d", 5)
    circ.add_classicalexpbox_register(a | b, c)  # type: ignore
    circ.H(0)
    circ.H(0, condition=Bit(3))
    circ.H(0)

    run_qir_gen_and_check(circ, "test_pytket_qir_5", profile=profile)

    assert circ.c_registers == [
        BitRegister("a", 5),
        BitRegister("b", 5),
        BitRegister("c", 5),
        BitRegister("d", 5),
    ]


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_6(profile: QIRProfile) -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    circ.add_c_register("d", 5)
    circ.add_classicalexpbox_register(a | b, c)  # type: ignore
    circ.H(2)
    circ.H(1)
    circ.X(0)
    circ.Measure(Qubit(0), c[4])
    circ.Z(0, condition=c[4])
    circ.H(0)

    run_qir_gen_and_check(circ, "test_pytket_qir_6", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_7(profile: QIRProfile) -> None:
    # test calssical exp box handling
    circ = Circuit(2)
    a = circ.add_c_register("a", 3)
    b = circ.add_c_register("b", 3)
    c = circ.add_c_register("c", 3)
    d = circ.add_c_register("d", 3)
    circ.add_classicalexpbox_register(a & d, c)  # type: ignore
    circ.add_classicalexpbox_register(a | b, c)  # type: ignore
    circ.add_classicalexpbox_register(a ^ b, c)  # type: ignore
    circ.add_classicalexpbox_register(a + b, c)  # type: ignore
    circ.add_classicalexpbox_register(a - b, c)  # type: ignore
    circ.add_classicalexpbox_register(a * b, c)  # type: ignore
    # circ.add_classicalexpbox_register(a // b, c) No division yet.
    circ.add_classicalexpbox_register(a << b, c)  # type: ignore
    circ.add_classicalexpbox_register(a >> b, c)  # type: ignore
    circ.add_classicalexpbox_register(reg_eq(a, b), c)  # type: ignore
    circ.add_classicalexpbox_register(reg_neq(a, b), c)  # type: ignore
    circ.add_classicalexpbox_register(reg_gt(a, b), c)  # type: ignore
    circ.add_classicalexpbox_register(reg_geq(a, b), c)  # type: ignore
    circ.add_classicalexpbox_register(reg_lt(a, b), c)  # type: ignore
    circ.add_classicalexpbox_register(reg_leq(a, b), c)  # type: ignore

    run_qir_gen_and_check(circ, "test_pytket_qir_7", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_8(profile: QIRProfile) -> None:
    # test setbits op
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 8)

    c.add_c_setbits([True], [a[0]])
    c.add_c_setbits([True], [a[2]])
    c.add_c_setbits([True], [a[1]])
    c.add_c_setbits([True], [a[7]])
    c.add_c_setbits([False, True] + [False] * 6, list(a))

    run_qir_gen_and_check(c, "test_pytket_qir_8", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_9(profile: QIRProfile) -> None:
    # test copybits op
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 2)
    b = c.add_c_register("b", 2)

    c.add_c_copyreg(a, b)

    run_qir_gen_and_check(c, "test_pytket_qir_9", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_10(profile: QIRProfile) -> None:
    # test copybits op
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 4)
    b = c.add_c_register("b", 2)

    c.add_c_copyreg(a, b)

    run_qir_gen_and_check(c, "test_pytket_qir_10", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_11(profile: QIRProfile) -> None:
    # test copybits op
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 2)
    b = c.add_c_register("b", 4)

    c.add_c_copyreg(a, b)

    run_qir_gen_and_check(c, "test_pytket_qir_11", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_12(profile: QIRProfile) -> None:
    # test << and >> ops
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 8)

    c.add_classicalexpbox_register(a << 1, a)  # type: ignore

    run_qir_gen_and_check(c, "test_pytket_qir_12", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_13(profile: QIRProfile) -> None:
    # test << and >> ops
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 8)
    b = c.add_c_register("b", 8)

    c.add_classicalexpbox_register(a << 1, a)  # type: ignore
    c.add_classicalexpbox_register(a >> 3, b)  # type: ignore

    run_qir_gen_and_check(c, "test_pytket_qir_13", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_14(profile: QIRProfile) -> None:
    # test setbits op
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 8)
    b = c.add_c_register("b", 10)
    d = c.add_c_register("d", 10)

    c.add_c_setbits([True], [a[0]])
    c.add_c_setbits([False, True] + [False] * 6, list(a))
    c.add_c_setbits([True, True] + [False] * 8, list(b))

    c.add_c_setreg(23, a)
    c.add_c_copyreg(a, b)

    c.add_classicalexpbox_register(a + b, d)  # type: ignore
    c.add_classicalexpbox_register(a - b, d)  # type: ignore
    # c.add_classicalexpbox_register(a * b // d, d)
    c.add_classicalexpbox_register(a << 1, a)  # type: ignore
    c.add_classicalexpbox_register(a >> 1, b)  # type: ignore

    c.X(0, condition=reg_eq(a ^ b, 1))
    c.X(0, condition=(a[0] ^ b[0]))
    c.X(0, condition=reg_eq(a & b, 1))
    c.X(0, condition=reg_eq(a | b, 1))

    c.X(0, condition=a[0])
    c.X(0, condition=reg_neq(a, 1))
    c.X(0, condition=if_not_bit(a[0]))
    c.X(0, condition=reg_gt(a, 1))
    c.X(0, condition=reg_lt(a, 1))
    c.X(0, condition=reg_geq(a, 1))
    c.X(0, condition=reg_leq(a, 1))
    c.Phase(0, condition=a[0])

    run_qir_gen_and_check(c, "test_pytket_qir_14", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_15(profile: QIRProfile) -> None:
    # test setbits op
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 32)
    b = c.add_c_register("b", 32)
    d = c.add_c_register("d", 32)

    c.add_c_setbits([True], [a[0]])
    c.add_c_setbits([False, True] + [False] * 30, list(a))
    c.add_c_setbits([True, True] + [False] * 30, list(b))

    c.add_c_setreg(23, a)
    c.add_c_copyreg(a, b)

    c.add_classicalexpbox_register(a + b, d)  # type: ignore
    c.add_classicalexpbox_register(a - b, d)  # type: ignore
    # c.add_classicalexpbox_register(a * b // d, d)
    c.add_classicalexpbox_register(a << 1, a)  # type: ignore
    c.add_classicalexpbox_register(a >> 1, b)  # type: ignore

    c.X(0, condition=reg_eq(a ^ b, 1))
    c.X(0, condition=(a[0] ^ b[0]))
    c.X(0, condition=reg_eq(a & b, 1))
    c.X(0, condition=reg_eq(a | b, 1))

    c.X(0, condition=a[0])
    c.X(0, condition=reg_neq(a, 1))
    c.X(0, condition=if_not_bit(a[0]))
    c.X(0, condition=reg_gt(a, 1))
    c.X(0, condition=reg_lt(a, 1))
    c.X(0, condition=reg_geq(a, 1))
    c.X(0, condition=reg_leq(a, 1))
    c.Phase(0, condition=a[0])

    run_qir_gen_and_check(c, "test_pytket_qir_15", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_16(profile: QIRProfile) -> None:
    # test setbits op
    c = Circuit(1, name="test_classical")
    a = c.add_c_register("a", 10)
    b = c.add_c_register("b", 11)
    d = c.add_c_register("d", 20)

    c.Measure(Qubit(0), a[0])

    c.add_c_setbits([True, True] + [False] * 9, list(b))

    c.add_classicalexpbox_register(a + b, d)  # type: ignore

    run_qir_gen_and_check(c, "test_pytket_qir_16", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_17(profile: QIRProfile) -> None:
    # test calssical exp box handling
    # circuit to cover capabilities covered in example notebook
    c = Circuit(0, 1, name="test_classical")
    a = c.add_c_register("a", 8)
    c.add_c_setreg(32, a)

    run_qir_gen_and_check(c, "test_pytket_qir_17", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.BASE,
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_18(profile: QIRProfile) -> None:
    # try circuit with multi-circuit register
    c = Circuit()
    q1 = Qubit("q1", 0)
    q2 = Qubit("q2", 0)
    c1 = Bit("c1", 0)
    c2 = Bit("c2", 0)
    for q in (q1, q2):
        c.add_qubit(q)
    for cb in (c1, c2):
        c.add_bit(cb)
    c.H(q1)
    c.CX(q1, q2)
    c.Measure(q1, c1)
    c.Measure(q2, c2)

    with pytest.raises(ValueError):
        pytket_to_qir(
            c, name="ptest_pytket_qir_18", qir_format=QIRFormat.STRING, profile=profile
        )

    # gives:
    # E ValueError: The circuit that should be converted should only have the default
    # E             quantum register. You can convert it using the pytket
    # E             compiler pass `FlattenRelabelRegistersPass`.


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.BASE,
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_19(profile: QIRProfile) -> None:
    # try circuit with multi-circuit register
    c = Circuit()
    q1 = Qubit("q1", 0)
    q2 = Qubit("q2", 0)
    c1 = Bit("c1", 0)
    c2 = Bit("c2", 0)
    for q in (q1, q2):
        c.add_qubit(q)
    for cb in (c1, c2):
        c.add_bit(cb)
    c.H(q1)
    c.CX(q1, q2)
    c.Measure(q1, c1)
    c.Measure(q2, c2)

    FlattenRelabelRegistersPass().apply(c)

    run_qir_gen_and_check(c, "test_pytket_qir_19", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.BASE,
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_20(profile: QIRProfile) -> None:
    circ = Circuit(10, 10)
    for i in range(10):
        circ.H(i)
    circ.measure_all()

    run_qir_gen_and_check(circ, "test_pytket_qir_20", profile=profile)


if __name__ == "__main__":
    test_pytket_qir(QIRProfile.PYTKET)
    test_pytket_qir_2(QIRProfile.PYTKET)
    test_pytket_qir_3(QIRProfile.PYTKET)
    test_pytket_qir_4(QIRProfile.PYTKET)
    test_pytket_qir_5(QIRProfile.PYTKET)
    test_pytket_qir_6(QIRProfile.PYTKET)
    test_pytket_qir_7(QIRProfile.PYTKET)
    test_pytket_qir_8(QIRProfile.PYTKET)
    test_pytket_qir_9(QIRProfile.PYTKET)
    test_pytket_qir_10(QIRProfile.PYTKET)
    test_pytket_qir_11(QIRProfile.PYTKET)
    test_pytket_qir_12(QIRProfile.PYTKET)
    test_pytket_qir_13(QIRProfile.PYTKET)
    test_pytket_qir_14(QIRProfile.PYTKET)
    test_pytket_qir_15(QIRProfile.PYTKET)
    test_pytket_qir_16(QIRProfile.PYTKET)
    test_pytket_qir_17(QIRProfile.PYTKET)
    test_pytket_qir_18(QIRProfile.PYTKET)
    test_pytket_qir_19(QIRProfile.PYTKET)
    test_pytket_qir_20(QIRProfile.PYTKET)
