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


import pyqir
import pytest
from utilities import check_qir_result  # type: ignore

from pytket.circuit import Bit, Circuit
from pytket.passes import FlattenRelabelRegistersPass
from pytket.qir.conversion.api import (
    QIRFormat,
    check_circuit,
    pytket_to_qir,
)


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


def test_pytket_api_creg_2() -> None:
    circ = Circuit(3)

    circ.add_bit(Bit("c2", 3))
    circ.add_bit(Bit("c2", 1))

    circ.H(0, condition=Bit("c2", 1))

    with pytest.raises(ValueError):
        pytket_to_qir(circ)


def test_pytket_api_creg_3() -> None:
    circ = Circuit(3)

    circ.add_bit(Bit("c2", 3))
    circ.add_bit(Bit("c2", 1))

    circ.H(0, condition=Bit("c2", 1))

    with pytest.raises(ValueError):
        check_circuit(circ)


def test_pytket_api_creg_4() -> None:
    circ = Circuit(3)

    circ.add_bit(Bit("c2", 0))
    circ.add_bit(Bit("c2", 1))
    circ.add_bit(Bit("c2", 2))
    circ.add_bit(Bit("c2", 3))

    circ.H(0, condition=Bit("c2", 2))
    check_circuit(circ)

    FlattenRelabelRegistersPass("q").apply(circ)

    check_circuit(circ)


def test_pytket_api_creg_5() -> None:
    circ = Circuit(3)

    circ.add_bit(Bit("c2", 1))
    circ.add_bit(Bit("c2", 2))
    circ.add_bit(Bit("c2", 3))

    circ.H(0, condition=Bit("c2", 2))
    with pytest.raises(ValueError):
        check_circuit(circ)

    circ.add_bit(Bit("c2", 0))

    FlattenRelabelRegistersPass("q").apply(circ)

    check_circuit(circ)


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
