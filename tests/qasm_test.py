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

from utilities import check_qir_result  # type: ignore

from pytket.qasm import circuit_from_qasm, circuit_from_qasm_str
from pytket.qir.conversion.api import QIRFormat, pytket_to_qir


def test_pytket_qir_qasm() -> None:
    with open("qec.qasm") as my_file:
        circ = circuit_from_qasm_str(my_file.read())

    result = pytket_to_qir(
        circ,
        name="test_pytket_qir_qasm",
        qir_format=QIRFormat.STRING,
        cut_pytket_register=True,
    )

    check_qir_result(result, "test_pytket_qir_qasm")


def test_pytket_qir_qasm_ii() -> None:
    try:
        with open("qec_ii.qasm") as my_file:
            circ = circuit_from_qasm_str(my_file.read())

        result = pytket_to_qir(
            circ,
            name="test_pytket_qir_qasm_ii",
            qir_format=QIRFormat.STRING,
            cut_pytket_register=True,
        )

        check_qir_result(result, "test_pytket_qir_qasm_ii")
    except FileNotFoundError:
        with open("qec.qasm") as my_file:
            circ = circuit_from_qasm_str(my_file.read())
        result = pytket_to_qir(
            circ,
            name="test_pytket_qir_qasm",
            qir_format=QIRFormat.STRING,
            cut_pytket_register=True,
        )
        check_qir_result(result, "test_pytket_qir_qasm")


def test_pytket_qir_qasm_long() -> None:
    try:
        n = 7500

        newfile = ""
        with open("test_pytket_qir_qasm_long.qasm") as qfile:
            count = 0
            for line in qfile:
                count = count + 1
                if count < n:
                    newfile += line

        with open("test_pytket_qir_qasm_long_x.qasm", "w") as f:
            f.write(newfile)

        c = circuit_from_qasm("test_pytket_qir_qasm_long_x.qasm")

        result = pytket_to_qir(
            c,
            name="test_pytket_qir_qasm_long",
            qir_format=QIRFormat.STRING,
            cut_pytket_register=True,
            compile_circuit=True,
        )

        check_qir_result(result, "test_pytket_qir_qasm_long")
    except FileNotFoundError:
        with open("qec.qasm") as my_file:
            circ = circuit_from_qasm_str(my_file.read())
        result = pytket_to_qir(
            circ,
            name="test_pytket_qir_qasm",
            qir_format=QIRFormat.STRING,
            cut_pytket_register=True,
        )
        check_qir_result(result, "test_pytket_qir_qasm")


if __name__ == "__main__":
    test_pytket_qir_qasm()
    test_pytket_qir_qasm_ii()
    test_pytket_qir_qasm_long()
