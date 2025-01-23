# Copyright Quantinuum
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
from typing import TYPE_CHECKING, Union

import pyqir

from pytket.circuit import Circuit
from pytket.passes import (
    scratch_reg_resize_pass,
)

from .azurebaseprofileqirgenerator import AzureBaseProfileQirGenerator
from .azureprofileqirgenerator import AzureAdaptiveProfileQirGenerator
from .baseprofileqirgenerator import BaseProfileQirGenerator
from .module import tketqirModule
from .profileqirgenerator import AdaptiveProfileQirGenerator
from .pytketqirgenerator import PytketQirGenerator

if TYPE_CHECKING:
    from .qirgenerator import AbstractQirGenerator


class QIRFormat(Enum):
    """Return types qir, options are BINARY for a binary
    output and STRING for a string output
    """

    BINARY = 0
    STRING = 1


class QIRProfile(Enum):
    """Profile for the QIR generation"""

    BASE = 0
    AZUREBASE = 1
    ADAPTIVE = 2
    AZUREADAPTIVE = 3
    ADAPTIVE_CREGSIZE = 4
    PYTKET = 5


def pytket_to_qir(
    circ: Circuit,
    name: str = "Generated from input pytket circuit",
    qir_format: QIRFormat = QIRFormat.BINARY,
    int_type: int = 64,
    cut_pytket_register: bool = False,
    profile: QIRProfile = QIRProfile.PYTKET,
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
    :param profile: generates QIR corresponding to the selected profile:
        Use QIRProfile.BASE for the base profile, see:
        https://github.com/qir-alliance/qir-spec/blob/main/specification/under_development/profiles/Base_Profile.md
        Use QIRProfile.ADAPTIVE for the adaptive profile, see:
        https://github.com/qir-alliance/qir-spec/tree/main/specification/under_development/profiles/Adaptive_Profile.md
        Use QIRProfile.ADAPTIVE_CREGSIZE for the adaptive profile with additional
        truncation operation to assure that integers matching the classical
        registers have no unexpected set bits, see:
        https://github.com/qir-alliance/qir-spec/tree/main/specification/under_development/profiles/Adaptive_Profile.md
        Use QIRProfile.PYTKET for QIR with additonal function for classical registers.

    """

    if cut_pytket_register:
        cpass = scratch_reg_resize_pass(int_type)
        cpass.apply(circ)

    check_circuit(circ, int_type)

    m = tketqirModule(
        name=name,
        num_qubits=circ.n_qubits,
        num_results=circ.n_qubits,
    )

    trunc = False
    if profile == QIRProfile.ADAPTIVE_CREGSIZE:
        trunc = True

    if profile == QIRProfile.BASE:
        qir_generator: AbstractQirGenerator = BaseProfileQirGenerator(
            circuit=circ,
            module=m,
            wasm_int_type=int_type,
            qir_int_type=int_type,
        )
    elif profile == QIRProfile.AZUREBASE:
        qir_generator = AzureBaseProfileQirGenerator(
            circuit=circ,
            module=m,
            wasm_int_type=int_type,
            qir_int_type=int_type,
        )
    elif profile == QIRProfile.PYTKET:
        qir_generator = PytketQirGenerator(
            circuit=circ,
            module=m,
            wasm_int_type=int_type,
            qir_int_type=int_type,
        )
    elif profile == QIRProfile.ADAPTIVE or profile == QIRProfile.ADAPTIVE_CREGSIZE:
        qir_generator = AdaptiveProfileQirGenerator(
            circuit=circ,
            module=m,
            wasm_int_type=int_type,
            qir_int_type=int_type,
            trunc=trunc,
        )
    elif profile == QIRProfile.AZUREADAPTIVE:
        qir_generator = AzureAdaptiveProfileQirGenerator(
            circuit=circ,
            module=m,
            wasm_int_type=int_type,
            qir_int_type=int_type,
            trunc=trunc,
        )
    else:
        raise NotImplementedError("unexpected profile")

    populated_module = qir_generator.circuit_to_module(qir_generator.circuit, True)

    if profile == QIRProfile.AZUREADAPTIVE:

        assert not qir_generator.has_wasm

        sar_azure_dict: dict[str, str] = qir_generator.get_azure_sar()

        initial_result = str(populated_module.module.ir())

        for az in sar_azure_dict:
            initial_result = initial_result.replace(az, sar_azure_dict[az])

        result = initial_result

        bitcode = pyqir.Module.from_ir(pyqir.Context(), result).bitcode

        if qir_format == QIRFormat.BINARY:
            return bitcode
        elif qir_format == QIRFormat.STRING:
            return result
        else:
            assert not "unsupported return type"  # type: ignore

    elif qir_generator.has_wasm:
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
