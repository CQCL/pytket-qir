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

import pytest
from utilities import (  # type: ignore
    run_qir_gen_and_check,
)

from pytket.circuit import (
    Bit,
    CircBox,
    Circuit,
    OpType,
    Qubit,
    if_not_bit,
    reg_eq,
)
from pytket.circuit.clexpr import wired_clexpr_from_logic_exp
from pytket.circuit.logic_exp import BitNot, BitWiseOp, create_bit_logic_exp
from pytket.qir.conversion.api import (
    ClassicalRegisterWidthError,
    QIRFormat,
    QIRProfile,
    pytket_to_qir,
)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional(profile: QIRProfile) -> None:
    # test conditional handling

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    d = circ.add_c_register("d", 5)
    circ.H(0)
    circ.add_clexpr(*wired_clexpr_from_logic_exp(a | b, c))  # type: ignore
    circ.add_clexpr(*wired_clexpr_from_logic_exp(c | b, d))  # type: ignore
    circ.add_clexpr(*wired_clexpr_from_logic_exp(c | b, d), condition=a[4])  # type: ignore
    circ.H(0)
    circ.Measure(Qubit(0), d[4])
    circ.H(1)
    circ.Measure(Qubit(1), d[3])
    circ.H(2)
    circ.Measure(Qubit(2), d[2])

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_2(profile: QIRProfile) -> None:
    # test conditional handling with else case

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    b = circ.add_c_register("b", 5)
    c = circ.add_c_register("c", 5)
    d = circ.add_c_register("d", 5)
    circ.H(0)
    circ.add_clexpr(*wired_clexpr_from_logic_exp(a | b, c))  # type: ignore
    circ.add_clexpr(*wired_clexpr_from_logic_exp(c | b, d))  # type: ignore
    circ.add_clexpr(
        *wired_clexpr_from_logic_exp(c | b, d),  # type: ignore
        condition=if_not_bit(a[4]),
    )
    circ.H(0)
    circ.Measure(Qubit(0), d[4])
    circ.H(1)
    circ.Measure(Qubit(1), d[3])
    circ.H(2)
    circ.Measure(Qubit(2), d[2])

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional_2", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_3(profile: QIRProfile) -> None:
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

    circ.add_clexpr(*wired_clexpr_from_logic_exp(a + b - d, c))  # type: ignore
    circ.add_clexpr(*wired_clexpr_from_logic_exp(a * b * d * c, e))  # type: ignore

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional_3", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_4(profile: QIRProfile) -> None:
    # test complicated conditions and recursive classical op

    circ = Circuit(2, 2).H(0).H(1).measure_all()

    circ.add_gate(OpType.H, [0], condition_bits=[0, 1], condition_value=3)

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional_4", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_5(profile: QIRProfile) -> None:
    # test complicated conditions and recursive classical op

    circ = Circuit(2, 3).H(0).H(1).measure_all()

    circ.add_gate(OpType.H, [0], condition_bits=[0, 1, 2], condition_value=3)

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional_5", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_6(profile: QIRProfile) -> None:
    # test conditional for manual added gates

    circ = Circuit(2, 3).H(0).H(1)

    circ.add_gate(
        OpType.PhasedX,
        [0.1, 0.2],
        [0],
        condition_bits=[0, 1, 2],
        condition_value=3,
    )

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional_6", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_7(profile: QIRProfile) -> None:
    circ = Circuit(7, name="testcirc")

    syn = circ.add_c_register("syn", 4)

    circ.X(0, condition=reg_eq(syn, 1))
    circ.X(0, condition=reg_eq(syn, 2))
    circ.X(0, condition=reg_eq(syn, 2))
    circ.X(0, condition=reg_eq(syn, 3))
    circ.X(0, condition=reg_eq(syn, 4))
    circ.X(0, condition=reg_eq(syn, 4))

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional_7", profile=profile)


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
def test_pytket_qir_conditional_8(profile: QIRProfile) -> None:
    c = Circuit(4)
    c.H(0)
    c.H(1)
    c.H(2)
    c.H(3)
    cbox = CircBox(c)
    d = Circuit(4)
    a = d.add_c_register("a", 4)
    d.add_circbox(cbox, [0, 2, 1, 3], condition=a[0])

    run_qir_gen_and_check(c, "test_pytket_qir_conditional_8", profile=profile)


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
def test_pytket_qir_conditional_9(profile: QIRProfile) -> None:
    c = Circuit(4)
    c.X(0)
    c.Y(1)
    c.Z(2)
    c.H(3)
    cbox = CircBox(c)
    d = Circuit(4)
    a = d.add_c_register("a", 4)
    d.add_circbox(cbox, [0, 2, 1, 3], condition=a[0])

    run_qir_gen_and_check(c, "test_pytket_qir_conditional_9", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_10(profile: QIRProfile) -> None:
    box_circ = Circuit(4)
    box_circ.X(0)
    box_circ.Y(1)
    box_circ.Z(2)
    box_circ.H(3)
    box_c = box_circ.add_c_register("c", 5)

    box_circ.H(0)
    box_circ.add_clexpr(*wired_clexpr_from_logic_exp(box_c | box_c, box_c))  # type: ignore

    cbox = CircBox(box_circ)
    d = Circuit(4, 5)
    a = d.add_c_register("a", 4)
    d.add_circbox(cbox, [0, 2, 1, 3, 0, 1, 2, 3, 4], condition=a[0])

    run_qir_gen_and_check(d, "test_pytket_qir_conditional_10", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_11(profile: QIRProfile) -> None:
    box_circ = Circuit(4)
    box_circ.X(0)
    box_circ.Y(1)
    box_circ.Z(2)
    box_circ.H(3)
    box_c = box_circ.add_c_register("c", 5)

    box_circ.H(0)
    box_circ.add_clexpr(*wired_clexpr_from_logic_exp(box_c | box_c, box_c))  # type: ignore
    box_circ.add_clexpr(*wired_clexpr_from_logic_exp(box_c | box_c, box_c))  # type: ignore
    box_circ.add_c_setbits([False, True] + [False] * 3, list(box_c))

    cbox = CircBox(box_circ)
    d = Circuit(4, 5)
    a = d.add_c_register("a", 4)
    d.add_circbox(cbox, [0, 2, 1, 3, 0, 1, 2, 3, 4], condition=a[0])

    run_qir_gen_and_check(d, "test_pytket_qir_conditional_11", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_12(profile: QIRProfile) -> None:
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

    with pytest.raises(ClassicalRegisterWidthError):
        pytket_to_qir(
            circ,
            name="ptest_pytket_qir_conditional_12",
            qir_format=QIRFormat.STRING,
            cut_pytket_register=False,
        )

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional_12", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_13(profile: QIRProfile) -> None:
    # test conditional with no register

    circ = Circuit(7, name="testcirc")

    exp = create_bit_logic_exp(BitWiseOp.ONE, [])
    circ.H(0, condition=exp)
    exp2 = create_bit_logic_exp(BitWiseOp.ZERO, [])
    circ.H(0, condition=exp2)

    run_qir_gen_and_check(circ, "test_pytket_qir_conditional_13", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_14(profile: QIRProfile) -> None:
    box_circ = Circuit(4)
    box_circ.X(0)
    box_c = box_circ.add_c_register("c", 5)

    box_circ.add_clexpr(*wired_clexpr_from_logic_exp(box_c | box_c, box_c))  # type: ignore
    box_circ.add_clexpr(*wired_clexpr_from_logic_exp(box_c | box_c, box_c))  # type: ignore
    box_circ.add_c_setbits([False, True] + [False] * 3, list(box_c))

    cbox = CircBox(box_circ)
    d = Circuit(4, 5)
    a = d.add_c_register("a", 4)
    d.add_circbox(cbox, [0, 2, 1, 3, 0, 1, 2, 3, 4], condition=a[0])

    run_qir_gen_and_check(d, "test_pytket_qir_conditional_14-block", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_15(profile: QIRProfile) -> None:
    # test setbits op
    c = Circuit(1, name="ptest_classical")
    a = c.add_c_register("a", 10)
    b = c.add_c_register("b", 11)
    d = c.add_c_register("d", 20)

    c.Measure(Qubit(0), a[0])

    c.add_c_setbits([True, True] + [False] * 9, list(b))

    c.add_clexpr(*wired_clexpr_from_logic_exp(a + b, d))  # type: ignore

    run_qir_gen_and_check(c, "test_pytket_qir_conditional_15-block", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_16(profile: QIRProfile) -> None:
    # test setbits op
    c = Circuit(1, name="ptest_classical")
    a = c.add_c_register("a", 10)
    b = c.add_c_register("b", 11)
    d = c.add_c_register("d", 20)

    c.Measure(Qubit(0), a[0])

    c.add_c_setbits([True, True] + [False] * 9, list(b), condition=a[0])

    c.add_c_setbits([True, True] + [False] * 9, list(b), condition=a[0])

    c.add_clexpr(*wired_clexpr_from_logic_exp(a + b, d), condition=a[0])  # type: ignore

    run_qir_gen_and_check(c, "test_pytket_qir_conditional_16-block", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_17(profile: QIRProfile) -> None:
    # test setbits op
    c = Circuit(1, name="ptest_classical")
    a = c.add_c_register("a", 1)
    b = c.add_c_register("b", 10)
    d = c.add_c_register("d", 20)

    c.Measure(Qubit(0), a[0])
    for i in range(10):
        c.Measure(Qubit(0), b[i], condition=a[0])

    for i in range(20):
        c.Measure(Qubit(0), d[i], condition=a[0])

    c.add_c_setbits([True, True] + [False] * 8, list(b), condition=a[0])

    c.add_c_setbits([True, True] + [False] * 8, list(b), condition=a[0])

    c.add_clexpr(*wired_clexpr_from_logic_exp(a + b, d), condition=a[0])  # type: ignore

    run_qir_gen_and_check(c, "test_pytket_qir_conditional_17-block", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_18(profile: QIRProfile) -> None:
    c = Circuit(1, 1, name="ptest_classical")
    c.H(0, condition=BitNot(c.bits[0]))
    run_qir_gen_and_check(c, "test_pytket_qir_conditional_18", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_19(profile: QIRProfile) -> None:
    c = Circuit(1, 2, name="ptest_classical")

    c.H(0)
    c.Measure(Qubit(0), Bit(0))
    c.add_clexpr(*wired_clexpr_from_logic_exp(BitNot(c.bits[0]), [c.bits[1]]))

    run_qir_gen_and_check(c, "test_pytket_qir_conditional_19", profile=profile)


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_conditional_20(profile: QIRProfile) -> None:
    # test setbits op
    c = Circuit(1, name="ptest_classical")
    a = c.add_c_register("a", 32)

    c.add_c_setbits([False] * 22 + [True, True] + [False] * 8, list(a))

    run_qir_gen_and_check(c, "test_pytket_qir_conditional_20", profile=profile)


if __name__ == "__main__":
    test_pytket_qir_conditional(QIRProfile.PYTKET)
