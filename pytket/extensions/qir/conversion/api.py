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

"""
public api for qir conversion from pytket
"""

from pytket.circuit import Circuit

from .conversion import QirGenerator
from .module import Module


def pytket_to_qir(circ: Circuit) -> str:
    """converts give circ to qir string"""
    return str(circ)


def pytket_to_qir_2(circ: Circuit) -> str:
    """converts give circ to qir string"""

    m = Module(
        name="Generated from input pytket circuit",
        num_qubits=circ.n_qubits,
        num_results=circ.n_bits,
    )

    qir_generator = QirGenerator(
        circuit=circ,
        module=m,
        wasm_int_type=32,
        qir_int_type=64,
    )

    populated_module = qir_generator.circuit_to_module(
        qir_generator.circuit, qir_generator.module
    )

    return populated_module.module.ir()
