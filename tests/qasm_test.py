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
from utilities import run_qir_gen_and_check  # type: ignore

from pytket.qasm import circuit_from_qasm_str
from pytket.qir.conversion.api import QIRProfile


def test_pytket_qir_qasm() -> None:
    with open("qasm/qec.qasm") as my_file:
        circ = circuit_from_qasm_str(my_file.read())

    run_qir_gen_and_check(circ, "test_pytket_qir_qasm")


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_pytket_qir_qasm_classical_0(profile: QIRProfile) -> None:
    with open("qasm/test0.qasm") as my_file:
        circ = circuit_from_qasm_str(my_file.read())

    run_qir_gen_and_check(
        circ,
        "test_pytket_qir_qasm_classical_0",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_pytket_qir_qasm_classical_1(profile: QIRProfile) -> None:
    with open("qasm/test1.qasm") as my_file:
        circ = circuit_from_qasm_str(my_file.read())

    run_qir_gen_and_check(
        circ,
        "test_pytket_qir_qasm_classical_1",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_bitreg_as_bit_1(profile: QIRProfile) -> None:
    # https://github.com/CQCL/tket/issues/1896
    qasm = """OPENQASM 2.0;
include "hqslib1.inc";
creg a[1];
creg b[2];
a = a ^ b[0];
"""
    circ = circuit_from_qasm_str(qasm)
    run_qir_gen_and_check(
        circ,
        "test_bitreg_as_bit_1",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_bitreg_as_bit_2(profile: QIRProfile) -> None:
    # https://github.com/CQCL/tket/issues/1896
    qasm = """OPENQASM 2.0;
include "hqslib1.inc";
creg a[1];
creg b[2];
a = a[0] ^ b[0];
"""
    circ = circuit_from_qasm_str(qasm)
    run_qir_gen_and_check(
        circ,
        "test_bitreg_as_bit_2",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_bitreg_as_bit_3(profile: QIRProfile) -> None:
    # https://github.com/CQCL/tket/issues/1896
    qasm = """OPENQASM 2.0;
include "hqslib1.inc";
creg a[1];
creg b[2];
a[0] = a[0] ^ b[0];
"""
    circ = circuit_from_qasm_str(qasm)
    run_qir_gen_and_check(
        circ,
        "test_bitreg_as_bit_3",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_bitreg_as_bit_4(profile: QIRProfile) -> None:
    # https://github.com/CQCL/tket/issues/1896
    qasm = """OPENQASM 2.0;
include "hqslib1.inc";
creg a[1];
creg b[2];
a[0] = a ^ b[0];
"""
    circ = circuit_from_qasm_str(qasm)
    run_qir_gen_and_check(
        circ,
        "test_bitreg_as_bit_4",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_bitreg_as_bit_5(profile: QIRProfile) -> None:
    # https://github.com/CQCL/tket/issues/1896
    qasm = """OPENQASM 2.0;
include "hqslib1.inc";
creg a[1];
creg b[2];
a = a + b[0];
"""
    circ = circuit_from_qasm_str(qasm)
    run_qir_gen_and_check(
        circ,
        "test_bitreg_as_bit_5",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_bitreg_as_bit_6(profile: QIRProfile) -> None:
    # https://github.com/CQCL/tket/issues/1896
    qasm = """OPENQASM 2.0;
include "hqslib1.inc";
creg a[1];
creg b[2];
a = a[0] + b[0];
"""
    circ = circuit_from_qasm_str(qasm)
    run_qir_gen_and_check(
        circ,
        "test_bitreg_as_bit_6",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_bitreg_as_bit_7(profile: QIRProfile) -> None:
    # https://github.com/CQCL/tket/issues/1896
    qasm = """OPENQASM 2.0;
include "hqslib1.inc";
creg a[1];
creg b[2];
a[0] = a[0] + b[0];
"""
    circ = circuit_from_qasm_str(qasm)
    run_qir_gen_and_check(
        circ,
        "test_bitreg_as_bit_7",
        profile=profile,
    )


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.AZUREADAPTIVE,
        QIRProfile.PYTKET,
    ],
)
def test_bitreg_as_bit_8(profile: QIRProfile) -> None:
    # https://github.com/CQCL/tket/issues/1896
    qasm = """OPENQASM 2.0;
include "hqslib1.inc";
creg a[1];
creg b[2];
a[0] = a + b[0];
"""
    circ = circuit_from_qasm_str(qasm)
    run_qir_gen_and_check(
        circ,
        "test_bitreg_as_bit_8",
        profile=profile,
    )


if __name__ == "__main__":
    test_pytket_qir_qasm()
