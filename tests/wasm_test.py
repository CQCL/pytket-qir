# Copyright 2020-2024 Cambridge Quantum Computing
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

from pytket import wasm
from pytket.circuit import Circuit
from pytket.qir.conversion.api import QIRFormat, pytket_to_qir


def test_pytket_qir_wasm() -> None:
    w = wasm.WasmFileHandler("testfile.wasm")
    circ = Circuit(1)
    circ.H(0)

    result = pytket_to_qir(
        circ,
        name="test_pytket_qir_wasm",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=32,
    )

    check_qir_result(result, "test_pytket_qir_wasm")


def test_pytket_qir_wasm_ii() -> None:
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
        name="test_pytket_qir_wasm_ii",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=32,
    )

    check_qir_result(result, "test_pytket_qir_wasm_ii")


def test_pytket_qir_wasm_ii_64() -> None:
    w = wasm.WasmFileHandler("testfile.wasm", int_size=64)
    c = Circuit(6, 6)
    c0 = c.add_c_register("c0", 3)
    c1 = c.add_c_register("c1", 4)
    c.add_wasm_to_reg("add_something", w, [c0], [c1])
    c.add_wasm_to_reg("add_something", w, [c1], [c1])
    result = pytket_to_qir(
        c,
        name="test_pytket_qir_wasm_ii_64",
        qir_format=QIRFormat.STRING,
        wfh=w,
        int_type=64,
    )

    check_qir_result(result, "test_pytket_qir_wasm_ii_64")


if __name__ == "__main__":
    test_pytket_qir_wasm()
