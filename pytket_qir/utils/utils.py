from enum import Enum


class QIRFormat(Enum):
    IR: str = "ir"
    BITCODE: str = "bitcode"


class CommandUnsupportedError(Exception):
    pass
