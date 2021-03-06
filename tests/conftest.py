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

import os
from pathlib import Path
from typing import Generator

from pytest import fixture  # type: ignore

from pytket import Circuit  # type: ignore
from pytket.circuit import (  # type: ignore
    CircBox,
    OpType,
)

from pytket_qir.qir import write_qir_file

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
def one_conditional_circuit() -> Circuit:
    circuit = Circuit(5, 13)
    circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    circuit.CX(3, 0).CX(1, 0).Measure(1, 0).add_gate(OpType.Reset, [1])
    circuit.Measure(2, 1).add_gate(OpType.Reset, [2])
    circuit.Measure(3, 2).add_gate(OpType.Reset, [3])
    circuit.Measure(4, 3).add_gate(OpType.Reset, [4])

    condition_circuit = Circuit(5, 13)
    condition_circuit.add_gate(OpType.Reset, [0])
    condition_circuit.Ry(0.9553166181245094, 0).Rz(-5.497787143782138, 0)
    condition_circuit.Ry(0.9553166181245094, 1).Rz(-5.497787143782138, 1)
    condition_circuit.Ry(0.9553166181245094, 2).Rz(-5.497787143782138, 2)
    condition_circuit.Ry(0.9553166181245094, 3).Rz(-5.497787143782138, 3)
    condition_circuit.Ry(0.9553166181245094, 4).Rz(-5.497787143782138, 4)
    condition_circuit.Measure(1, 8).add_gate(OpType.Reset, [1])
    condition_circuit.Measure(2, 9).add_gate(OpType.Reset, [2])
    condition_circuit.Measure(3, 10).add_gate(OpType.Reset, [3])
    condition_circuit.Measure(4, 11).add_gate(OpType.Reset, [4])

    condition_circuit.H(0).Y(0).H(0)
    condition_circuit.Measure(0, 12).add_gate(OpType.Reset, [0])

    circ_box = CircBox(condition_circuit)
    c_reg = circuit.get_c_register("c")
    args = list(circuit.qubits) + list(circuit.bits)
    circuit.add_circbox(circ_box, args, condition=c_reg[0])

    circuit.H(0).Y(0).H(0).Measure(0, 12).add_gate(OpType.Reset, [0])

    return circuit


@fixture
def multiple_conditionals_circuit() -> Circuit:
    circuit = Circuit(6, 6)
    circuit.H(0).CX(0, 1).H(2).CX(2, 4).H(3).CX(3, 5).CX(1, 2).H(1)
    circuit.Measure(1, 0).add_gate(OpType.Reset, [1])

    condition_circuit_1 = Circuit(6, 6)
    condition_circuit_1.Z(4)
    condition_circuit_1.Measure(2, 1).add_gate(OpType.Reset, [2])

    condition_circuit_1_1 = Circuit(6, 6)
    condition_circuit_1_1.X(4)
    condition_circuit_1_1.CX(4, 3).H(4)
    condition_circuit_1_1.Measure(4, 2).add_gate(OpType.Reset, [4])

    condition_circuit_1_1_1 = Circuit(6, 6)
    condition_circuit_1_1_1.Z(5)
    append_condition_circuit_1_1_1 = Circuit(6, 6)
    append_condition_circuit_1_1_1.Measure(3, 3).add_gate(OpType.Reset, [3])
    condition_circuit_1_1_1.append(append_condition_circuit_1_1_1)

    condition_circuit_1_1_1_1 = Circuit(6, 6)
    condition_circuit_1_1_1_1.X(5)
    append_condition_circuit_1_1_1_1 = Circuit(6, 6)
    append_condition_circuit_1_1_1_1.Measure(0, 4).add_gate(OpType.Reset, [0])
    append_condition_circuit_1_1_1_1.Measure(5, 5).add_gate(OpType.Reset, [5])
    condition_circuit_1_1_1_1.append(append_condition_circuit_1_1_1_1)

    circ_box_1_1_1_1 = CircBox(condition_circuit_1_1_1_1)
    c_reg = circuit.get_c_register("c")
    args = list(circuit.qubits) + list(circuit.bits)
    condition_circuit_1_1_1.add_circbox(circ_box_1_1_1_1, args, condition=c_reg[3])
    condition_circuit_1_1_1.append(append_condition_circuit_1_1_1_1)

    circ_box_1_1_1 = CircBox(condition_circuit_1_1_1)
    c_reg = circuit.get_c_register("c")
    condition_circuit_1_1.add_circbox(circ_box_1_1_1, args, condition=c_reg[2])
    condition_circuit_1_1.Measure(3, 3).add_gate(OpType.Reset, [3])
    condition_circuit_1_1.add_circbox(circ_box_1_1_1_1, args, condition=c_reg[3])
    condition_circuit_1_1.append(append_condition_circuit_1_1_1_1)

    circ_box_1_1 = CircBox(condition_circuit_1_1)
    c_reg = circuit.get_c_register("c")
    condition_circuit_1.add_circbox(circ_box_1_1, args, condition=c_reg[1])
    condition_circuit_1.CX(4, 3).H(4)
    condition_circuit_1.Measure(4, 2).add_gate(OpType.Reset, [4])
    condition_circuit_1.add_circbox(circ_box_1_1_1, args, condition=c_reg[2])
    condition_circuit_1.Measure(3, 3).add_gate(OpType.Reset, [3])
    condition_circuit_1.add_circbox(circ_box_1_1_1_1, args, condition=c_reg[3])
    condition_circuit_1.append(append_condition_circuit_1_1_1_1)

    circ_box_1 = CircBox(condition_circuit_1)
    c_reg = circuit.get_c_register("c")
    circuit.add_circbox(circ_box_1, args, condition=c_reg[0])
    circuit.Measure(2, 1).add_gate(OpType.Reset, [2])
    circuit.add_circbox(circ_box_1_1, args, condition=c_reg[1])
    circuit.CX(4, 3).H(4)
    circuit.Measure(4, 2).add_gate(OpType.Reset, [4])
    circuit.add_circbox(circ_box_1_1_1, args, condition=c_reg[2])
    circuit.Measure(3, 3).add_gate(OpType.Reset, [3])
    circuit.add_circbox(circ_box_1_1_1_1, args, condition=c_reg[3])
    circuit.append(append_condition_circuit_1_1_1_1)

    return circuit


@fixture
def nested_conditionals_circuit() -> Circuit:
    circuit = Circuit(5, 13)
    circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    circuit.CX(3, 0).CX(1, 0)
    circuit.Measure(1, 0).add_gate(OpType.Reset, [1])
    circuit.Measure(2, 1).add_gate(OpType.Reset, [2])
    circuit.Measure(3, 2).add_gate(OpType.Reset, [3])
    circuit.Measure(4, 3).add_gate(OpType.Reset, [4])

    condition_circuit_1 = Circuit(5, 13)
    condition_circuit_1.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0)
    condition_circuit_1.CX(3, 0).CX(1, 0)
    condition_circuit_1.Measure(1, 0).add_gate(OpType.Reset, [1])
    condition_circuit_1.Measure(2, 1).add_gate(OpType.Reset, [2])
    condition_circuit_1.Measure(3, 2).add_gate(OpType.Reset, [3])
    condition_circuit_1.Measure(4, 3).add_gate(OpType.Reset, [4])

    nested_conditional_circuit_1 = Circuit(5, 13)
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

    nested_conditional_circuit_1.H(0).Y(0).H(0)
    nested_conditional_circuit_1.H(0).Y(0).H(0)

    nested_conditional_circuit_1.Measure(0, 12).add_gate(OpType.Reset, [0])

    nested_circ_box_1 = CircBox(nested_conditional_circuit_1)
    c_reg = condition_circuit_1.c_registers[0]
    args = list(condition_circuit_1.qubits) + list(condition_circuit_1.bits)
    condition_circuit_1.add_circbox(nested_circ_box_1, args, condition=c_reg[1])

    condition_circuit_1.H(0).Y(0).H(0)
    condition_circuit_1.H(0).Y(0).H(0)
    condition_circuit_1.Measure(0, 12).add_gate(OpType.Reset, [0])

    circ_box_1 = CircBox(condition_circuit_1)
    c_reg = circuit.get_c_register("c")
    args = list(circuit.qubits) + list(circuit.bits)
    circuit.add_circbox(circ_box_1, args, condition=c_reg[0])

    circuit.CX(4, 3).CX(4, 2).CX(3, 2).CX(2, 1).CX(4, 0).CX(3, 0).CX(1, 0)
    circuit.add_gate(OpType.Reset, [1]).Measure(2, 1)
    circuit.add_gate(OpType.Reset, [2]).Measure(3, 2)
    circuit.add_gate(OpType.Reset, [3]).Measure(4, 3)
    circuit.add_gate(OpType.Reset, [4])

    return circuit


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
    c.X(0).X(1)

    # Sub-circuit for condition true
    c1 = Circuit(2)
    c1.H(0).H(1)

    cb1 = CircBox(c1)
    args1 = list(range(c1.n_qubits)) + list(range(len(c1.bits)))
    c.add_circbox(cb1, args1, condition_bits=[0], condition_value=1)

    c.Y(0).Y(1)

    # Sub-circuit for condition false
    c.add_circbox(cb1, args1, condition_bits=[1], condition_value=0)

    c.Z(0).Z(1)

    write_qir_file(c, simple_conditional_file_name)
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
