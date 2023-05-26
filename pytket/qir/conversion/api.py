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

import pyqir

from pytket.circuit import Circuit

from .conversion import QirGenerator
from .module import tketqirModule


class QIRFormat(Enum):
    """Return types qir, options are BINARY for a binary
    output and STRING for a string output
    """

    BINARY = 0
    STRING = 1


def pytket_to_qir(
    circ: Circuit,
    name: str = "Generated from input pytket circuit",
    qir_format: QIRFormat = QIRFormat.BINARY,
    pyqir_0_7_compatibility: bool = False,
) -> Union[str, bytes, None]:
    """converts given pytket circuit to qir

    :param circ: given circuit
    :type circ: pytket circuit
    :param name: name for the qir module created
    :type name: str
    :param qir_format: format of the generated qir, default value is binary
    :type qir_format: QIRFormat
    :param pyqir_0_7_compatibility: converts the output to be compatible with
        pyqir 0.7, default value false
    :type pyqir_0_7_compatibility: bool
    """

    if len(circ.q_registers) > 1 or circ.q_registers[0].name != "q":
        raise ValueError(
            """The circuit that should be converted should only have the default
            quantum register. You can convert it using the pytket
            compiler pass `FlattenRelabelRegistersPass`."""
        )

    for creg in circ.c_registers:
        if creg.size > 64:
            raise ValueError("classical registers must not have more than 64 bits")

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

    if pyqir_0_7_compatibility:

        initial_result = str(populated_module.module.ir())  # type: ignore

        result = initial_result.replace("entry_point", "EntryPoint").replace("num_required_qubits", "requiredQubits").replace("num_required_results", "requiredResults")  # type: ignore

        bitcode = pyqir.Module.from_ir(pyqir.Context(), result).bitcode  # type: ignore

        if qir_format == QIRFormat.BINARY:
            return bitcode  # type: ignore
        elif qir_format == QIRFormat.STRING:
            return result  # type: ignore
        else:
            assert not "unsupported return type"

    else:
        if qir_format == QIRFormat.BINARY:
            return populated_module.module.bitcode()
        elif qir_format == QIRFormat.STRING:
            return populated_module.module.ir()
        else:
            assert not "unsupported return type"
