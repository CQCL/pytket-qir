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

from pytket import wasm
from pytket.circuit import Bit, Circuit, Qubit
from pytket.qir.conversion.api import QIRFormat, QIRProfile, pytket_to_qir


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_wasm(profile: QIRProfile) -> None:
    w = wasm.WasmFileHandler("testfile.wasm")
    circ = Circuit(1)
    circ.H(0)

    result = pytket_to_qir(
        circ,
        name=f"test_pytket_qir_wasm-{profile}",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=32,
        profile=profile,
    )

    check_qir_result(result, f"test_pytket_qir_wasm-{profile}")


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_wasm_2(profile: QIRProfile) -> None:
    w = wasm.WasmFileHandler("testfile.wasm")
    c = Circuit(6, 6)
    c0 = c.add_c_register("c0", 3)
    c1 = c.add_c_register("c1", 4)
    c2 = c.add_c_register("c2", 5)
    c.add_wasm_to_reg("multi", w, [c0, c1], [c2])
    c.add_wasm_to_reg("add_one", w, [c2], [c2])
    c.add_wasm_to_reg("no_return", w, [c2], [])
    c.add_wasm_to_reg("init", w, [], [])
    c.add_wasm_to_reg("no_parameters", w, [], [c2])
    result = pytket_to_qir(
        c,
        name=f"test_pytket_qir_wasm_2-{profile}",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=32,
        profile=profile,
    )

    check_qir_result(result, f"test_pytket_qir_wasm_2-{profile}")


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_wasm_3(profile: QIRProfile) -> None:
    w = wasm.WasmFileHandler("testfile.wasm", int_size=64)
    c = Circuit(6, 6)
    c0 = c.add_c_register("c0", 3)
    c1 = c.add_c_register("c1", 4)
    c.add_wasm_to_reg("add_something", w, [c0], [c1])
    c.add_wasm_to_reg("add_something", w, [c1], [c1])
    result = pytket_to_qir(
        c,
        name=f"test_pytket_qir_wasm_3-{profile}",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=64,
        profile=profile,
    )

    check_qir_result(result, f"test_pytket_qir_wasm_3-{profile}")


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_wasm_4(profile: QIRProfile) -> None:
    w = wasm.WasmFileHandler("testfile.wasm", int_size=64)
    c = Circuit(6, 6)
    c.Measure(Qubit(0), Bit(0))
    c.Measure(Qubit(1), Bit(1))
    c.Measure(Qubit(2), Bit(2))
    c0 = c.add_c_register("c0", 3)
    c1 = c.add_c_register("c1", 4)
    c.add_wasm_to_reg("add_something", w, [c0], [c1])
    c.add_wasm_to_reg("add_something", w, [c1], [c1])
    result = pytket_to_qir(
        c,
        name=f"test_pytket_qir_wasm_4-{profile}",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=64,
        profile=profile,
    )

    check_qir_result(result, f"test_pytket_qir_wasm_4-{profile}")


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_wasm_5(profile: QIRProfile) -> None:
    w = wasm.WasmFileHandler("testfile.wasm", int_size=32, check_file=False)
    c = Circuit(6, 6)
    c.Measure(Qubit(0), Bit(0))
    c.Measure(Qubit(1), Bit(1))
    c.Measure(Qubit(2), Bit(2))
    c0 = c.add_c_register("c0", 64)
    c1 = c.add_c_register("c1", 32)
    c.add_c_setbits([True] + [False] * 63, list(c0))
    c.add_wasm_to_reg("add_one", w, [c0], [c1])

    w.check()

    result = pytket_to_qir(
        c,
        name=f"test_pytket_qir_wasm_5-{profile}",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=64,
        profile=profile,
    )

    check_qir_result(result, f"test_pytket_qir_wasm_5-{profile}")


@pytest.mark.parametrize(
    "profile",
    [
        QIRProfile.ADAPTIVE,
        QIRProfile.PYTKET,
        QIRProfile.ADAPTIVE_CREGSIZE,
    ],
)
def test_pytket_qir_wasm_6(profile: QIRProfile) -> None:
    w = wasm.WasmFileHandler("testfile.wasm", int_size=32, check_file=False)
    c = Circuit(6, 6)
    c.Measure(Qubit(0), Bit(0))
    c.Measure(Qubit(1), Bit(1))
    c.Measure(Qubit(2), Bit(2))
    c0 = c.add_c_register("c0", 64)
    c1 = c.add_c_register("c1", 32)
    c.add_c_setbits([False] * 30 + [True, True, True, True] + [False] * 30, list(c0))
    c.add_wasm_to_reg("add_one", w, [c0], [c1])

    w.check()

    result = pytket_to_qir(
        c,
        name=f"test_pytket_qir_wasm_6-{profile}",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=64,
        profile=profile,
    )

    check_qir_result(result, f"test_pytket_qir_wasm_6-{profile}")


if __name__ == "__main__":
    test_pytket_qir_wasm(QIRProfile.PYTKET)
    test_pytket_qir_wasm_2(QIRProfile.PYTKET)
    test_pytket_qir_wasm_3(QIRProfile.PYTKET)
    test_pytket_qir_wasm_4(QIRProfile.PYTKET)
