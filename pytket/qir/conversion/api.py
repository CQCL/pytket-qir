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

from enum import Enum
from typing import Union

from pytket.circuit import Circuit

from .conversion import QirGenerator
from .module import tketqirModule


class ReturnTypeQIR(Enum):
    """Return types qir, options are BINARY for a binary
    output and STRING for a string output
    """

    BINARY = 0
    STRING = 1


def pytket_to_qir(
    circ: Circuit,
    name: str = "Generated from input pytket circuit",
    returntype: ReturnTypeQIR = ReturnTypeQIR.BINARY,
) -> Union[str, bytes, None]:
    """converts given pytket circuit to qir
    :param circ: given circuit
    :type circ: pytket circuit
    :param name: name for the qir module created
    :type name: str
    :param returntype: format of the generated qir, defaut value is binary
    :type returntype: ReturnTypeQIR
    """

    if len(circ.q_registers) > 1:
        raise ValueError(
            """The circuit that should be converted should only have one
            quantum register, you can convert it with using the pytket
              compilerpass `FlattenRelabelRegistersPass`"""
        )

    for creg in circ.c_registers:
        if creg.size > 64:
            raise ValueError(
                "each of the classical register must not have more than 64 bits"
            )

    m = tketqirModule(
        name=name,
        num_qubits=circ.n_qubits,
        num_results=circ.n_qubits,
    )

    qir_generator = QirGenerator(
        circuit=circ,
        module=m,
        wasm_int_type=32,
        qir_int_type=64,
    )

    populated_module = qir_generator.circuit_to_module(
        qir_generator.circuit, qir_generator.module, True
    )
    if returntype == ReturnTypeQIR.BINARY:
        return populated_module.module.bitcode()
    elif returntype == ReturnTypeQIR.STRING:
        return populated_module.module.ir()
    else:
        raise ValueError("unsupported return type")
