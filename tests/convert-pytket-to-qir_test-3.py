from collections import OrderedDict
from functools import partial
import os
from pathlib import Path
from string import Template
from typing import cast, Callable, Generator, List, Tuple

from pytest import fixture  # type: ignore

from pyqir.generator import bitcode_to_ir, types  # type: ignore
from pyqir.generator import Builder, IntPredicate, Value  # type: ignore
from pytket import Circuit  # type: ignore
from pytket.circuit import CircBox, OpType, Bit  # type: ignore
from pytket.circuit.logic_exp import (  # type: ignore
    BitNot,
    if_bit,
    if_not_bit,
    reg_eq,
    reg_neq,
    reg_geq,
    reg_gt,
    reg_lt,
    reg_leq,
)

from pytket_qir.converter import Block, circuit_to_qir, write_qir_file  # type: ignore

from pytket_qir.gatesets.base import FuncName, FuncNat, FuncSpec  # type: ignore

from pytket_qir.gatesets.base import CustomGateSet, CustomQirGate
from pytket_qir.gatesets.pyqir import _TK_TO_PYQIR
from pytket_qir.generator import QirGenerator
from pytket_qir.module import Module


from pytket.circuit import Circuit

circ = Circuit(2)
a = circ.add_c_register("a", 3)
b = circ.add_c_register("b", 3)
c = circ.add_c_register("c", 3)
circ.add_classicalexpbox_register(a & b, c)
circ.add_classicalexpbox_register(a | b, c)
circ.add_classicalexpbox_register(a ^ b, c)
circ.add_classicalexpbox_register(a + b, c)
circ.add_classicalexpbox_register(a - b, c)
circ.add_classicalexpbox_register(a * b, c)
# circ.add_classicalexpbox_register(a // b, c) No division yet.
circ.add_classicalexpbox_register(a << b, c)
circ.add_classicalexpbox_register(a >> b, c)
circ.add_classicalexpbox_register(reg_eq(a, b), c)
circ.add_classicalexpbox_register(reg_neq(a, b), c)
circ.add_classicalexpbox_register(reg_gt(a, b), c)
circ.add_classicalexpbox_register(reg_geq(a, b), c)
circ.add_classicalexpbox_register(reg_lt(a, b), c)
circ.add_classicalexpbox_register(reg_leq(a, b), c)

assert circ.n_qubits == 2
assert circ.n_bits == 9

module = Module(
    name="Generated from input pytket circuit",
    num_qubits=circ.n_qubits,
    num_results=circ.n_bits,
)
wasm_int_type = types.Int(32)
qir_int_type = types.Int(32)
qir_generator = QirGenerator(
    circuit=circ,
    module=module,
    wasm_int_type=wasm_int_type,
    qir_int_type=qir_int_type,
)

populated_module = qir_generator.circuit_to_module(
    qir_generator.circuit, qir_generator.module
)

print(populated_module.module.ir())
