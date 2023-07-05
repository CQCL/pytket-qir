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


import pytest

import pyqir

from utilities import check_qir_result  # type: ignore

from pytket.qir.conversion.api import (
    pytket_to_qir,
    QIRFormat,
)

from pytket.qir.conversion.apill import pytket_to_qir_ll

from pytket.circuit import Circuit  # type: ignore


def test_pytket_qir_BINARY() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(circ, name="test_pytket_qir", qir_format=QIRFormat.BINARY)

    assert type(result) == bytes


def test_pytket_qir() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(circ, name="test_pytket_qir", qir_format=QIRFormat.STRING)

    check_qir_result(result, "test_pytket_qir")


def test_pytket_qir_ll() -> None:
    circ = Circuit(1)

    result = pytket_to_qir(circ, name="test_pytket_qir_ll", qir_format=QIRFormat.STRING)
    result2 = pytket_to_qir_ll(circ, name="test_pytket_qir_ll")

    check_qir_result(result, "test_pytket_qir_ll")
    check_qir_result(result2, "test_pytket_qir_lll")


def test_pytket_qir_ll_2() -> None:
    circ = Circuit(1)
    circ.H(0)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_ll_2", qir_format=QIRFormat.STRING
    )
    result2 = pytket_to_qir_ll(circ, name="test_pytket_qir_ll_2")

    check_qir_result(result, "test_pytket_qir_ll_2")
    check_qir_result(result2, "test_pytket_qir_lll_2")


"""def test_pytket_qir_ll_3() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(
        circ, name="test_pytket_qir_ll_3", qir_format=QIRFormat.STRING
    )
    result2 = pytket_to_qir_ll(circ, name="test_pytket_qir_ll_3")

    check_qir_result(result, "test_pytket_qir_ll_3")
    check_qir_result(result2, "test_pytket_qir_ll_3")"""


def test_pytket_qir_optimised() -> None:
    circ = Circuit(
        3,
    )
    circ.H(0)

    result = pytket_to_qir(
        circ,
        name="test_pytket_qir",
        qir_format=QIRFormat.STRING,
        pyqir_0_6_compatibility=True,
    )

    check_qir_result(result, "test_pytket_qir_optimised")


def test_pytket_qir_optimised_ii() -> None:
    circ = Circuit(2).H(0).CX(0, 1).measure_all()

    result = pytket_to_qir(
        circ,
        name="test_pytket_qir",
        qir_format=QIRFormat.STRING,
        pyqir_0_6_compatibility=True,
    )

    check_qir_result(result, "test_pytket_qir_optimised_ii")


def test_pytket_api_qreg() -> None:
    circ = Circuit(3)
    circ.H(0)

    circ.add_q_register("q2", 3)

    with pytest.raises(ValueError):
        pytket_to_qir(circ)


def test_pytket_api_qreg_ii() -> None:
    circ = Circuit()

    circ.add_q_register("q2", 3)

    with pytest.raises(ValueError):
        pytket_to_qir(circ)


def test_pytket_api_creg() -> None:
    circ = Circuit(3)
    circ.H(0)

    circ.add_c_register("c2", 100)

    with pytest.raises(ValueError):
        pytket_to_qir(circ)


def test_pytket_qir_module() -> None:
    circ = Circuit(3)
    circ.H(0)

    result = pytket_to_qir(circ, name="test_pytket_qir", qir_format=QIRFormat.STRING)

    result_2 = pytket_to_qir(circ, name="test_pytket_qir")

    check_qir_result(result, "test_pytket_qir_module")

    bitcode = pyqir.Module.from_ir(pyqir.Context(), result).bitcode  # type: ignore

    assert bitcode == result_2


if __name__ == "__main__":
    test_pytket_qir_BINARY()
    test_pytket_qir()
    test_pytket_api_qreg()
