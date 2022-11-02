from enum import Enum


class QIRFormat(Enum):
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
