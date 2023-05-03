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

from pytket.extensions.qir import pytket_to_qir

from pytket.circuit import Circuit


def test_pytket_qir() -> None:
    circ = Circuit(3)
    circ.H(0)
    pytket_to_qir(circ)


def test_pytket_qir_ii() -> None:
    circ = Circuit(3)
    circ.H(0)
    print(pytket_to_qir(circ))
