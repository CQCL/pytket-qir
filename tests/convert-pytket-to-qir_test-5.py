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
from pytket.circuit import CircBox, OpType, Bit, Qubit  # type: ignore
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


from pytket.qasm import circuit_to_qasm_str

from pytket.circuit import Circuit

from pytket.passes import FlattenRegisters, FlattenRelabelRegistersPass

circ = Circuit(3)
a = circ.add_c_register("a", 5)
b = circ.add_c_register("b", 5)
c = circ.add_c_register("c", 5)
circ.add_classicalexpbox_register(a | b, c)
circ.H(2)
circ.H(1)
circ.X(0)
circ.Measure(Qubit(0), c[4])
circ.Z(0, condition=c[4])
circ.H(0)

print(circuit_to_qasm_str(circ, header="hqslib1"))

# FlattenRegisters().apply(circ)
# FlattenRelabelRegistersPass("q").apply(circ)

module = Module(
    name="Generated from input pytket circuit",
    num_qubits=circ.n_qubits,
    num_results=circ.n_bits,
)
wasm_int_type = types.Int(32)
qir_int_type = types.Int(64)
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

print(
    """

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""
)

import pyqir

mod = pyqir.SimpleModule("if_bool", num_qubits=2, num_results=2)
qis = pyqir.BasicQisBuilder(mod.builder)

# Use an external function to generate integers that we can compare with icmp.
i32 = pyqir.IntType(mod.context, 32)


get_int = mod.add_external_function("get_int", pyqir.FunctionType(i32, []))

# Apply X to the qubit if 'a' is 7.
a = mod.builder.call(get_int, [])
assert a is not None
a_eq_7 = mod.builder.icmp(pyqir.IntPredicate.EQ, a, pyqir.const(i32, 7))
mod.builder.if_(a_eq_7, lambda: qis.x(mod.qubits[0]))


"""
# Multiple conditions can be combined with 'and' and 'or'.
b = mod.builder.call(get_int, [])
assert b is not None
b_sgt_a = mod.builder.icmp(pyqir.IntPredicate.SGT, b, a)
or_cond = mod.builder.or_(a_eq_7, b_sgt_a)

# Both the true and false branches can be specified.
b_ne_2 = mod.builder.icmp(pyqir.IntPredicate.NE, b, pyqir.const(i32, 2))
and_cond = mod.builder.and_(or_cond, b_ne_2)
mod.builder.if_(
    and_cond,
    true=lambda: qis.h(mod.qubits[1]),
    false=lambda: qis.y(mod.qubits[1]),
)
#"""

if __name__ == "__main__":
    print(mod.ir())
