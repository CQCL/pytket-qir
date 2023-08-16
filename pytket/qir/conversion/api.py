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
from typing import Optional, Union

import pyqir

from pytket import wasm
from pytket._tket.circuit import _TEMP_BIT_NAME  # type: ignore
from pytket.circuit import Bit, Circuit  # type: ignore
from pytket.passes import CustomPass  # type: ignore

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
    wfh: Optional[wasm.WasmFileHandler] = None,
    int_type: int = 64,
    cut_pytket_register: bool = False,
) -> Union[str, bytes, None]:
    """converts given pytket circuit to qir

    :param circ: given circuit
    :type circ: pytket circuit
    :param name: name for the qir module created
    :type name: str
    :param qir_format: format of the generated qir, default value is binary
    :type qir_format: QIRFormat
    :param pyqir_0_6_compatibility: converts the output to be compatible with
        pyqir 0.6, default value false
    :type pyqir_0_6_compatibility: bool
    :param int_type: size of each integer, allowed value 32 and 64
    :type int_type: int
    :param cut_pytket_register: breaks up the internal scratch bit registers
      into smaller registers, default value false
    :type cut_pytket_register: bool
    """

    if len(circ.q_registers) > 1 or (
        len(circ.q_registers) == 1 and circ.q_registers[0].name != "q"
    ):
        raise ValueError(
            """The circuit that should be converted should only have the default
            quantum register. You can convert it using the pytket
            compiler pass `FlattenRelabelRegistersPass`."""
        )

    if int_type != 32 and int_type != 64:
        raise ValueError("the integer size must be 32 or 64")

    if cut_pytket_register:
        cpass = _scratch_reg_resize_pass(int_type)
        cpass.apply(circ)

    for creg in circ.c_registers:
        if creg.size > 64:
            raise ValueError("classical registers must not have more than 64 bits")

    m = tketqirModule(
        name=name,
        num_qubits=circ.n_qubits,
        num_results=circ.n_qubits,
    )

    qir_generator = QirGenerator(
        circuit=circ, module=m, wasm_int_type=int_type, qir_int_type=int_type, wfh=wfh
    )

    populated_module = qir_generator.circuit_to_module(
        qir_generator.circuit, qir_generator.module, True
    )

    if wfh is not None:
        wasm_sar_dict: dict[str, str] = qir_generator.get_wasm_sar()

        initial_result = str(populated_module.module.ir())  # type: ignore

        for wf in wasm_sar_dict:
            initial_result = initial_result.replace(wf, wasm_sar_dict[wf])

        result = initial_result

        bitcode = pyqir.Module.from_ir(pyqir.Context(), result).bitcode  # type: ignore

        if qir_format == QIRFormat.BINARY:
            return bitcode  # type: ignore
        elif qir_format == QIRFormat.STRING:
            return result  # type: ignore
        else:
            assert not "unsupported return type"  # type: ignore

    else:
        if qir_format == QIRFormat.BINARY:
            return populated_module.module.bitcode()
        elif qir_format == QIRFormat.STRING:
            return populated_module.module.ir()
        else:
            assert not "unsupported return type"  # type: ignore


def _scratch_reg_resize_pass(max_size: int) -> CustomPass:
    """Given a max scratch register width, return a compiler pass that
    breaks up the internal scratch bit registers into smaller registers
    """

    def trans(circ: Circuit, max_size: int = max_size) -> Circuit:
        # Find all scratch bits
        scratch_bits = [
            bit
            for bit in circ.bits
            if (
                bit.reg_name == _TEMP_BIT_NAME
                or bit.reg_name.startswith(f"{_TEMP_BIT_NAME}_")
            )
        ]
        # If the total number of scratch bits exceeds the max width, rename them
        if len(scratch_bits) > max_size:
            bits_map = {}
            for i, bit in enumerate(scratch_bits):
                bits_map[bit] = Bit(f"{_TEMP_BIT_NAME}_{i//max_size}", i % max_size)
            circ.rename_units(bits_map)
        return circ

    return CustomPass(trans, label="resize scratch bits")
