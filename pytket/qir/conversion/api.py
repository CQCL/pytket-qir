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

"""
public api for qir conversion from pytket
"""

from enum import Enum
from typing import Optional, Union

import pyqir

from pytket import wasm
from pytket.circuit import Bit, Circuit, UnitID
from pytket.passes import (
    CustomPass,
)
from pytket.unit_id import _TEMP_BIT_NAME

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
    :param name: name for the qir module created
    :param qir_format: format of the generated qir, default value is binary
    :param wfh: wasm file handler used when creating the circuit.
      Only needed when there are wasm calls in the circuit.
    :param int_type: size of each integer, allowed value 32 and 64
    :param cut_pytket_register: breaks up the internal scratch bit registers
      into smaller registers, default value false
    """

    if cut_pytket_register:
        cpass = _scratch_reg_resize_pass(int_type)
        cpass.apply(circ)  # type: ignore

    check_circuit(circ, int_type)

    m = tketqirModule(
        name=name,
        num_qubits=circ.n_qubits,
        num_results=circ.n_qubits,
    )

    qir_generator = QirGenerator(
        circuit=circ, module=m, wasm_int_type=int_type, qir_int_type=int_type, wfh=wfh
    )

    populated_module = qir_generator.circuit_to_module(qir_generator.circuit, True)

    if wfh is not None:
        wasm_sar_dict: dict[str, str] = qir_generator.get_wasm_sar()

        initial_result = str(populated_module.module.ir())

        for wf in wasm_sar_dict:
            initial_result = initial_result.replace(wf, wasm_sar_dict[wf])

        result = initial_result

        bitcode = pyqir.Module.from_ir(pyqir.Context(), result).bitcode

        if qir_format == QIRFormat.BINARY:
            return bitcode
        elif qir_format == QIRFormat.STRING:
            return result
        else:
            assert not "unsupported return type"  # type: ignore

    else:
        if qir_format == QIRFormat.BINARY:
            return populated_module.module.bitcode()
        elif qir_format == QIRFormat.STRING:
            return populated_module.module.ir()
        else:
            assert not "unsupported return type"  # type: ignore


def check_circuit(
    circuit: Circuit,
    int_type: int = 64,
) -> None:
    """Checks the validity of the circuit.

    Running this check before conversion is recommended for big circuits that
    take a long time to be converted.

    :param circuit: given circuit
    :param int_type: integer bit width (32 or 64)
    :raises ValueError: with a suggestion on how to resolve the problems
    """
    if len(circuit.q_registers) > 1 or (
        len(circuit.q_registers) == 1 and circuit.q_registers[0].name != "q"
    ):
        raise ValueError(
            """The circuit that should be converted should only have the default
            quantum register. You can convert it using the pytket
            compiler pass `FlattenRelabelRegistersPass`."""
        )

    if int_type != 32 and int_type != 64:
        raise ValueError("the integer size must be 32 or 64")

    for creg in circuit.c_registers:
        if creg.size > int_type:
            raise ValueError(
                f"""classical registers must not have more than {int_type} bits, \
you could try to set cut_pytket_register=True in the conversion"""
            )

    set_circ_register = set([creg.name for creg in circuit.c_registers])
    for b in set([b.reg_name for b in circuit.bits]):
        if b not in set_circ_register:
            raise ValueError(f"Used register {b} in not a valid register")


def _scratch_reg_resize_pass(max_size: int) -> CustomPass:  # type: ignore
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
            bits_map: dict[UnitID, UnitID] = {}
            for i, bit in enumerate(scratch_bits):
                bits_map[bit] = Bit(f"{_TEMP_BIT_NAME}_{i//max_size}", i % max_size)
            circ.rename_units(bits_map)
        return circ

    return CustomPass(trans, label="resize scratch bits")
