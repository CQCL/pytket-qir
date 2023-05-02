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
qb = circ.add_q_register("qb", 3)
bb = circ.add_c_register("bb", 5)
c = circ.add_c_register("c", 5)
#circ.add_classicalexpbox_register(a & bb, c)
circ.add_classicalexpbox_register(a | c, bb)
circ.H(qb[0])
#circ.H(2)
#circ.H(1)
# circ.add_barrier([0, 1]) not working
circ.X(0)
#circ.Y(1)
#circ.Z(1)
# circ.H(0, condition=Bit(0))
circ.Measure(Qubit(0), c[4])
circ.H(0, condition=c[4])
#circ.H(0, condition=Bit(0))
#circ.H(0, condition=Bit(0))

#circ.Y(1, condition=Bit(1))
#circ.Z(2, condition=c[1])

circ.H(0)
#circ.H(1)
#circ.H(2)

#circ.H(0)
#circ.Measure(qb[0], a[0])
#cbcirc = Circuit(3)
#cbcirc.H(0)  # , condition=a[0]

#print(dir(circ))
#print(circ.bits)
#print(len(circ.bits))

#circ_box = CircBox(cbcirc)
# circ.add_circbox(circ_box, [0, 1, 2], condition=if_bit(a[0]))

for g in circ:
    print(g)

print(circuit_to_qasm_str(circ, header="hqslib1"))

FlattenRegisters().apply(circ)
# FlattenRelabelRegistersPass("q").apply(circ)
# FlattenRelabelRegistersPass

print("START ###############################")

circ = Circuit(3)
a = circ.add_c_register("a", 5)
b = circ.add_c_register("b", 5)
c = circ.add_c_register("c", 5)
circ.add_classicalexpbox_register(a | b, c)



print(circ.to_dict())
# FlattenRegisters().apply(circ)

map = {
    Bit("a", 0) : Bit("d", 0),
    Bit("a", 1) : Bit("d", 1),
    Bit("a", 2) : Bit("d", 2),
    Bit("a", 3) : Bit("d", 3),
    Bit("a", 4) : Bit("d", 4),
}
circ.rename_units(map)

print(circ.to_dict())

print("START ###############################")

"""
{'bits': [['c', [0]], ['c', [1]], ['c', [2]], ['c', [3]], ['c', [4]], ['c', [5]], ['c', [6]], ['c', [7]], ['c', [8]], ['c', [9]], ['c', [10]],
        ['c', [11]], ['c', [12]], ['c', [13]], ['c', [14]]], 
 'commands': [{'args': [['c', [0]], ['c', [1]], ['c', [2]], ['c', [3]], ['c', [4]], ['c', [10]], ['c', [11]], ['c', [12]], ['c', [13]], ['c', [14]],
                        ['c', [5]], ['c', [6]], ['c', [7]], ['c', [8]], ['c', [9]]],
               'op': {'box': {'exp': {'args': [{'name': 'a', 'size': 5}, {'name': 'c', 'size': 5}], 'op': 'RegWiseOp.OR'},
               'id': 'ee032f0b-4559-421b-b855-2d38d97c9b94', 'n_i': 10, 'n_io': 0, 'n_o': 5, 'type': 'ClassicalExpBox'}, 'type': 'ClassicalExpBox'}},
                 {'args': [['q', [0]]], 'op': {'type': 'X'}}, 
                 {'args': [['q', [3]]], 'op': {'type': 'H'}}, 
                 {'args': [['q', [0]], ['c', [14]]], 'op': {'type': 'Measure'}}, 
                 {'args': [['c', [14]], ['q', [0]]], 'op': {'conditional': {'op': {'type': 'H'}, 'value': 1, 'width': 1}, 'type': 'Conditional'}}, 
                 {'args': [['q', [0]]], 'op': {'type': 'H'}}],
                  
                   
                 'created_qubits': [], 'discarded_qubits': [],
                   'implicit_permutation': [[['q', [0]], ['q', [0]]], [['q', [1]], ['q', [1]]], [['q', [2]], ['q', [2]]], [['q', [3]], ['q', [3]]],
                                       [['q', [4]], ['q', [4]]], [['q', [5]], ['q', [5]]]],
                   'phase': '0.0', 'qubits': [['q', [0]], ['q', [1]], ['q', [2]], ['q', [3]], ['q', [4]], ['q', [5]]]}


"""

for g in circ:
    print(g)

print(circ.to_dict())

print(circuit_to_qasm_str(circ, header="hqslib1"))

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




"""
#with open("ClassicalCircuit-cond.ll", "w") as output_file:
#output_file.write(populated_module.module.ir())

#print(populated_module)
#print(dir(populated_module))
#print("\n\n")
#print(dir(populated_module.module.ir))
#print("\n\n")
#print(populated_module.module.ir.__str__())
#print(populated_module.module.qubits)
#for x in populated_module.module.qubits:
#print(x)
##print(x.name)
##print(x.type)
#print(dir(x))
#print(populated_module.module.results)
#for x in populated_module.module.results:
#print(x)
##print(x.name)
##print(x.type)
#print(dir(x))
#print(populated_module.module.ir())"""

print(
    """

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""
)


print(populated_module.module.ir())

print(
    """

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""
)
"""

# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from pyqir import BasicQisBuilder, SimpleModule

mod = SimpleModule("if_result", num_qubits=2, num_results=2)
qis = BasicQisBuilder(mod.builder)

# Manually reset a qubit by measuring it and applying the X gate if the result
# is one.
qis.h(mod.qubits[0])
qis.mz(mod.qubits[0], mod.results[0])
qis.if_result(mod.results[0], lambda: qis.x(mod.qubits[0]))
qis.h(mod.qubits[0])


# Branches can be nested, for example, to execute an instruction only if both
# results are one.
for i in range(2):
    qis.h(mod.qubits[i])
    qis.mz(mod.qubits[i], mod.results[i])


def x_both() -> None:
    qis.x(mod.qubits[0])
    qis.x(mod.qubits[1])


qis.if_result(mod.results[0], lambda: qis.if_result(mod.results[1], x_both))

# You can also add instructions that will execeute only when the result is zero.
qis.if_result(mod.results[0], zero=lambda: qis.x(mod.qubits[0]))

# In general, you can provide both the one and zero branches at the same time.
qis.if_result(
    mod.results[0],
    one=lambda: qis.z(mod.qubits[0]),
    zero=lambda: qis.y(mod.qubits[0]),
)

"""

# if __name__ == "__main__":
# print(mod.ir())



# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

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


#"""
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
