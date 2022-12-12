from enum import Enum


class QirFormat(Enum):
    IR: str = "ir"
    BITCODE: str = "bitcode"


class InstructionError(Exception):
    pass


class ClassicalExpBoxError(Exception):
    pass


class SetBitsOpError(Exception):
    pass


class WASMError(Exception):
    pass


class BarrierError(Exception):
    pass


class RtError(Exception):
    pass


class CircuitError(Exception):
    pass
