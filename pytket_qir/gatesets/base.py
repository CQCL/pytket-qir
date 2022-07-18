from enum import Enum
from string import Template
from typing import Callable, Dict, List, NamedTuple, Union

from pyqir.generator.types import Double, Integer, Qubit, Result, Void  # type: ignore


PyQirInputTypes = Union[Double, Qubit, Result]
PyQirOutputTypes = Union[Integer, Result, Void]


class OpNat(Enum):
    QIS = "qis"
    CIS = "cis"


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


class OpSpec(Enum):
    BODY = "body"
    ADJ = "adj"
    CTL = "ctl"
    CTLADJ = "ctladj"


QirGate = NamedTuple(
    "QirGate",
    [
        (
            "opnat",
            OpNat,
        ),
        (
            "opname",
            OpName,
        ),
        (
            "opspec",
            OpSpec,
        ),
    ],
)


CustomQirGate = NamedTuple(
    "CustomQirGate",
    [
        (
            "opnat",
            OpNat,
        ),
        (
            "opname",
            OpName,
        ),
        (
            "opspec",
            OpSpec,
        ),
        (
            "function_signature",
            List[PyQirInputTypes],
        ),
        (
            "return_type",
            PyQirOutputTypes,
        ),
    ],
)


GateSet = NamedTuple(
    "GateSet",
    [
        ("name", str),
        ("tk_to_gateset", Callable),
        ("gateset_to_tk", Callable),
    ],
)


CustomGateSet = NamedTuple(
    "CustomGateSet",
    [
        ("name", str),
        ("template", Template),
        ("gateset", Dict[str, CustomQirGate]),
        ("tk_to_gateset", Callable),
        ("gateset_to_tk", Callable),
    ],
)
