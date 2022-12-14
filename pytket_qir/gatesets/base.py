from dataclasses import dataclass
from enum import Enum
from string import Template
from typing import Callable, Dict, List, NamedTuple, Set, Union

from pyqir.generator.types import Double, Int, Qubit, Result, Void  # type: ignore
from pytket import OpType  # type: ignore


PyQirParameterType = Union[Double, Int, Qubit, Result]
PyQirReturnType = Union[Int, Result, Void]


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
    function_signature: List[PyQirParameterType]
    return_type: PyQirReturnType


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
