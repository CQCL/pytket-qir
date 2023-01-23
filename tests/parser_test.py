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

from pathlib import Path
from typing import cast

import pytest

from pytket import Circuit  # type: ignore
from pytket.circuit import OpType  # type: ignore
from pytket.wasm import WasmFileHandler  # type: ignore
from pyqir.parser import QirBlock, QirModule

from pytket_qir.parser import QirParser
from pytket_qir.utils import InstructionError


qir_files_dir = Path("./qir_test_files")


class TestQirToPytketGates:
    """Test all L3 supported gates from QIR to pytket."""

    def test_h_only(self) -> None:
        h_only_bc_file_path = qir_files_dir / "h_only.bc"
        qir_module = QirModule(str(h_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).H(0)
        assert circuit == expected_circuit

    def test_cx_only(self) -> None:
        cx_only_bc_file_path = qir_files_dir / "cx_only.bc"
        qir_module = QirModule(str(cx_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(2)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(2).CX(0, 1)
        assert circuit == expected_circuit

    def test_t_only(self) -> None:
        t_only_bc_file_path = qir_files_dir / "t_only.bc"
        qir_module = QirModule(str(t_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).T(0)
        assert circuit == expected_circuit

    def test_tdg_only(self) -> None:
        tdg_only_bc_file_path = qir_files_dir / "tadj_only.bc"
        qir_module = QirModule(str(tdg_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).Tdg(0)
        assert circuit == expected_circuit

    def test_x_only(self) -> None:
        x_only_bc_file_path = qir_files_dir / "x_only.bc"
        qir_module = QirModule(str(x_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).X(0)
        assert circuit == expected_circuit

    def test_y_only(self) -> None:
        y_only_bc_file_path = qir_files_dir / "y_only.bc"
        qir_module = QirModule(str(y_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).Y(0)
        assert circuit == expected_circuit

    def test_z_only(self) -> None:
        z_only_bc_file_path = qir_files_dir / "z_only.bc"
        qir_module = QirModule(str(z_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).Z(0)
        assert circuit == expected_circuit

    def test_rx_only(self) -> None:
        rx_only_bc_file_path = qir_files_dir / "rx_only.bc"
        qir_module = QirModule(str(rx_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).Rx(-5.497787143782138, 0)
        assert circuit == expected_circuit

    def test_rz_only(self) -> None:
        rz_only_bc_file_path = qir_files_dir / "rz_only.bc"
        qir_module = QirModule(str(rz_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).Rz(-5.497787143782138, 0)
        assert circuit == expected_circuit

    def test_measure_only(self) -> None:
        measure_only_bc_file_path = qir_files_dir / "measure_only.bc"
        qir_module = QirModule(str(measure_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1, 1).Measure(0, 0)
        assert circuit == expected_circuit

    def test_reset_only(self) -> None:
        reset_only_bc_file_path = qir_files_dir / "reset_only.bc"
        qir_module = QirModule(str(reset_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        expected_circuit = Circuit(1).add_gate(OpType.Reset, [0])
        assert circuit == expected_circuit

    def test_grover_circuit(self, grover_circuit: Circuit) -> None:
        grover_bc_file_path = qir_files_dir / "SimpleGroverBaseProfile.bc"
        qir_module = QirModule(str(grover_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(3, 2)
        circuit = parser.block_to_circuit(entry_block, circuit)
        assert circuit == grover_circuit

    def test_wasm_only(self) -> None:
        wasm_only_bc_file_path = qir_files_dir / "wasm_only_test.bc"
        wasm_file_path = qir_files_dir / "wasm_adder.wasm"
        wasm_handler = WasmFileHandler(str(wasm_file_path))
        qir_module = QirModule(str(wasm_only_bc_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module, wasm_handler=wasm_handler)
        circuit = Circuit(1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        com = circuit.get_commands()[0]
        assert com.op.type == OpType.WASM
        assert len(com.args) == 64
        assert circuit.depth() == 1

    def test_untagged_rt_functions(self) -> None:
        rt_function_file_path = qir_files_dir / "untagged_rt_functions.bc"
        qir_module = QirModule(str(rt_function_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(2, 2)
        circuit = parser.block_to_circuit(entry_block, circuit)

        barriers = circuit.commands_of_type(OpType.Barrier)
        assert barriers[0].op.type == OpType.Barrier
        assert (
            barriers[0].op.data
            == '{"name": "__quantum__rt__integer_record_output", "arg": "%0"}'
        )
        assert barriers[0].qubits == []
        assert circuit.get_c_register(
            barriers[0].args[0].reg_name
        ) == circuit.get_c_register("%0")
        assert barriers[1].op.type == OpType.Barrier
        assert (
            barriers[1].op.data
            == '{"name": "__quantum__rt__bool_record_output", "arg": "%1"}'
        )
        assert barriers[1].qubits == []
        assert circuit.get_c_register(
            barriers[1].args[0].reg_name
        ) == circuit.get_c_register("%1")
        assert barriers[2].op.type == OpType.Barrier
        assert (
            barriers[2].op.data
            == '{"name": "__quantum__rt__result_record_output", "arg": 0, "index": 0}'
        )
        assert barriers[2].qubits == []
        assert barriers[2].bits[0].index[0] == 0
        assert barriers[3].op.type == OpType.Barrier
        assert (
            barriers[3].op.data
            == '{"name": "__quantum__rt__result_record_output", "arg": 1, "index": 1}'
        )
        assert barriers[3].qubits == []
        assert barriers[3].bits[0].index[0] == 1

    def test_tagged_rt_functions(self) -> None:
        rt_function_file_path = qir_files_dir / "tagged_rt_functions.bc"
        qir_module = QirModule(str(rt_function_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(2, 2)
        circuit = parser.block_to_circuit(entry_block, circuit)

        barriers = circuit.commands_of_type(OpType.Barrier)

        assert barriers[0].op.type == OpType.Barrier
        assert (
            barriers[0].op.data == '{"name": "__quantum__rt__integer_record_output",'
            ' "arg": "%0", "tag": "0_t2\\u0000"}'
        )
        assert barriers[0].qubits == []
        assert circuit.get_c_register(
            barriers[0].args[0].reg_name
        ) == circuit.get_c_register("%0")
        assert barriers[1].op.type == OpType.Barrier
        assert (
            barriers[1].op.data == '{"name": "__quantum__rt__bool_record_output",'
            ' "arg": "%1", "tag": "0_t3\\u0000"}'
        )
        assert barriers[1].qubits == []
        assert circuit.get_c_register(
            barriers[1].args[0].reg_name
        ) == circuit.get_c_register("%1")
        assert barriers[2].op.type == OpType.Barrier
        assert (
            barriers[2].op.data == '{"name": "__quantum__rt__result_record_output",'
            ' "arg": 0, "index": 0, "tag": "0_t0\\u0000"}'
        )
        assert barriers[2].qubits == []
        assert barriers[2].bits[0].index[0] == 0
        assert barriers[3].op.type == OpType.Barrier
        assert (
            barriers[3].op.data == '{"name": "__quantum__rt__result_record_output",'
            ' "arg": 1, "index": 1, "tag": "0_t1\\u0000"}'
        )
        assert barriers[3].qubits == []
        assert barriers[3].bits[0].index[0] == 1

    def test_select(self) -> None:
        select_function_file_path = qir_files_dir / "select.bc"
        qir_module = QirModule(str(select_function_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)

        output_register = circuit.get_c_register("%1")

        conditionals = []

        for com in circuit.get_commands():
            if (
                com.op.type == OpType.Conditional
            ):  # Raising an error if I use .commands_of_type(OpType.Conditional)
                conditionals.append(com)

        conditional0 = conditionals[0]
        assert conditional0.op.type == OpType.Conditional
        assert conditional0.bits == list(output_register)
        assert conditional0.op.value == 1
        assert sum([n * 2**k for k, n in enumerate(conditional0.op.op.values)]) == 99

        conditional1 = conditionals[1]
        assert conditional1.op.type == OpType.Conditional
        assert conditional1.bits == list(output_register)
        assert conditional1.op.value == 0
        assert sum([n * 2**k for k, n in enumerate(conditional1.op.op.values)]) == 22

    def test_zext(self) -> None:
        zext_function_file_path = qir_files_dir / "zext.bc"
        qir_module = QirModule(str(zext_function_file_path))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)

        output_reg = circuit.get_c_register("%0")

        barrier = circuit.get_commands()[0]
        assert barrier.bits == list(output_reg)
        assert barrier.op.data == '{"name": "zext"}'


class TestQirToPytketClassicalOps:
    """
    A class to test the translation from classical operations
    to pytket circuit model.
    """

    def test_add_only(self) -> None:
        add_only_bc_file = qir_files_dir / "add_only.bc"
        qir_module = QirModule(str(add_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " + " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_sub_only(self) -> None:
        sub_only_bc_file = qir_files_dir / "sub_only.bc"
        qir_module = QirModule(str(sub_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " - " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_mul_only(self) -> None:
        mul_only_bc_file = qir_files_dir / "mul_only.bc"
        qir_module = QirModule(str(mul_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " * " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_div_only(self) -> None:
        div_only_bc_file = qir_files_dir / "div_only.bc"
        qir_module = QirModule(str(div_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " / " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_shl_only(self) -> None:
        shl_only_bc_file = qir_files_dir / "shl_only.bc"
        qir_module = QirModule(str(shl_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " << " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_lshr_only(self) -> None:
        lshr_only_bc_file = qir_files_dir / "lshr_only.bc"
        qir_module = QirModule(str(lshr_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " >> " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_eq_only(self) -> None:
        eq_only_bc_file = qir_files_dir / "eq_only.bc"
        qir_module = QirModule(str(eq_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " == 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_neq_only(self) -> None:
        neq_only_bc_file = qir_files_dir / "neq_only.bc"
        qir_module = QirModule(str(neq_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " != 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_ule_only(self) -> None:
        ule_only_bc_file = qir_files_dir / "ule_only.bc"
        qir_module = QirModule(str(ule_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " <= 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_uge_only(self) -> None:
        uge_only_bc_file = qir_files_dir / "uge_only.bc"
        qir_module = QirModule(str(uge_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " >= 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_ult_only(self) -> None:
        ult_only_bc_file = qir_files_dir / "ult_only.bc"
        qir_module = QirModule(str(ult_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " < 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_ugt_only(self) -> None:
        ugt_only_bc_file = qir_files_dir / "ugt_only.bc"
        qir_module = QirModule(str(ugt_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " > 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_neg_only(self) -> None:
        neg_only_bc_file = qir_files_dir / "neg_only.bc"
        qir_module = QirModule(str(neg_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_box = circuit.get_commands()[0]
        assert str(c_box.op.get_exp()) == "(- 2)"

    def test_and_only(self) -> None:
        and_only_bc_file = qir_files_dir / "and_only.bc"
        qir_module = QirModule(str(and_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " & " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_or_only(self) -> None:
        or_only_bc_file = qir_files_dir / "or_only.bc"
        qir_module = QirModule(str(or_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " | " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_xor_only(self) -> None:
        xor_only_bc_file = qir_files_dir / "xor_only.bc"
        qir_module = QirModule(str(xor_only_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " ^ " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_purely_classical(self) -> None:
        purely_classical_file = qir_files_dir / "purely_classical.bc"
        qir_module = QirModule(str(purely_classical_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        circuit = parser.block_to_circuit(entry_block, circuit)
        coms = circuit.get_commands()

        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[7] + " + " + c_reg_names[8] + ")"
        assert str(coms[2].op.get_exp()) == reconstructed_expr

        reconstructed_expr = "(" + c_reg_names[0] + " + " + c_reg_names[8] + ")"
        assert str(coms[5].op.get_exp()) == reconstructed_expr

        reconstructed_expr = "(" + c_reg_names[7] + " - " + c_reg_names[8] + ")"
        assert str(coms[7].op.get_exp()) == reconstructed_expr

        reconstructed_expr = "(" + c_reg_names[2] + " + " + c_reg_names[8] + ")"
        assert str(coms[9].op.get_exp()) == reconstructed_expr

        reconstructed_expr = "(" + c_reg_names[3] + " + " + c_reg_names[1] + ")"
        assert str(coms[10].op.get_exp()) == reconstructed_expr

        reconstructed_expr = "(" + c_reg_names[1] + " - " + c_reg_names[3] + ")"
        assert str(coms[11].op.get_exp()) == reconstructed_expr

    def test_not_supported_op(self) -> None:
        not_supported_bc_file = qir_files_dir / "not_supported.bc"
        qir_module = QirModule(str(not_supported_bc_file))
        entry_block = cast(QirBlock, qir_module.functions[0].get_block_by_name("entry"))
        parser = QirParser(qir_module)
        circuit = Circuit(1, 1)
        with pytest.raises(InstructionError):
            circuit = parser.block_to_circuit(entry_block, circuit)
