from enum import Enum
from string import Template
from typing import Callable, Dict, List, NamedTuple, Union

from pyqir.generator.types import Double, Integer, Qubit, Result, Void  # type: ignore


PyQirParameterTypes = Union[Double, Qubit, Result]
PyQirReturnTypes = Union[Integer, Result, Void]


class OpNat(Enum):
    QIS = "qis"
    CIS = "cis"
    HYBRID = "hybrid"


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
    WASM = "wasm"


class OpSpec(Enum):
    BODY = "body"
    ADJ = "adj"
    CTL = "ctl"
    CTLADJ = "ctladj"


qir_gate_base_fields = [
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
]


QirGate = NamedTuple(
    "QirGate",
    qir_gate_base_fields,
)


CustomQirGate = NamedTuple(
    "CustomQirGate",
    qir_gate_base_fields
    + [
        (
            "function_signature",
            List[PyQirParameterTypes],
        ),
        (
            "return_type",
            PyQirReturnTypes,
        ),
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
