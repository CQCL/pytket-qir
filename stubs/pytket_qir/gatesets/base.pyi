from _typeshed import Incomplete
from enum import Enum
from pyqir.generator.types import Double, Integer, Qubit, Result, Void
from typing import Union

PyQirInputTypes = Union[Double, Qubit, Result]
PyQirOutputTypes = Union[Integer, Result, Void]

class OpNat(Enum):
    QIS: str
    CIS: str

class OpName(Enum):
    H: str
    X: str
    Y: str
    Z: str
    S: str
    T: str
    RESET: str
    CNOT: str
    CX: str
    CZ: str
    MEASURE: str
    MEASUREZ: str
    Rx: str
    Ry: str
    Rz: str
    PHASEDX: str
    ZZPHASE: str
    ZZMAX: str
    AND: str
    OR: str
    XOR: str

class OpSpec(Enum):
    BODY: str
    ADJ: str
    CTL: str
    CTLADJ: str

QirGate: Incomplete
CustomQirGate: Incomplete
GateSet: Incomplete
CustomGateSet: Incomplete
