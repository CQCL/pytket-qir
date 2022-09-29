from dataclasses import dataclass


@dataclass
class WasmInt:
    """Int type definition for WASM functions."""

    size: int
    """Number of bits used to represent the integer."""


WASMI32: WasmInt = WasmInt(32)
WASMI64: WasmInt = WasmInt(64)
