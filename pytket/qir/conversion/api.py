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

from enum import Enum
from typing import TYPE_CHECKING

import pyqir
from pytket._tket.unit_id import _TEMP_BIT_REG_BASE
from pytket.circuit import Circuit, OpType
from pytket.passes import scratch_reg_resize_pass
from pytket.predicates import GateSetPredicate

from .azurebaseprofileqirgenerator import AzureBaseProfileQirGenerator
from .azureprofileqirgenerator import AzureAdaptiveProfileQirGenerator
from .baseprofileqirgenerator import BaseProfileQirGenerator
from .gatesets import PYQIR_FULL_GATESET
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


class ClassicalRegisterWidthError(Exception):
    """Error trying to convert a circuit with a classical register exceeding the maximum width"""

    def __init__(
        self, width: int, max_width: int = 64, hint: str | None = None
    ) -> None:
        self.width = width
        self.max_width = max_width
        self.hint = hint
        msg = (
            f"Classical register of width {width} exceeds maximum width ({max_width})."
        )
        if hint is not None:
            msg += f" Hint: {hint}."
        super().__init__(msg)


def pytket_to_qir(  # noqa: PLR0912, PLR0913, RET503
    circ: Circuit,
    name: str = "Generated from input pytket circuit",
    qir_format: QIRFormat = QIRFormat.BINARY,
    int_type: int = 64,
    cut_pytket_register: bool = False,
    profile: QIRProfile = QIRProfile.PYTKET,
) -> str | bytes | None:
    """Converts the given pytket :py:class:`~pytket._tket.circuit.Circuit` to qir

    :param circ: given circuit
    :param name: name for the qir module created
    :param qir_format: format of the generated qir, default value is binary
    :param wfh: wasm file handler used when creating the circuit.
      Only needed when there are wasm calls in the circuit.
    :param int_type: size of each integer, allowed value 32 and 64
    :param cut_pytket_register: breaks up the internal scratch bit registers
      into smaller registers, default value false
    :param profile: generates QIR corresponding to the selected profile:

      - Use ``QIRProfile.BASE`` for the base profile. See:
        https://github.com/qir-alliance/qir-spec/blob/main/specification/under_development/profiles/Base_Profile.md
      - Use ``QIRProfile.ADAPTIVE`` for the adaptive profile. See:
        https://github.com/qir-alliance/qir-spec/tree/main/specification/under_development/profiles/Adaptive_Profile.md
      - Use ``QIRProfile.ADAPTIVE_CREGSIZE`` for the adaptive profile with additional
        truncation operations to assure that integers matching the classical
        registers have no unexpected set bits. See:
        https://github.com/qir-alliance/qir-spec/tree/main/specification/under_development/profiles/Adaptive_Profile.md
      - Use ``QIRProfile.PYTKET`` for QIR with additional functions for classical
        registers.
      - Use ``QIRProfile.AZUREBASE`` for the base profile with metadata for Azure
        devices and ``array_record`` for output recording.
      - Use ``QIRProfile.AZUREADAPTIVE`` for the adaptive profile with metadata for
        Azure devices and bitwise recording of results via ``array_record``.
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
    elif profile in (QIRProfile.ADAPTIVE, QIRProfile.ADAPTIVE_CREGSIZE):
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

        for az, azv in sar_azure_dict.items():
            initial_result = initial_result.replace(az, azv)

        result = initial_result

        bitcode = pyqir.Module.from_ir(pyqir.Context(), result).bitcode

        if qir_format == QIRFormat.BINARY:
            return bitcode
        if qir_format == QIRFormat.STRING:
            return result
        assert not "unsupported return type"  # type: ignore

    elif qir_generator.has_wasm:
        wasm_sar_dict: dict[str, str] = qir_generator.get_wasm_sar()

        initial_result = str(populated_module.module.ir())

        for wf, wfv in wasm_sar_dict.items():
            initial_result = initial_result.replace(wf, wfv)

        result = initial_result

        bitcode = pyqir.Module.from_ir(pyqir.Context(), result).bitcode

        if qir_format == QIRFormat.BINARY:
            return bitcode
        if qir_format == QIRFormat.STRING:
            return result
        assert not "unsupported return type"  # type: ignore

    elif qir_format == QIRFormat.BINARY:
        return populated_module.module.bitcode()
    elif qir_format == QIRFormat.STRING:
        return populated_module.module.ir()
    else:
        assert not "unsupported return type"  # type: ignore


def check_circuit(
    circuit: Circuit,
    int_type: int = 64,
    gate_set: set[OpType] = PYQIR_FULL_GATESET.base_gateset,
) -> None:
    """Checks the validity of the circuit.

    Running this check before conversion is recommended for big circuits that
    take a long time to be converted.

    :param circuit: given circuit
    :param int_type: integer bit width (32 or 64)
    :param gate_set: set of OpTypes to use to check that all gates can be converted,
        the default value contains all gates which can be converted in any profile.
        See PYQIR_FULL_GATESET.base_gateset
    :raises ClassicalRegisterWidthError: for problems with classical register width
    :raises ValueError: for other circuit problems
    """
    if len(circuit.q_registers) > 1 or (
        len(circuit.q_registers) == 1 and circuit.q_registers[0].name != "q"
    ):
        raise ValueError(
            """The circuit that should be converted should only have the default
            quantum register. You can convert it using the pytket
            compiler pass `FlattenRelabelRegistersPass`.""",
        )

    if int_type not in {32, 64}:
        raise ValueError("the integer size must be 32 or 64")

    for creg in circuit.c_registers:
        if creg.size > int_type:
            hint: str | None = None
            if creg.name.startswith(_TEMP_BIT_REG_BASE):
                hint = "try setting `cut_pytket_register=True` when calling `pytket_to_qir()`"
            if int_type < 64 and creg.size <= 64:  # noqa: PLR2004
                hint = "try setting `int_type=64` when calling `pytket_to_qir()`"
            raise ClassicalRegisterWidthError(
                width=creg.size,
                max_width=int_type,
                hint=hint,
            )

    set_circ_register = {creg.name for creg in circuit.c_registers}
    for b in {b.reg_name for b in circuit.bits}:
        if b not in set_circ_register:
            raise ValueError(f"Used register {b} in not a valid register")

    gate_set_predicate = GateSetPredicate(gate_set)
    if not gate_set_predicate.verify(circuit):
        raise ValueError(
            f"Circuit contains gates that can't be converted to QIR. Supported gates: {gate_set}"
        )
