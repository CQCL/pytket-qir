# Copyright 2019-2022 Cambridge Quantum Computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from functools import partial
import os
from pathlib import Path
from string import Template
from typing import cast, Callable, Generator, List, Tuple

from pytest import fixture  # type: ignore

from pyqir.generator import bitcode_to_ir, types  # type: ignore
from pyqir.generator import Builder, IntPredicate, Value  # type: ignore
from pytket import Circuit  # type: ignore
from pytket.circuit import (  # type: ignore
    CircBox,
    OpType,
)
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

from pytket_qir.cfg import Block
from pytket_qir.generator import circuit_to_qir, write_qir_file  # type: ignore

from pytket_qir.gatesets.base import FuncName, FuncNat, FuncSpec  # type: ignore

from pytket_qir.gatesets.base import CustomGateSet, CustomQirGate
from pytket_qir.gatesets.pyqir import _TK_TO_PYQIR


qir_files_dir = Path("./qir_test_files")


@fixture
def bell_circuit() -> Circuit:
    circuit = Circuit(2, name="Bell Test")
    circuit.H(0)
    circuit.CX(0, 1)
    circuit.measure_all()
    return circuit


@fixture
def grover_circuit() -> Circuit:
    circuit = Circuit(3, 2)
    circuit.H(0).H(1).X(2).H(2).X(0).H(2).Tdg(0).Tdg(1)
    circuit.CX(2, 0).T(0).CX(1, 2).CX(1, 0).T(2).Tdg(0)
    circuit.CX(1, 2).CX(2, 0).Tdg(2).T(0).CX(1, 0).H(2).X(0)
    circuit.H(2).X(2).H(0).X(0).Z(1).CX(0, 1).Z(1).X(0).H(0)
    circuit.Measure(0, 0).Measure(1, 1)
    return circuit


@fixture
def one_conditional_else_circuit() -> Circuit:
    circuit = Circuit(5, 14)

    c_reg = circuit.get_c_register("c")

    circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    circuit.CX(3, 0).CX(1, 0).Measure(1, 0).add_gate(OpType.Reset, [1])
    circuit.Measure(2, 1).add_gate(OpType.Reset, [2])
    circuit.Measure(3, 2).add_gate(OpType.Reset, [3])
    circuit.Measure(4, 3).add_gate(OpType.Reset, [4])
    circuit.add_c_copybits([c_reg[0]], [c_reg[13]])

    true_condition_circuit = Circuit(5, 14)
    true_condition_circuit.add_gate(OpType.Reset, [0])
    true_condition_circuit.Ry(0.9553166181245094, 0).Rz(-5.497787143782138, 0)
    true_condition_circuit.Ry(0.9553166181245094, 1).Rz(-5.497787143782138, 1)
    true_condition_circuit.Ry(0.9553166181245094, 2).Rz(-5.497787143782138, 2)
    true_condition_circuit.Ry(0.9553166181245094, 3).Rz(-5.497787143782138, 3)
    true_condition_circuit.Ry(0.9553166181245094, 4).Rz(-5.497787143782138, 4)
    true_condition_circuit.Measure(1, 8).add_gate(OpType.Reset, [1])
    true_condition_circuit.Measure(2, 9).add_gate(OpType.Reset, [2])
    true_condition_circuit.Measure(3, 10).add_gate(OpType.Reset, [3])
    true_condition_circuit.Measure(4, 11).add_gate(OpType.Reset, [4])

    circ_box = CircBox(true_condition_circuit)
    args = list(range(true_condition_circuit.n_qubits)) + list(
        range(len(true_condition_circuit.bits))
    )
    circuit.add_circbox(circ_box, args, condition=if_bit(c_reg[13]))

    empty_circuit = Circuit(5, 14)
    circ_box_2 = CircBox(empty_circuit)
    args = list(range(empty_circuit.n_qubits)) + list(range(len(empty_circuit.bits)))
    circuit.add_circbox(circ_box_2, args, condition=if_not_bit(c_reg[13]))
    else_condition_circuit = Circuit(5, 14)
    else_condition_circuit.H(0).Y(0).H(0).Measure(0, 12).add_gate(OpType.Reset, [0])
    circuit.append(else_condition_circuit)

    return circuit


@fixture
def one_conditional_then_circuit() -> Circuit:
    circuit = Circuit(5, 14)

    c_reg = circuit.get_c_register("c")

    circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    circuit.CX(3, 0).CX(1, 0).Measure(1, 0).add_gate(OpType.Reset, [1])
    circuit.Measure(2, 1).add_gate(OpType.Reset, [2])
    circuit.Measure(3, 2).add_gate(OpType.Reset, [3])
    circuit.Measure(4, 3).add_gate(OpType.Reset, [4])
    circuit.add_c_copybits([c_reg[0]], [c_reg[13]])

    empty_circuit = Circuit(5, 14)
    circ_box_2 = CircBox(empty_circuit)
    args = list(range(empty_circuit.n_qubits)) + list(range(len(empty_circuit.bits)))
    circuit.add_circbox(circ_box_2, args, condition=if_bit(c_reg[13]))

    true_condition_circuit = Circuit(5, 14)
    true_condition_circuit.add_gate(OpType.Reset, [0])
    true_condition_circuit.Ry(0.9553166181245094, 0).Rz(-5.497787143782138, 0)
    true_condition_circuit.Ry(0.9553166181245094, 1).Rz(-5.497787143782138, 1)
    true_condition_circuit.Ry(0.9553166181245094, 2).Rz(-5.497787143782138, 2)
    true_condition_circuit.Ry(0.9553166181245094, 3).Rz(-5.497787143782138, 3)
    true_condition_circuit.Ry(0.9553166181245094, 4).Rz(-5.497787143782138, 4)
    true_condition_circuit.Measure(1, 8).add_gate(OpType.Reset, [1])
    true_condition_circuit.Measure(2, 9).add_gate(OpType.Reset, [2])
    true_condition_circuit.Measure(3, 10).add_gate(OpType.Reset, [3])
    true_condition_circuit.Measure(4, 11).add_gate(OpType.Reset, [4])

    circ_box = CircBox(true_condition_circuit)
    args = list(range(true_condition_circuit.n_qubits)) + list(
        range(len(true_condition_circuit.bits))
    )
    circuit.add_circbox(circ_box, args, condition=if_not_bit(c_reg[13]))

    then_condition_circuit = Circuit(5, 14)
    then_condition_circuit.H(0).Y(0).H(0).Measure(0, 12).add_gate(OpType.Reset, [0])
    circuit.append(then_condition_circuit)

    return circuit


@fixture
def one_conditional_diamond_circuit() -> Circuit:
    circuit = Circuit(5, 16)
    circuit.add_c_register("tk_SCRATCH_BIT", 4)

    creg = circuit.get_c_register("c")
    scratch_reg = circuit.get_c_register("tk_SCRATCH_BIT")

    circuit.add_c_setbits([1, 1], [13, 14])
    exp_entry = creg[13] | (creg[13] & creg[14])
    circuit.add_classicalexpbox_bit(exp_entry, [scratch_reg[0]])

    entry_circuit = Circuit(5, 16)
    creg = entry_circuit.get_c_register("c")
    entry_circuit.add_c_setbits([1], [13])
    entry_circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    entry_circuit.CX(3, 0).CX(1, 0).Measure(1, 0).add_gate(OpType.Reset, [1])
    entry_circuit.Measure(2, 1).add_gate(OpType.Reset, [2])
    entry_circuit.Measure(3, 2).add_gate(OpType.Reset, [3])
    entry_circuit.Measure(4, 3).add_gate(OpType.Reset, [4])
    entry_circuit.add_c_copybits([creg[0]], [creg[15]])

    circ_box = CircBox(entry_circuit)
    args = list(range(entry_circuit.n_qubits)) + list(range(len(entry_circuit.bits)))
    circuit.add_circbox(circ_box, args, condition=if_bit(scratch_reg[0]))

    false_condition_circuit = Circuit(5, 16)
    creg = false_condition_circuit.get_c_register("c")
    false_condition_circuit.add_c_setbits([1], [13])
    exp_false = creg[13] | (exp_entry & BitNot(creg[15]))
    circuit.add_classicalexpbox_bit(exp_false, [scratch_reg[1]])

    false_condition_circuit.Measure(2, 8).add_gate(OpType.Reset, [2])
    false_condition_circuit.Measure(3, 9).add_gate(OpType.Reset, [3])
    false_condition_circuit.Measure(4, 10).add_gate(OpType.Reset, [4])
    false_condition_circuit.Measure(1, 11).add_gate(OpType.Reset, [1])

    circ_box = CircBox(false_condition_circuit)
    args = list(range(false_condition_circuit.n_qubits)) + list(
        range(len(false_condition_circuit.bits))
    )
    circuit.add_circbox(circ_box, args, condition=if_bit(scratch_reg[1]))

    true_condition_circuit = Circuit(5, 16)
    creg = true_condition_circuit.get_c_register("c")
    true_condition_circuit.add_c_setbits([1], [13])
    exp_true = creg[13] | (exp_entry & creg[15])
    circuit.add_classicalexpbox_bit(exp_true, [scratch_reg[2]])

    true_condition_circuit.add_gate(OpType.Reset, [0])
    true_condition_circuit.Ry(0.9553166181245094, 0).Rz(-5.497787143782138, 0)
    true_condition_circuit.Ry(0.9553166181245094, 1).Rz(-5.497787143782138, 1)
    true_condition_circuit.Ry(0.9553166181245094, 2).Rz(-5.497787143782138, 2)
    true_condition_circuit.Ry(0.9553166181245094, 3).Rz(-5.497787143782138, 3)
    true_condition_circuit.Ry(0.9553166181245094, 4).Rz(-5.497787143782138, 4)
    true_condition_circuit.Measure(1, 8).add_gate(OpType.Reset, [1])
    true_condition_circuit.Measure(2, 9).add_gate(OpType.Reset, [2])
    true_condition_circuit.Measure(3, 10).add_gate(OpType.Reset, [3])
    true_condition_circuit.Measure(4, 11).add_gate(OpType.Reset, [4])

    circ_box = CircBox(true_condition_circuit)
    args = list(range(true_condition_circuit.n_qubits)) + list(
        range(len(true_condition_circuit.bits))
    )
    circuit.add_circbox(circ_box, args, condition=if_bit(scratch_reg[2]))

    diamond_condition_circuit = Circuit(5, 16)
    creg = diamond_condition_circuit.get_c_register("c")
    diamond_condition_circuit.add_c_setbits([1], [13])
    exp_diamond = (creg[13] | (exp_false & creg[13])) | (exp_true & creg[13])
    circuit.add_classicalexpbox_bit(exp_diamond, [scratch_reg[3]])
    diamond_condition_circuit.H(0).Y(0).H(0).Measure(0, 12).add_gate(OpType.Reset, [0])
    # circuit.append(diamond_condition_circuit)

    circ_box_2 = CircBox(diamond_condition_circuit)
    args = list(range(diamond_condition_circuit.n_qubits)) + list(
        range(len(diamond_condition_circuit.bits))
    )
    circuit.add_circbox(circ_box_2, args, condition=if_bit(scratch_reg[3]))

    return circuit


@fixture
def collapse_jump_instr() -> None:
    circuit = Circuit(5, 15)
    c_reg = circuit.get_c_register("c")
    circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1)
    circuit.add_c_copybits([c_reg[0]], [c_reg[13]])

    else_circuit = Circuit(5, 15)
    else_circuit.Z(2).Z(2).Z(2)

    circ_box_2 = CircBox(else_circuit)
    args = list(else_circuit.qubits) + list(else_circuit.bits)
    circuit.add_circbox(circ_box_2, args, condition=if_not_bit(c_reg[13]))

    then_circuit = Circuit(5, 15)
    then_circuit.Ry(0.9553166181245094, 0)
    then_circuit.Rz(-5.497787143782138, 0)
    then_circuit.Ry(0.9553166181245094, 1)
    then_circuit.Rz(-5.497787143782138, 1)
    then_circuit.X(1).X(1).X(1)
    then_circuit.Y(1).Y(1).Y(1)

    circ_box_1 = CircBox(then_circuit)
    args = list(then_circuit.qubits) + list(then_circuit.bits)
    circuit.add_circbox(circ_box_1, args, condition=if_bit(c_reg[13]))

    circuit.H(0).H(0).H(0)
    circuit.add_c_copybits([c_reg[1]], [c_reg[14]])

    leftbr1 = Circuit(5, 15)
    leftbr1.Z(0).Z(0).Z(0)

    circ_box_2 = CircBox(leftbr1)
    args = list(leftbr1.qubits) + list(leftbr1.bits)
    circuit.add_circbox(circ_box_2, args, condition=if_bit(c_reg[14]))

    rightbr1 = Circuit(5, 15)
    rightbr1.Y(2).Y(2).Y(2).X(2).X(2).X(2)

    circ_box_3 = CircBox(rightbr1)
    args = list(rightbr1.qubits) + list(rightbr1.bits)
    circuit.add_circbox(circ_box_3, args, condition=if_not_bit(c_reg[14]))

    circuit.H(2).H(2)

    return circuit


@fixture
def nested_conditionals_then() -> None:
    circuit = Circuit(5, 15)
    c_reg = circuit.get_c_register("c")
    circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1)
    circuit.add_c_copybits([c_reg[0]], [c_reg[13]])

    then_circuit = Circuit(5, 15)
    then_circuit.add_c_copybits([c_reg[1]], [c_reg[14]])
    then_circuit.Ry(0.9553166181245094, 0)
    then_circuit.Rz(-5.497787143782138, 0)
    then_circuit.Ry(0.9553166181245094, 1)
    then_circuit.Rz(-5.497787143782138, 1)

    then_circuit_1 = Circuit(5, 15)
    then_circuit_1.X(1).X(1).X(1)

    else_circuit_1 = Circuit(5, 15)
    else_circuit_1.Y(1).Y(1).Y(1)

    nested_circ_box_1 = CircBox(then_circuit_1)
    args = list(then_circuit_1.qubits) + list(then_circuit_1.bits)
    then_circuit.add_circbox(nested_circ_box_1, args, condition=if_bit(c_reg[14]))
    nested_circ_box_2 = CircBox(else_circuit_1)
    args = list(else_circuit_1.qubits) + list(else_circuit_1.bits)
    then_circuit.add_circbox(nested_circ_box_2, args, condition=if_not_bit(c_reg[14]))

    circ_box_1 = CircBox(then_circuit)
    args = list(then_circuit.qubits) + list(then_circuit.bits)
    circuit.add_circbox(circ_box_1, args, condition=if_bit(c_reg[13]))

    else_circuit = Circuit(5, 15)
    else_circuit.Z(2).Z(2).Z(2)

    circ_box_2 = CircBox(else_circuit)
    args = list(else_circuit.qubits) + list(else_circuit.bits)
    circuit.add_circbox(circ_box_2, args, condition=if_not_bit(c_reg[13]))

    exit_circuit = Circuit(5, 15)
    exit_circuit.H(0).H(0).H(0)

    circuit.append(exit_circuit)
    return circuit


@fixture
def nested_conditionals_circuit() -> Circuit:
    circuit = Circuit(5, 16)

    c_reg = circuit.get_c_register("c")

    circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    circuit.CX(3, 0).CX(1, 0)
    circuit.Measure(1, 0).add_gate(OpType.Reset, [1])
    circuit.Measure(2, 1).add_gate(OpType.Reset, [2])
    circuit.Measure(3, 2).add_gate(OpType.Reset, [3])
    circuit.Measure(4, 3).add_gate(OpType.Reset, [4])
    circuit.add_c_copybits([c_reg[0]], [c_reg[13]])

    condition_circuit_1 = Circuit(5, 16)
    condition_circuit_1.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    condition_circuit_1.CX(3, 0).CX(1, 0)
    condition_circuit_1.Measure(1, 0).add_gate(OpType.Reset, [1])
    condition_circuit_1.Measure(2, 1).add_gate(OpType.Reset, [2])
    condition_circuit_1.Measure(3, 2).add_gate(OpType.Reset, [3])
    condition_circuit_1.Measure(4, 3).add_gate(OpType.Reset, [4])
    condition_circuit_1.add_c_copybits([c_reg[1]], [c_reg[14]])

    condition_circuit_2 = Circuit(5, 16)
    condition_circuit_2.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    condition_circuit_2.CX(3, 0).CX(1, 0).add_gate(OpType.Reset, [1])
    condition_circuit_2.Measure(2, 1).add_gate(OpType.Reset, [2])
    condition_circuit_2.Measure(3, 2).add_gate(OpType.Reset, [3])
    condition_circuit_2.Measure(4, 3).add_gate(OpType.Reset, [4])
    condition_circuit_2.add_c_copybits([c_reg[2]], [c_reg[14]])

    nested_conditional_circuit_1 = Circuit(5, 15)
    nested_conditional_circuit_1.add_gate(OpType.Reset, [0])
    nested_conditional_circuit_1.Ry(0.9553166181245094, 0)
    nested_conditional_circuit_1.Rz(-5.497787143782138, 0)
    nested_conditional_circuit_1.Ry(0.9553166181245094, 1)
    nested_conditional_circuit_1.Rz(-5.497787143782138, 1)
    nested_conditional_circuit_1.Ry(0.9553166181245094, 2)
    nested_conditional_circuit_1.Rz(-5.497787143782138, 2)
    nested_conditional_circuit_1.Ry(0.9553166181245094, 3)
    nested_conditional_circuit_1.Rz(-5.497787143782138, 3)
    nested_conditional_circuit_1.Ry(0.9553166181245094, 4)
    nested_conditional_circuit_1.Rz(-5.497787143782138, 4)

    nested_conditional_circuit_1.Measure(1, 8).add_gate(OpType.Reset, [1])
    nested_conditional_circuit_1.Measure(2, 9).add_gate(OpType.Reset, [2])
    nested_conditional_circuit_1.Measure(3, 10).add_gate(OpType.Reset, [3])
    nested_conditional_circuit_1.Measure(4, 11).add_gate(OpType.Reset, [4])

    nested_circ_box_1 = CircBox(nested_conditional_circuit_1)
    args = list(nested_conditional_circuit_1.qubits) + list(
        nested_conditional_circuit_1.bits
    )
    condition_circuit_1.add_circbox(
        nested_circ_box_1, args, condition=if_bit(c_reg[14])
    )
    condition_circuit_2.add_circbox(
        nested_circ_box_1, args, condition=if_bit(c_reg[14])
    )

    nested_conditional_circuit_2 = Circuit(5, 15)
    nested_conditional_circuit_2.H(0).Y(0).H(0)
    nested_conditional_circuit_2.H(0).Y(0).H(0)
    nested_conditional_circuit_2.Measure(0, 12).add_gate(OpType.Reset, [0])
    condition_circuit_1.append(nested_conditional_circuit_2)
    condition_circuit_2.append(nested_conditional_circuit_2)

    circ_box_1 = CircBox(condition_circuit_1)
    args = list(range(condition_circuit_1.n_qubits)) + list(
        range(len(condition_circuit_1.bits))
    )
    circuit.add_circbox(circ_box_1, args, condition=if_bit(c_reg[13]))

    circuit.append(condition_circuit_2)
    return circuit


@fixture
def circuit_classical_arithmetic() -> Circuit:
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
    write_qir_file(circ, "ClassicalCircuit.ll")
    yield
    os.remove("ClassicalCircuit.ll")


@fixture
def circuit_classical_reg2const_arithmetic() -> Circuit:
    circ = Circuit(2)
    a = circ.add_c_register("a", 3)
    b = circ.add_c_register("b", 3)
    c = circ.add_c_register("c", 3)
    circ.add_c_setreg(3, b)
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
    write_qir_file(circ, "ClassicalReg2ConstCircuit.ll")
    yield
    os.remove("ClassicalReg2ConstCircuit.ll")


@fixture
def bitwise_file() -> str:
    return "test_bitwise_ops.ll"


@fixture
def file_name() -> str:
    return "SimpleCircuit.ll"


@fixture
def circuit_pyqir_gateset(file_name: str) -> Generator:
    c = Circuit(2, 2)
    c.H(0)
    c.X(1)
    c.Y(0)
    c.Z(1)
    c.S(0)
    c.Sdg(1)
    c.T(0)
    c.Tdg(1)
    c.add_gate(OpType.Reset, [0])
    c.CX(0, 1)
    c.CZ(1, 0)
    c.Rx(0.0, 1)
    c.Ry(1.0, 0)
    c.Rz(2.0, 1)
    c.Measure(1, 1)
    write_qir_file(c, file_name)
    yield
    os.remove(file_name)


@fixture
def simple_conditional_file_name() -> str:
    return "SimpleConditionalCircuit.ll"


@fixture
def simple_conditional_circuit(simple_conditional_file_name: str) -> Generator:
    c = Circuit(2, 2)

    measure_reg = c.add_c_register("%0", 1)
    source_reg = c.get_c_register("c")
    c.add_c_copybits([source_reg[0]], [measure_reg[0]])

    c.X(0).X(1)
    # Sub-circuit for condition true
    c1 = Circuit(2)
    c1.H(0).H(1)

    cb1 = CircBox(c1)
    args1 = list(range(c1.n_qubits)) + list(range(len(c1.bits)))
    c.add_circbox(cb1, args1, condition=if_bit(measure_reg[0]))

    c.Y(0).Y(1)

    measure_reg = c.add_c_register("%1", 1)
    c.add_c_copybits([source_reg[1]], [measure_reg[0]])
    # Sub-circuit for condition false
    c.add_circbox(cb1, args1, condition=if_not_bit(measure_reg[0]))

    c.Z(0).Z(1)

    qis_read_result = CustomQirGate(
        func_nat=FuncNat.QIS,
        func_name=FuncName.READ_RES,
        func_spec=FuncSpec.BODY,
        function_signature=[types.RESULT],
        return_type=types.BOOL,
    )

    _PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}

    ext_pyqir_gates = CustomGateSet(
        name="ExtPyQir",
        template=Template("__quantum__${func_nat}__${func_name}__${func_spec}"),
        base_gateset=set(_TK_TO_PYQIR.keys()),
        gateset={"read_result": qis_read_result},
        tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
        gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
    )

    ir_bytes = cast(bytes, circuit_to_qir(c, gateset=ext_pyqir_gates))
    ll = bitcode_to_ir(ir_bytes)

    with open(simple_conditional_file_name, "w") as output_file:
        output_file.write(ll)

    yield
    os.remove(simple_conditional_file_name)


@fixture
def pytket_nested_conditionals_file_name() -> str:
    return "NestedConditionalsCircuit.ll"


@fixture
def pytket_nested_conditionals_circuit(
    pytket_nested_conditionals_file_name: str,
) -> Generator:
    circuit = Circuit(2, 2)
    circuit.X(0).X(1)

    # Sub-circuit for conditonal true
    c1 = Circuit(2, 2)
    c1.Y(0).Y(1)

    # Sub-circuit for conditional false
    c2 = Circuit(2)
    c2.Z(0).Z(1)

    cb2 = CircBox(c2)
    args2 = list(range(c2.n_qubits)) + list(range(len(c2.bits)))
    c1.add_circbox(cb2, args2, condition_bits=[1], condition_value=0)

    cb1 = CircBox(c1)
    args1 = list(range(c1.n_qubits)) + list(range(len(c1.bits)))

    circuit.add_circbox(cb1, args1, condition_bits=[0], condition_value=1)

    write_qir_file(circuit, pytket_nested_conditionals_file_name)
    yield
    os.remove(pytket_nested_conditionals_file_name)


_OPERATORS: List[Tuple[str, Callable[[Builder], Callable[[Value, Value], Value]]]] = [
    ("and", lambda b: b.and_),
    ("or", lambda b: b.or_),
    ("xor", lambda b: b.xor),
    ("add", lambda b: b.add),
    ("sub", lambda b: b.sub),
    ("mul", lambda b: b.mul),
    ("shl", lambda b: b.shl),
    ("lshr", lambda b: b.lshr),
    ("icmp eq", lambda b: partial(b.icmp, IntPredicate.EQ)),
    ("icmp ne", lambda b: partial(b.icmp, IntPredicate.NE)),
    ("icmp ugt", lambda b: partial(b.icmp, IntPredicate.UGT)),
    ("icmp uge", lambda b: partial(b.icmp, IntPredicate.UGE)),
    ("icmp ult", lambda b: partial(b.icmp, IntPredicate.ULT)),
    ("icmp ule", lambda b: partial(b.icmp, IntPredicate.ULE)),
    ("icmp sgt", lambda b: partial(b.icmp, IntPredicate.SGT)),
    ("icmp sge", lambda b: partial(b.icmp, IntPredicate.SGE)),
    ("icmp slt", lambda b: partial(b.icmp, IntPredicate.SLT)),
    ("icmp sle", lambda b: partial(b.icmp, IntPredicate.SLE)),
]


@fixture
def operators() -> List:
    return _OPERATORS


@fixture
def simple_conditional_cfg() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["then0__2.i.i.i", "else"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "then0__2.i.i.i": Block(
            name="then0__2.i.i.i",
            succs=[
                "Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit"
            ],
            preds=["entry"],
            composition=["then0__2.i.i.i"],
            visited=False,
        ),
        "else": Block(
            name="else",
            succs=[
                "Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit"
            ],
            preds=["entry"],
            composition=["else"],
            visited=False,
        ),
        "Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit": Block(
            name="Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit",
            succs=[],
            preds=["else", "then0__2.i.i.i"],
            composition=[
                "Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit"
            ],
            visited=False,
        ),
    }
    return cfg


@fixture
def collapsed_simple_chain_cfg() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=[],
            preds=[],
            composition=[
                "entry",
                "continue1",
                "continue2",
                "continue3",
                "continue4",
                "continue5",
                "continue6",
                "continue7",
                "continue8",
                "exit1",
                "exit2",
            ],
            visited=False,
        )
    }
    return cfg


@fixture
def collapsed_jump_left_cfg() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["else0", "then0"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "else0": Block(
            name="else0",
            succs=["continue0"],
            preds=["entry"],
            composition=["else0"],
            visited=False,
        ),
        "then0": Block(
            name="then0",
            succs=["continue0"],
            preds=["entry"],
            composition=["then0", "then1", "then2"],
            visited=False,
        ),
        "continue0": Block(
            name="continue0",
            succs=[],
            preds=["then0", "else0"],
            composition=["continue0"],
            visited=False,
        ),
    }
    return cfg


@fixture
def collapsed_jump_right_cfg() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["then0", "else0"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "then0": Block(
            name="then0",
            succs=["continue0"],
            preds=["entry"],
            composition=["then0"],
            visited=False,
        ),
        "else0": Block(
            name="else0",
            succs=["continue0"],
            preds=["entry"],
            composition=["else0", "then1", "then2"],
            visited=False,
        ),
        "continue0": Block(
            name="continue0",
            succs=[],
            preds=["else0", "then0"],
            composition=["continue0"],
            visited=False,
        ),
    }
    return cfg


@fixture
def collapsed_complex_chain() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["else0", "then0"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "else0": Block(
            name="else0",
            succs=["continue0"],
            preds=["entry"],
            composition=["else0"],
            visited=False,
        ),
        "then0": Block(
            name="then0",
            succs=["continue0"],
            preds=["entry"],
            composition=["then0", "then1", "then2"],
            visited=False,
        ),
        "continue0": Block(
            name="continue0",
            succs=["leftbr1", "rightbr1"],
            preds=["then0", "else0"],
            composition=["continue0", "continue1", "continue2"],
            visited=False,
        ),
        "leftbr1": Block(
            name="leftbr1",
            succs=["exit1"],
            preds=["continue0"],
            composition=["leftbr1"],
            visited=False,
        ),
        "rightbr1": Block(
            name="rightbr1",
            succs=["exit1"],
            preds=["continue0"],
            composition=["rightbr1", "rightbr2"],
            visited=False,
        ),
        "exit1": Block(
            name="exit1",
            succs=[],
            preds=["rightbr1", "leftbr1"],
            composition=["exit1", "exit2"],
            visited=False,
        ),
    }
    return cfg


@fixture
def collapsed_nested_chains() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["else0", "then0"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "else0": Block(
            name="else0",
            succs=["continue0"],
            preds=["entry"],
            composition=["else0"],
            visited=False,
        ),
        "then0": Block(
            name="then0",
            succs=["then11", "else11"],
            preds=["entry"],
            composition=["then0", "then1", "then2"],
            visited=False,
        ),
        "then11": Block(
            name="then11",
            succs=["continue0"],
            preds=["then0"],
            composition=["then11", "then12", "then13"],
            visited=False,
        ),
        "else11": Block(
            name="else11",
            succs=["continue0"],
            preds=["then0"],
            composition=["else11"],
            visited=False,
        ),
        "continue0": Block(
            name="continue0",
            succs=["leftbr1", "rightbr1"],
            preds=["else11", "then11", "else0"],
            composition=["continue0", "continue1", "continue2"],
            visited=False,
        ),
        "leftbr1": Block(
            name="leftbr1",
            succs=["exit1"],
            preds=["continue0"],
            composition=["leftbr1"],
            visited=False,
        ),
        "rightbr1": Block(
            name="rightbr1",
            succs=["exit1"],
            preds=["continue0"],
            composition=["rightbr1", "rightbr2"],
            visited=False,
        ),
        "exit1": Block(
            name="exit1",
            succs=[],
            preds=["rightbr1", "leftbr1"],
            composition=["exit1", "exit2"],
            visited=False,
        ),
    }
    return cfg


@fixture
def insert_block_right() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["then0__2.i.i.i", "entry_trivial_block"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "then0__2.i.i.i": Block(
            name="then0__2.i.i.i",
            succs=[
                "Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit"
            ],
            preds=["entry"],
            composition=["then0__2.i.i.i"],
            visited=False,
        ),
        "Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit": Block(
            name="Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit",
            succs=[],
            preds=["then0__2.i.i.i", "entry_trivial_block"],
            composition=[
                "Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit"
            ],
            visited=False,
        ),
        "entry_trivial_block": Block(
            name="entry_trivial_block",
            succs=[
                "Microsoft__Quantum__Samples__MeasureDistilledTAtDepth3InX__body.1.exit"
            ],
            preds=["entry"],
            composition=["entry_trivial_block"],
            visited=False,
        ),
    }
    return cfg


@fixture
def insert_block_left() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["else", "entry_trivial_block"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "else": Block(
            name="else",
            succs=["then"],
            preds=["entry"],
            composition=["else"],
            visited=False,
        ),
        "then": Block(
            name="then",
            succs=[],
            preds=["else", "entry_trivial_block"],
            composition=["then"],
            visited=False,
        ),
        "entry_trivial_block": Block(
            name="entry_trivial_block",
            succs=["then"],
            preds=["entry"],
            composition=["entry_trivial_block"],
            visited=False,
        ),
    }
    return cfg


@fixture
def insert_nested_blocks_right() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["then", "entry_trivial_block"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "then": Block(
            name="then",
            succs=["continue"],
            preds=["entry"],
            composition=["then"],
            visited=False,
        ),
        "continue": Block(
            name="continue",
            succs=["then1", "continue_trivial_block"],
            preds=["then", "entry_trivial_block"],
            composition=["continue"],
            visited=False,
        ),
        "then1": Block(
            name="then1",
            succs=[
                "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i"
            ],
            preds=["continue"],
            composition=["then1"],
            visited=False,
        ),
        "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i": Block(
            name="TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i",
            succs=[
                "then2",
                "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit."
                "i_trivial_block",
            ],
            preds=["then1", "continue_trivial_block"],
            composition=[
                "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i"
            ],
            visited=False,
        ),
        "then2": Block(
            name="then2",
            succs=["continue2"],
            preds=[
                "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i"
            ],
            composition=["then2"],
            visited=False,
        ),
        "continue2": Block(
            name="continue2",
            succs=["then3", "continue2_trivial_block"],
            preds=[
                "then2",
                "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2."
                "exit.i_trivial_block",
            ],
            composition=["continue2"],
            visited=False,
        ),
        "then3": Block(
            name="then3",
            succs=[
                "TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement"
                "__body.1.exit"
            ],
            preds=["continue2"],
            composition=["then3"],
            visited=False,
        ),
        "TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__body."
        "1.exit": Block(
            name="TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement"
            "__body.1.exit",
            succs=[],
            preds=["then3", "continue2_trivial_block"],
            composition=[
                "TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__"
                "body.1.exit"
            ],
            visited=False,
        ),
        "entry_trivial_block": Block(
            name="entry_trivial_block",
            succs=["continue"],
            preds=["entry"],
            composition=["entry_trivial_block"],
            visited=False,
        ),
        "continue_trivial_block": Block(
            name="continue_trivial_block",
            succs=[
                "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i"
            ],
            preds=["continue"],
            composition=["continue_trivial_block"],
            visited=False,
        ),
        "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit."
        "i_trivial_block": Block(
            name="TeleportChain__TeleportQubitUsingPresharedEntanglement__body."
            "2.exit.i_trivial_block",
            succs=["continue2"],
            preds=[
                "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2."
                "exit.i"
            ],
            composition=[
                "TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2."
                "exit.i_trivial_block"
            ],
            visited=False,
        ),
        "continue2_trivial_block": Block(
            name="continue2_trivial_block",
            succs=[
                "TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement"
                "__body.1.exit"
            ],
            preds=["continue2"],
            composition=["continue2_trivial_block"],
            visited=False,
        ),
    }
    return cfg


@fixture
def split_fork_left() -> dict:
    cfg = {
        "entry": Block(
            name="entry",
            succs=["then", "else"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "then": Block(
            name="then",
            succs=["then1", "else1"],
            preds=["entry"],
            composition=["then"],
            visited=False,
        ),
        "then1": Block(
            name="then1",
            succs=["exit_trivial_block"],
            preds=["then"],
            composition=["then1"],
            visited=False,
        ),
        "else1": Block(
            name="else1",
            succs=["exit_trivial_block"],
            preds=["then"],
            composition=["else1"],
            visited=False,
        ),
        "else": Block(
            name="else",
            succs=["exit"],
            preds=["entry"],
            composition=["else"],
            visited=False,
        ),
        "exit": Block(
            name="exit",
            succs=[],
            preds=["else", "exit_trivial_block"],
            composition=["exit"],
            visited=False,
        ),
        "exit_trivial_block": Block(
            name="exit_trivial_block",
            succs=["exit"],
            preds=["else1", "then1"],
            composition=["exit_trivial_block"],
            visited=False,
        ),
    }
    return cfg


@fixture
def split_fork_right() -> dict:
    return {
        "entry": Block(
            name="entry",
            succs=["then", "else"],
            preds=[],
            composition=["entry"],
            visited=False,
        ),
        "then": Block(
            name="then",
            succs=["exit"],
            preds=["entry"],
            composition=["then"],
            visited=False,
        ),
        "else": Block(
            name="else",
            succs=["then1", "else1"],
            preds=["entry"],
            composition=["else"],
            visited=False,
        ),
        "then1": Block(
            name="then1",
            succs=["exit_trivial_block"],
            preds=["else"],
            composition=["then1"],
            visited=False,
        ),
        "else1": Block(
            name="else1",
            succs=["exit_trivial_block"],
            preds=["else"],
            composition=["else1"],
            visited=False,
        ),
        "exit": Block(
            name="exit",
            succs=[],
            preds=["exit_trivial_block", "then"],
            composition=["exit"],
            visited=False,
        ),
        "exit_trivial_block": Block(
            name="exit_trivial_block",
            succs=["exit"],
            preds=["else1", "then1"],
            composition=["exit_trivial_block"],
            visited=False,
        ),
    }
