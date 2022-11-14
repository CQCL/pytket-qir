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
import pytest  # type: ignore
from pytket import Circuit, OpType  # type: ignore
from pytket.circuit import Conditional  # type: ignore
from pytket.wasm import WasmFileHandler  # type: ignore

from pytket_qir.parser import circuit_from_qir
from pytket_qir.utils import InstructionError


qir_files_dir = Path("./qir_test_files")


class TestQirToPytketGateTranslation:
    """A class to test all L3 supported gates from QIR to pytket gate model."""

    def test_h_only(self) -> None:
        h_only_bc_file_path = qir_files_dir / "h_only.bc"
        circuit = circuit_from_qir(h_only_bc_file_path)
        expected_circuit = Circuit(1).H(0)
        assert circuit == expected_circuit

    def test_cx_only(self) -> None:
        cx_only_bc_file_path = qir_files_dir / "cx_only.bc"
        circuit = circuit_from_qir(cx_only_bc_file_path)
        expected_circuit = Circuit(2).CX(0, 1)
        assert circuit == expected_circuit

    def test_t_only(self) -> None:
        t_only_bc_file_path = qir_files_dir / "t_only.bc"
        circuit = circuit_from_qir(t_only_bc_file_path)
        expected_circuit = Circuit(1).T(0)
        assert circuit == expected_circuit

    def test_tdg_only(self) -> None:
        tdg_only_bc_file_path = qir_files_dir / "tadj_only.bc"
        circuit = circuit_from_qir(tdg_only_bc_file_path)
        expected_circuit = Circuit(1).Tdg(0)
        assert circuit == expected_circuit

    def test_x_only(self) -> None:
        x_only_bc_file_path = qir_files_dir / "x_only.bc"
        circuit = circuit_from_qir(x_only_bc_file_path)
        expected_circuit = Circuit(1).X(0)
        assert circuit == expected_circuit

    def test_y_only(self) -> None:
        y_only_bc_file_path = qir_files_dir / "y_only.bc"
        circuit = circuit_from_qir(y_only_bc_file_path)
        expected_circuit = Circuit(1).Y(0)
        assert circuit == expected_circuit

    def test_z_only(self) -> None:
        z_only_bc_file_path = qir_files_dir / "z_only.bc"
        circuit = circuit_from_qir(z_only_bc_file_path)
        expected_circuit = Circuit(1).Z(0)
        assert circuit == expected_circuit

    def test_rx_only(self) -> None:
        rx_only_bc_file_path = qir_files_dir / "rx_only.bc"
        circuit = circuit_from_qir(rx_only_bc_file_path)
        expected_circuit = Circuit(1).Rx(-5.497787143782138, 0)
        assert circuit == expected_circuit

    def test_rz_only(self) -> None:
        rz_only_bc_file_path = qir_files_dir / "rz_only.bc"
        circuit = circuit_from_qir(rz_only_bc_file_path)
        expected_circuit = Circuit(1).Rz(-5.497787143782138, 0)
        assert circuit == expected_circuit

    def test_measure_only(self) -> None:
        measure_only_bc_file_path = qir_files_dir / "measure_only.bc"
        circuit = circuit_from_qir(measure_only_bc_file_path)
        expected_circuit = Circuit(1, 1).Measure(0, 0)
        assert circuit == expected_circuit

    def test_reset_only(self) -> None:
        reset_only_bc_file_path = qir_files_dir / "reset_only.bc"
        circuit = circuit_from_qir(reset_only_bc_file_path)
        expected_circuit = Circuit(1).add_gate(OpType.Reset, [0])
        assert circuit == expected_circuit

    def test_grover_circuit(self, grover_circuit: Circuit) -> None:
        grover_bc_file_path = qir_files_dir / "SimpleGroverBaseProfile.bc"
        circuit = circuit_from_qir(grover_bc_file_path)
        assert circuit == grover_circuit

    def test_wasm_only(self) -> None:
        wasm_only_bc_file_path = qir_files_dir / "wasm_only_test.bc"
        wasm_file_path = qir_files_dir / "wasm_adder.wasm"
        wasm_handler = WasmFileHandler(str(wasm_file_path))
        circuit = circuit_from_qir(wasm_only_bc_file_path, wasm_handler=wasm_handler)
        com = circuit.get_commands()[0]
        assert com.op.type == OpType.WASM
        assert len(com.args) == 64
        assert circuit.depth() == 1

    def test_untagged_rt_functions(self) -> None:
        rt_function_file_path = qir_files_dir / "untagged_rt_functions.bc"
        circuit = circuit_from_qir(rt_function_file_path)

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
            == '{"name": "__quantum__rt__result_record_output", "arg": 0}'
        )
        assert barriers[2].qubits == []
        assert barriers[2].bits[0].index[0] == 0
        assert barriers[3].op.type == OpType.Barrier
        assert (
            barriers[3].op.data
            == '{"name": "__quantum__rt__result_record_output", "arg": 1}'
        )
        assert barriers[3].qubits == []
        assert barriers[3].bits[0].index[0] == 1

    def test_tagged_rt_functions(self) -> None:
        rt_function_file_path = qir_files_dir / "tagged_rt_functions.bc"
        circuit = circuit_from_qir(rt_function_file_path)

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
            ' "arg": 0, "tag": "0_t0\\u0000"}'
        )
        assert barriers[2].qubits == []
        assert barriers[2].bits[0].index[0] == 0
        assert barriers[3].op.type == OpType.Barrier
        assert (
            barriers[3].op.data == '{"name": "__quantum__rt__result_record_output",'
            ' "arg": 1, "tag": "0_t1\\u0000"}'
        )
        assert barriers[3].qubits == []
        assert barriers[3].bits[0].index[0] == 1

    def test_select(self) -> None:
        select_function_file_path = qir_files_dir / "select.bc"

        circuit = circuit_from_qir(select_function_file_path)
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
        zext_function_file_path = qir_files_dir / "zext.ll"

        circuit = circuit_from_qir(zext_function_file_path)
        output_reg = circuit.get_c_register("%0")

        barrier = circuit.get_commands()[0]
        assert barrier.bits == list(output_reg)
        assert barrier.op.data == '{"name": "zext"}'


class TestQirToPytketConditionals:
    """A class to test circuit translation containing conditionals."""

    def test_single_conditional(self, one_conditional_circuit: Circuit) -> None:
        one_conditional_bc_path = qir_files_dir / "one_conditional.bc"

        circuit = circuit_from_qir(one_conditional_bc_path)

        non_condition_circuit = Circuit(circuit.n_qubits, circuit.n_bits)
        for com in circuit.get_commands()[:15]:
            non_condition_circuit.add_gate(com.op, com.args)

        exp_non_condition_circuit = Circuit(circuit.n_qubits, circuit.n_bits)
        for com in one_conditional_circuit.get_commands()[:15]:
            exp_non_condition_circuit.add_gate(com.op, com.args)

        assert non_condition_circuit == exp_non_condition_circuit

        condition_com = circuit.get_commands()[15]

        inverse_reg_map = {v: k for k, v in circuit._reg_map.items()}
        assert inverse_reg_map[condition_com.args[0]].reg_name == "%0"

        condition_circuit = condition_com.op.op.get_circuit()

        exp_condition_com = one_conditional_circuit.get_commands()[15]
        exp_condition_circuit = exp_condition_com.op.op.get_circuit()

        # Comparing commands as I get a type error while comparing circuits.
        # TypeError: unhashable type: 'instancemethod'.
        for com1, com2 in zip(
            condition_circuit.get_commands(), exp_condition_circuit.get_commands()
        ):
            assert com1 == com2

        final_circuit = Circuit(5, 13)
        for com in circuit.get_commands()[16:]:
            final_circuit.add_gate(com.op, com.args)

        exp_final_circuit = Circuit(5, 13)
        for com in one_conditional_circuit.get_commands()[16:]:
            exp_final_circuit.add_gate(com.op, com.args)

        assert final_circuit == exp_final_circuit

    def test_multiple_successive_conditionals(
        self,
        multiple_conditionals_circuit,
    ) -> None:
        multiple_conditionals_bc_file_path = (
            qir_files_dir / "teleportchain_baseprofile.bc"
        )

        circuit = circuit_from_qir(multiple_conditionals_bc_file_path)

        non_condition_circuit = Circuit(circuit.n_qubits, circuit.n_bits)
        for com in circuit.get_commands()[:10]:
            non_condition_circuit.add_gate(com.op, com.args)

        exp_non_condition_circuit = Circuit(circuit.n_qubits, circuit.n_bits)
        for com in multiple_conditionals_circuit.get_commands()[:10]:
            exp_non_condition_circuit.add_gate(com.op, com.args)

        assert non_condition_circuit == exp_non_condition_circuit

        condition_com_1 = circuit.get_commands()[10]

        inverse_reg_map = {v: k for k, v in circuit._reg_map.items()}
        assert inverse_reg_map[condition_com_1.args[0]].reg_name == "%0"

        condition_circuit_1 = condition_com_1.op.op.get_circuit()
        condition_circuit_1_coms = condition_circuit_1.get_commands()

        exp_condition_com_1 = multiple_conditionals_circuit.get_commands()[10]
        exp_condition_circuit_1 = exp_condition_com_1.op.op.get_circuit()
        exp_condition_circuit_1_coms = exp_condition_circuit_1.get_commands()

        non_condition_circuit_1 = Circuit(6, 262)
        exp_non_condition_circuit_1 = Circuit(6, 262)

        for com in condition_circuit_1_coms:
            if not isinstance(com.op, Conditional):
                non_condition_circuit_1.add_gate(com.op, com.args)

        for com in exp_condition_circuit_1_coms:
            if not isinstance(com.op, Conditional):
                exp_non_condition_circuit_1.add_gate(com.op, com.args)

        assert non_condition_circuit_1 == exp_non_condition_circuit_1

        condition_circuit_1_1_coms = (
            condition_circuit_1_coms[3].op.op.get_circuit().get_commands()
        )
        exp_condition_circuit_1_1_coms = (
            exp_condition_circuit_1_coms[3].op.op.get_circuit().get_commands()
        )
        non_condition_circuit_1_1 = Circuit(6, 262)
        exp_non_condition_circuit_1_1 = Circuit(6, 262)

        assert inverse_reg_map[condition_circuit_1_coms[3].args[0]].reg_name == "%1"

        for com in condition_circuit_1_1_coms:
            if not isinstance(com.op, Conditional):
                non_condition_circuit_1_1.add_gate(com.op, com.args)

        for com in exp_condition_circuit_1_1_coms:
            if not isinstance(com.op, Conditional):
                exp_non_condition_circuit_1_1.add_gate(com.op, com.args)

        assert non_condition_circuit_1_1 == exp_non_condition_circuit_1_1

        condition_circuit_1_1_1_coms = (
            condition_circuit_1_1_coms[5].op.op.get_circuit().get_commands()
        )
        exp_condition_circuit_1_1_1_coms = (
            exp_condition_circuit_1_1_coms[5].op.op.get_circuit().get_commands()
        )
        non_condition_circuit_1_1_1 = Circuit(6, 262)
        exp_non_condition_circuit_1_1_1 = Circuit(6, 262)

        assert inverse_reg_map[condition_circuit_1_1_coms[5].args[0]].reg_name == "%2"

        for com in condition_circuit_1_1_1_coms:
            if not isinstance(com.op, Conditional):
                non_condition_circuit_1_1_1.add_gate(com.op, com.args)

        for com in exp_condition_circuit_1_1_1_coms:
            if not isinstance(com.op, Conditional):
                exp_non_condition_circuit_1_1_1.add_gate(com.op, com.args)

        assert non_condition_circuit_1_1_1 == exp_non_condition_circuit_1_1_1

        condition_circuit_1_1_1_1_coms = (
            condition_circuit_1_1_1_coms[3].op.op.get_circuit().get_commands()
        )
        exp_condition_circuit_1_1_1_1_coms = (
            exp_condition_circuit_1_1_1_coms[3].op.op.get_circuit().get_commands()
        )
        non_condition_circuit_1_1_1_1 = Circuit(6, 6)
        exp_non_condition_circuit_1_1_1_1 = Circuit(6, 6)

        assert inverse_reg_map[condition_circuit_1_1_1_coms[3].args[0]].reg_name == "%3"

        for com in condition_circuit_1_1_1_1_coms:
            if not isinstance(com.op, Conditional):
                non_condition_circuit_1_1_1_1.add_gate(com.op, com.args)

        for com in exp_condition_circuit_1_1_1_1_coms:
            if not isinstance(com.op, Conditional):
                exp_non_condition_circuit_1_1_1_1.add_gate(com.op, com.args)

        assert non_condition_circuit_1_1_1_1 == exp_non_condition_circuit_1_1_1_1

    def test_nested_conditionals(
        self,
        nested_conditionals_circuit: Circuit,
    ) -> None:
        nested_conditionals_bc_file_path = qir_files_dir / "nested_conditionals.bc"
        circuit = circuit_from_qir(nested_conditionals_bc_file_path)

        non_condition_circuit = Circuit(5, 205)
        for com in circuit.get_commands()[:15]:
            non_condition_circuit.add_gate(com.op, com.args)

        exp_non_condition_circuit = Circuit(5, 205)
        for com in nested_conditionals_circuit.get_commands()[:15]:
            exp_non_condition_circuit.add_gate(com.op, com.args)

        assert non_condition_circuit == exp_non_condition_circuit

        condition_circuit_1 = circuit.get_commands()[15].op.op.get_circuit()
        exp_condition_circuit_1 = nested_conditionals_circuit.get_commands()[
            15
        ].op.op.get_circuit()

        inverse_reg_map = {v: k for k, v in circuit._reg_map.items()}
        assert inverse_reg_map[circuit.get_commands()[15].args[0]].reg_name == "%0"

        non_condition_circuit_1 = Circuit(5, 205)
        coms = condition_circuit_1.get_commands()
        del coms[15]
        for com in coms:
            non_condition_circuit_1.add_gate(com.op, com.args)

        exp_non_condition_circuit_1 = Circuit(5, 205)
        coms = exp_condition_circuit_1.get_commands()
        del coms[15]
        for com in coms:
            exp_non_condition_circuit_1.add_gate(com.op, com.args)

        assert non_condition_circuit_1 == exp_non_condition_circuit_1

        nested_conditional_circuit_1 = condition_circuit_1.get_commands()[
            15
        ].op.op.get_circuit()
        exp_nested_conditional_circuit_1 = exp_condition_circuit_1.get_commands()[
            15
        ].op.op.get_circuit()

        assert (
            inverse_reg_map[condition_circuit_1.get_commands()[15].args[0]].reg_name
            == "%1"
        )

        for com1, com2 in zip(
            nested_conditional_circuit_1.get_commands(),
            exp_nested_conditional_circuit_1.get_commands(),
        ):
            assert com1 == com2

        inter_circuit = Circuit(5, 205)
        for com in circuit.get_commands()[16:30]:
            inter_circuit.add_gate(com.op, com.args)

        exp_inter_circuit = Circuit(5, 205)
        for com in nested_conditionals_circuit.get_commands()[16:30]:
            exp_inter_circuit.add_gate(com.op, com.args)

        for com1, com2 in zip(
            inter_circuit.get_commands(), exp_inter_circuit.get_commands()
        ):
            assert com1 == com2

        assert inverse_reg_map[circuit.get_commands()[30].args[0]].reg_name == "c"
        assert inverse_reg_map[circuit.get_commands()[30].args[0]].index[0] == 2


class TestQirToPytketClassicalOps:
    """
    A class to test the translation from classical operations
    to pytket circuit model.
    """

    def test_add_only(self) -> None:
        add_only_bc_file = qir_files_dir / "add_only.bc"
        circuit = circuit_from_qir(add_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " + " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_sub_only(self) -> None:
        sub_only_bc_file = qir_files_dir / "sub_only.bc"
        circuit = circuit_from_qir(sub_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " - " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_mul_only(self) -> None:
        mul_only_bc_file = qir_files_dir / "mul_only.bc"
        circuit = circuit_from_qir(mul_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " * " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_div_only(self) -> None:
        div_only_bc_file = qir_files_dir / "div_only.bc"
        circuit = circuit_from_qir(div_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " / " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_shl_only(self) -> None:
        shl_only_bc_file = qir_files_dir / "shl_only.bc"
        circuit = circuit_from_qir(shl_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " << " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_lshr_only(self) -> None:
        lshr_only_bc_file = qir_files_dir / "lshr_only.bc"
        circuit = circuit_from_qir(lshr_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " >> " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_eq_only(self) -> None:
        eq_only_bc_file = qir_files_dir / "eq_only.bc"
        circuit = circuit_from_qir(eq_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " == 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_neq_only(self) -> None:
        neq_only_bc_file = qir_files_dir / "neq_only.bc"
        circuit = circuit_from_qir(neq_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " != 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_ule_only(self) -> None:
        ule_only_bc_file = qir_files_dir / "ule_only.bc"
        circuit = circuit_from_qir(ule_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " <= 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_uge_only(self) -> None:
        uge_only_bc_file = qir_files_dir / "uge_only.bc"
        circuit = circuit_from_qir(uge_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " >= 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_ult_only(self) -> None:
        ult_only_bc_file = qir_files_dir / "ult_only.bc"
        circuit = circuit_from_qir(ult_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " < 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_ugt_only(self) -> None:
        ugt_only_bc_file = qir_files_dir / "ugt_only.bc"
        circuit = circuit_from_qir(ugt_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " > 3)"
        c_box = circuit.get_commands()[1]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_neg_only(self) -> None:
        neg_only_bc_file = qir_files_dir / "neg_only.bc"
        circuit = circuit_from_qir(neg_only_bc_file)
        c_box = circuit.get_commands()[0]
        assert str(c_box.op.get_exp()) == "(- 2)"

    def test_and_only(self) -> None:
        and_only_bc_file = qir_files_dir / "and_only.bc"
        circuit = circuit_from_qir(and_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " & " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_or_only(self) -> None:
        or_only_bc_file = qir_files_dir / "or_only.bc"
        circuit = circuit_from_qir(or_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " | " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_xor_only(self) -> None:
        xor_only_bc_file = qir_files_dir / "xor_only.bc"
        circuit = circuit_from_qir(xor_only_bc_file)
        c_reg_names = [reg.name for reg in circuit.c_registers]
        reconstructed_expr = "(" + c_reg_names[2] + " ^ " + c_reg_names[3] + ")"
        c_box = circuit.get_commands()[2]
        assert str(c_box.op.get_exp()) == reconstructed_expr

    def test_purely_classical(self) -> None:
        purely_classical_file = qir_files_dir / "purely_classical.bc"
        circuit = circuit_from_qir(purely_classical_file)
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

    def test_classical_and_controlflow(self) -> None:
        classical_and_controlflow_file = qir_files_dir / "classical_and_controlflow.bc"
        circuit = circuit_from_qir(classical_and_controlflow_file)
        com0 = circuit.get_commands()[0]
        assert sum([n * 2**k for k, n in enumerate(com0.op.values)]) == 1
        com1 = circuit.get_commands()[1]
        assert sum([n * 2**k for k, n in enumerate(com1.op.values)]) == 2
        com2 = circuit.get_commands()[2]
        assert str(com2.op.get_exp()) == "(c_reg_1 + c_reg_2)"
        com3 = circuit.get_commands()[3]
        assert sum([n * 2**k for k, n in enumerate(com3.op.values)]) == 4
        com4 = circuit.get_commands()[4]
        assert sum([n * 2**k for k, n in enumerate(com4.op.values)]) == 3
        com5 = circuit.get_commands()[5]
        assert str(com5.op.get_exp()) == "(%0 + c_reg_2)"
        com6 = circuit.get_commands()[6]
        assert sum([n * 2**k for k, n in enumerate(com6.op.values)]) == 2
        com7 = circuit.get_commands()[7]
        assert str(com7.op.get_exp()) == "(c_reg_1 - c_reg_2)"
        # com8 is the conditional box handled below.
        com9 = circuit.get_commands()[9]
        assert str(com9.op.get_exp()) == "(%1 - %2)"
        com10 = circuit.get_commands()[10]
        assert com10.op.type == OpType.H
        com11 = circuit.get_commands()[11]
        assert com11.op.type == OpType.Measure
        com12 = circuit.get_commands()[12]
        assert com12.op.type == OpType.Reset

        classical_boxes = []
        for com in circuit.get_commands():
            if com.op.type == OpType.Conditional:
                classical_boxes.append(com)

        subcoms = classical_boxes[0].op.op.get_circuit().get_commands()

        assert str(subcoms[0].op.get_exp()) == "(%1 - %2)"
        com1 = subcoms[1]
        assert sum([n * 2**k for k, n in enumerate(com1.op.values)]) == 1
        com2 = subcoms[2]
        assert com2.op.type == OpType.Z
        com3 = subcoms[3]
        assert str(com3.op.get_exp()) == "(%2 + c_reg_2)"
        com4 = subcoms[4]
        assert com4.op.type == OpType.H
        com5 = subcoms[5]
        assert str(com5.op.get_exp()) == "(%4 + %1)"
        com6 = subcoms[6]
        assert com6.op.type == OpType.Measure
        com7 = subcoms[7]
        assert str(com7.op.get_exp()) == "(%1 - %5)"
        com8 = subcoms[8]
        assert com8.op.type == OpType.Reset

    def test_wasm_and_controlflow(self) -> None:
        wasm_file_path = qir_files_dir / "wasm_adder.wasm"
        wasm_handler = WasmFileHandler(str(wasm_file_path))
        wasm_and_controlflow_file = qir_files_dir / "wasm_and_controlflow.bc"
        circuit = circuit_from_qir(wasm_and_controlflow_file, wasm_handler=wasm_handler)

        coms = circuit.get_commands()
        com0 = coms[0]
        assert sum([n * 2**k for k, n in enumerate(com0.op.values)]) == 0
        com1 = coms[1]
        assert sum([n * 2**k for k, n in enumerate(com1.op.values)]) == 3
        com2 = coms[2]
        assert sum([n * 2**k for k, n in enumerate(com2.op.values)]) == 4
        com3 = coms[3]
        assert str(com3.op.get_exp()) == "(c_reg_1 + c_reg_2)"
        com5 = coms[5]
        assert sum([n * 2**k for k, n in enumerate(com5.op.values)]) == 2
        com6 = coms[6]
        assert str(com6.op.get_exp()) == "(%1 + c_reg_2)"

        inverse_reg_map = {v: k for k, v in circuit._reg_map.items()}

        com4 = coms[4]
        # Check the condition bit is correct before flattening.
        assert inverse_reg_map[com4.args[0]].reg_name == "%2"

        subcircuit = coms[4].op.op.get_circuit()

        coms = subcircuit.get_commands()

        com0 = coms[0]
        assert com0.op.type == OpType.WASM
        assert com0.op.func_name == "add_one"
        com1 = coms[1]
        assert sum([n * 2**k for k, n in enumerate(com1.op.values)]) == 2
        com2 = coms[2]
        assert str(com2.op.get_exp()) == "(%1 + c_reg_2)"

    def test_select_and_controlflow(self) -> None:
        select_and_controlflow_file = qir_files_dir / "select_and_controlflow.bc"
        circuit = circuit_from_qir(select_and_controlflow_file)

        inverse_reg_map = {v: k for k, v in circuit._reg_map.items()}
        coms = circuit.get_commands()
        com0 = coms[0]
        assert sum([n * 2**k for k, n in enumerate(com0.op.values)]) == 1
        com1 = coms[1]
        assert sum([n * 2**k for k, n in enumerate(com1.op.values)]) == 0
        com2 = coms[2]
        assert str(com2.op.get_exp()) == "(c_reg_1 + c_reg_2)"
        com3 = coms[3]
        assert sum([n * 2**k for k, n in enumerate(com3.op.values)]) == 3
        com4 = coms[4]
        assert sum([n * 2**k for k, n in enumerate(com4.op.values)]) == 4
        com5 = coms[5]
        assert str(com5.op.get_exp()) == "(c_reg_1 + c_reg_2)"
        com6 = coms[6]

        assert inverse_reg_map[com6.args[0]].reg_name == "%2"

        com7 = coms[7]
        assert sum([n * 2**k for k, n in enumerate(com7.op.values)]) == 2
        com8 = coms[8]
        assert str(com8.op.get_exp()) == "(%1 + c_reg_2)"

        condition_circuit = com6.op.op.get_circuit()
        coms = condition_circuit.get_commands()

        com0 = coms[0]
        assert inverse_reg_map[com0.args[0]].reg_name == "%0"
        assert sum([n * 2**k for k, n in enumerate(com0.op.op.values)]) == 99
        com1 = coms[1]
        assert sum([n * 2**k for k, n in enumerate(com1.op.values)]) == 2
        com2 = coms[2]
        assert sum([n * 2**k for k, n in enumerate(com2.op.op.values)]) == 22
        com3 = coms[3]
        assert str(com3.op.get_exp()) == "(%1 + c_reg_2)"

    def test_not_supported_op(self) -> None:
        not_supported_bc_file = qir_files_dir / "not_supported.bc"
        with pytest.raises(InstructionError):
            circuit_from_qir(not_supported_bc_file)