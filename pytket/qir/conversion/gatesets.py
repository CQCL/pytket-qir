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


from dataclasses import dataclass
from enum import Enum
from string import Template
from typing import Any, Callable, NamedTuple, Union

from pytket import OpType  # type: ignore

# PyQirParameterType = any  # Union[Double, Int, Qubit, Result] # todo
# PyQirReturnType = any  # Union[Int, Result, Void] # todo


class FuncNat(Enum):
    QIS = "qis"
    CIS = "cis"
    HYBRID = "hybrid"
    RT = "rt"


class FuncName(Enum):
    H = "h"
    X = "x"
    Y = "y"
    Z = "z"
    S = "s"
    T = "t"
    RESET = "reset"
    CNOT = "cnot"
    CX = "cx"
    CZ = "cz"
    MEASURE = "m"
    MEASUREZ = "mz"
    Rx = "rx"
    Ry = "ry"
    Rz = "rz"
    PHASEDX = "u1q"
    ZZPHASE = "rzz"
    ZZMAX = "zz"
    AND = "and"
    OR = "or"
    XOR = "xor"
    INT = "integer"
    BOOL = "bool"
    RES = "result"
    READ_RES = "read_result"


class FuncSpec(Enum):
    BODY = "body"
    ADJ = "adj"
    CTL = "ctl"
    CTLADJ = "ctladj"
    REC_OUT = "record_output"


@dataclass(frozen=True)
class QirGate:
    func_nat: FuncNat
    func_name: Union[FuncName, Enum]
    func_spec: FuncSpec


@dataclass(frozen=True)
class CustomQirGate(QirGate):
    function_signature: list
    return_type: Any


class CustomGateSet(NamedTuple):
    name: str
    template: Template
    base_gateset: set[OpType]
    gateset: dict[str, CustomQirGate]
    tk_to_gateset: Callable


_TK_TO_PYQIR = {
    OpType.H: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.H, func_spec=FuncSpec.BODY
    ),
    OpType.X: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.X, func_spec=FuncSpec.BODY
    ),
    OpType.Y: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Y, func_spec=FuncSpec.BODY
    ),
    OpType.Z: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Z, func_spec=FuncSpec.BODY
    ),
    OpType.S: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.S, func_spec=FuncSpec.BODY
    ),
    OpType.Sdg: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.S, func_spec=FuncSpec.ADJ
    ),
    OpType.T: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.T, func_spec=FuncSpec.BODY
    ),
    OpType.Tdg: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.T, func_spec=FuncSpec.ADJ
    ),
    OpType.Reset: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.RESET, func_spec=FuncSpec.BODY
    ),
    OpType.CX: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.CX, func_spec=FuncSpec.BODY
    ),
    OpType.CZ: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.CZ, func_spec=FuncSpec.BODY
    ),
    OpType.Measure: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.MEASUREZ, func_spec=FuncSpec.BODY
    ),
    OpType.Rx: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Rx, func_spec=FuncSpec.BODY
    ),
    OpType.Ry: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Ry, func_spec=FuncSpec.BODY
    ),
    OpType.Rz: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Rz, func_spec=FuncSpec.BODY
    ),
    OpType.CopyBits: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.READ_RES, func_spec=FuncSpec.BODY
    ),
}


PYQIR_GATES = CustomGateSet(
    name="PyQir",
    template=Template("__quantum__${func_nat}__${func_name}__${func_spec}"),
    base_gateset=set(_TK_TO_PYQIR.keys()),
    gateset={},
    tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
)
