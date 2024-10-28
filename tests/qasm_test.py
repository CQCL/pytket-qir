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

from utilities import run_qir_gen_and_check  # type: ignore

from pytket.qasm import circuit_from_qasm_str


def test_pytket_qir_qasm() -> None:
    with open("qasm/qec.qasm") as my_file:
        circ = circuit_from_qasm_str(my_file.read())

    run_qir_gen_and_check(circ, "test_pytket_qir_qasm")


if __name__ == "__main__":
    test_pytket_qir_qasm()
