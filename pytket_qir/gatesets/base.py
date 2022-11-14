from dataclasses import dataclass
from enum import Enum
from string import Template
from typing import Callable, Dict, List, NamedTuple, Set, Union

from pyqir import Type  # type: ignore
from pytket import OpType  # type: ignore


class OpNat(Enum):
    QIS = "qis"
    CIS = "cis"
    HYBRID = "hybrid"
    RT = "rt"


class OpName(Enum):
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


class OpSpec(Enum):
    BODY = "body"
    ADJ = "adj"
    CTL = "ctl"
    CTLADJ = "ctladj"
    REC_OUT = "record_output"


@dataclass(frozen=True)
class QirGate:
    opnat: OpNat
    opname: Union[OpName, Enum]
    opspec: OpSpec


@dataclass(frozen=True)
class CustomQirGate(QirGate):
    function_signature: List[Type]
    return_type: Type


CustomGateSet = NamedTuple(
    "CustomGateSet",
    [
        ("name", str),
        ("template", Template),
        ("base_gateset", Set[OpType]),
        ("gateset", Dict[str, CustomQirGate]),
        ("tk_to_gateset", Callable),
        ("gateset_to_tk", Callable),
    ],
)
