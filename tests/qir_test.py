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
from typing import Generator, List
import pytest  # type: ignore
from pytket import Circuit, OpType  # type: ignore
from pytket.circuit import Conditional  # type: ignore
from pytket.wasm import WasmFileHandler  # type: ignore

from pyqir.generator import bitcode_to_ir  # type: ignore

from pytket_qir.qir import (
    circuit_to_pyqir_module,
    write_qir_file,
    circuit_from_qir,
)
from pytket_qir.utils.utils import QIRFormat  # type: ignore


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
        wasm_file_path = qir_files_dir / "wasm_file.wasm"
        wasm_handler = WasmFileHandler(str(wasm_file_path))
        circuit = circuit_from_qir(wasm_only_bc_file_path, wasm_handler=wasm_handler)
        assert circuit.depth() == 1


class TestQirToPytketConditionals:
    """A class to test circuit translation containing conditionals."""

    def test_single_conditional(self, one_conditional_circuit: Circuit) -> None:
        one_conditional_bc_path = qir_files_dir / "one_conditional.bc"

        circuit = circuit_from_qir(one_conditional_bc_path)

        non_condition_circuit = Circuit(5, 13)
        for com in circuit.get_commands()[:15]:
            non_condition_circuit.add_gate(com.op, com.args)

        exp_non_condition_circuit = Circuit(5, 13)
        for com in one_conditional_circuit.get_commands()[:15]:
            exp_non_condition_circuit.add_gate(com.op, com.args)

        assert non_condition_circuit == exp_non_condition_circuit

        condition_com = circuit.get_commands()[15]
        condition_circuit = condition_com.op.op.get_circuit()

        exp_condition_com = one_conditional_circuit.get_commands()[15]
        exp_condition_circuit = exp_condition_com.op.op.get_circuit()

        assert condition_circuit == exp_condition_circuit

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

        non_condition_circuit = Circuit(6, 6)
        for com in circuit.get_commands()[:10]:
            non_condition_circuit.add_gate(com.op, com.args)

        exp_non_condition_circuit = Circuit(6, 6)
        for com in multiple_conditionals_circuit.get_commands()[:10]:
            exp_non_condition_circuit.add_gate(com.op, com.args)

        assert non_condition_circuit == exp_non_condition_circuit

        condition_com_1 = circuit.get_commands()[10]
        condition_circuit_1 = condition_com_1.op.op.get_circuit()
        condition_circuit_1_coms = condition_circuit_1.get_commands()

        exp_condition_com_1 = multiple_conditionals_circuit.get_commands()[10]
        exp_condition_circuit_1 = exp_condition_com_1.op.op.get_circuit()
        exp_condition_circuit_1_coms = exp_condition_circuit_1.get_commands()

        non_condition_circuit_1 = Circuit(6, 6)
        exp_non_condition_circuit_1 = Circuit(6, 6)

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
        non_condition_circuit_1_1 = Circuit(6, 6)
        exp_non_condition_circuit_1_1 = Circuit(6, 6)

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
        non_condition_circuit_1_1_1 = Circuit(6, 6)
        exp_non_condition_circuit_1_1_1 = Circuit(6, 6)

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

        non_condition_circuit = Circuit(5, 13)
        for com in circuit.get_commands()[:15]:
            non_condition_circuit.add_gate(com.op, com.args)

        exp_non_condition_circuit = Circuit(5, 13)
        for com in nested_conditionals_circuit.get_commands()[:15]:
            exp_non_condition_circuit.add_gate(com.op, com.args)

        assert non_condition_circuit == exp_non_condition_circuit

        condition_circuit_1 = circuit.get_commands()[15].op.op.get_circuit()
        exp_condition_circuit_1 = nested_conditionals_circuit.get_commands()[
            15
        ].op.op.get_circuit()

        non_condition_circuit_1 = Circuit(5, 13)
        coms = condition_circuit_1.get_commands()
        del coms[15]
        for com in coms:
            non_condition_circuit_1.add_gate(com.op, com.args)

        exp_non_condition_circuit_1 = Circuit(5, 13)
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

        assert nested_conditional_circuit_1 == exp_nested_conditional_circuit_1

        inter_circuit = Circuit(5, 13)
        for com in circuit.get_commands()[16:30]:
            inter_circuit.add_gate(com.op, com.args)

        exp_inter_circuit = Circuit(5, 13)
        for com in nested_conditionals_circuit.get_commands()[16:30]:
            exp_inter_circuit.add_gate(com.op, com.args)

        assert inter_circuit == exp_inter_circuit


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

    def test_not_supported_op(self) -> None:
        not_supported_bc_file = qir_files_dir / "not_supported.bc"
        with pytest.raises(ValueError):
            circuit_from_qir(not_supported_bc_file)


class TestPytketToQirGateTranslation:
    """A class to test the gate translation from a pytket circuit to a QIR program."""

    def test_raise_pyqir_gateset_keyerror(self) -> None:
        c = Circuit(2)
        c.CY(0, 1)
        with pytest.raises(KeyError):
            write_qir_file(c, "RaiseError.ll")

    def test_qir_from_pytket_circuit_and_pyqir_gateset(
        self, circuit_pyqir_gateset: Generator
    ) -> None:
        with open("SimpleCircuit.ll", "r") as input_file:
            data = input_file.read()
        call_h = f"call void @__quantum__qis__h__body(%Qubit* null)"
        call_x = (
            f"call void @__quantum__qis__x__body(%Qubit* inttoptr (i64 1 to %Qubit*))"
        )
        call_y = f"call void @__quantum__qis__y__body(%Qubit* null)"
        call_z = (
            f"call void @__quantum__qis__z__body(%Qubit* inttoptr (i64 1 to %Qubit*))"
        )
        call_s = f"call void @__quantum__qis__s__body(%Qubit* null)"
        call_s_adj = (
            f"call void @__quantum__qis__s__adj(%Qubit* inttoptr (i64 1 to %Qubit*))"
        )
        call_t = f"call void @__quantum__qis__t__body(%Qubit* null)"
        call_t_adj = (
            f"call void @__quantum__qis__t__adj(%Qubit* inttoptr (i64 1 to %Qubit*))"
        )
        call_reset = f"call void @__quantum__qis__reset__body(%Qubit* null)"
        call_cnot = (
            f"call void @__quantum__qis__cnot__body("
            "%Qubit* null, %Qubit* inttoptr (i64 1 to %Qubit*)"
            ")"
        )
        call_cz = (
            f"call void @__quantum__qis__cz__body("
            "%Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* null"
            ")"
        )
        call_rx = (
            f"call void @__quantum__qis__rx__body("
            "double 0.000000e+00, %Qubit* inttoptr (i64 1 to %Qubit*)"
            ")"
        )
        call_ry = (
            f"call void @__quantum__qis__ry__body(double 1.000000e+00, %Qubit* null)"
        )
        call_rz = (
            f"call void @__quantum__qis__rz__body("
            "double 2.000000e+00, %Qubit* inttoptr (i64 1 to %Qubit*)"
            ")"
        )
        call_m = (
            f"call void @__quantum__qis__mz__body("
            "%Qubit* inttoptr (i64 1 to %Qubit*),"
            " %Result* inttoptr (i64 1 to %Result*)"
            ")"
        )
        assert call_h in data
        assert call_x in data
        assert call_y in data
        assert call_z in data
        assert call_s in data
        assert call_s_adj in data
        assert call_t in data
        assert call_t_adj in data
        assert call_reset in data
        assert call_cnot in data
        assert call_cz in data
        assert call_m in data
        assert call_rx in data
        assert call_ry in data
        assert call_rz in data

    def test_classical_arithmetic(
        self, circuit_classical_arithmetic: Circuit, operators: List
    ):
        with open("ClassicalCircuit.ll", "r") as input_file:
            data = input_file.readlines()

        with open(qir_files_dir / "ClassicalCircuit.ll", "r") as input_file:
           exp_data = input_file.readlines()

        for line in data:
            assert (
                line in exp_data
            )

    @pytest.mark.skip(reason="Waiting for feature releases in pyqir.")
    def test_bitwise_ops(self, circuit_bitwise_ops: Circuit) -> None:
        with open("test_bitwise_ops.ll", "r") as input_file:
            data = input_file.read()
        call_and = (
            f"call void @__quantum__cis__and__body("
            "%Result* %zero, %Result* %zero1, %Result* %zero2"
            ")"
        )
        call_or = (
            f"call void @__quantum__cis__or__body("
            "%Result* %zero3, %Result* %zero4, %Result* %zero5"
            ")"
        )
        call_xor = (
            f"call void @__quantum__cis__xor__body("
            "%Result* %zero6, %Result* %zero7, %Result* %zero8"
            ")"
        )

        assert call_and in data
        assert call_or in data
        assert call_xor in data

    def test_generate_wasmop(self) -> None:
        wasm_file_path = qir_files_dir / "wasm_adder.wasm"
        wasm_handler = WasmFileHandler(str(wasm_file_path))

        with open(qir_files_dir / "WASM.ll", "r") as input_file:
            exp_data = input_file.read()

        circuit = Circuit()
        c0 = circuit.add_c_register("c0", 64)
        c1 = circuit.add_c_register("c1", 64)

        circuit.add_wasm_to_reg("add_one", wasm_handler, [c0], [c1])
        ir_bytes = circuit_to_pyqir_module(circuit, wasm_path=wasm_file_path)
        assert isinstance(ir_bytes, bytes)

        ll = bitcode_to_ir(ir_bytes)
        assert ll in exp_data


class TestPytketToQirConditional:
    """
    A class to test the translation of pytket conditional
    sub-circuits (CircBox) to QIR.
    """

    def test_simple_conditional(
        self, simple_conditional_circuit: Generator, simple_conditional_file_name: str
    ):
        with open(simple_conditional_file_name, "r") as input_file:
            data = input_file.readlines()

        test_file_path = qir_files_dir / simple_conditional_file_name

        with open(test_file_path, "r") as input_file:
            exp_data = input_file.readlines()

        for line in data:
            assert (
                line in exp_data
            )  # Identical up to some ordering of the function declarations.

    def test_nested_conditionals(
        self,
        pytket_nested_conditionals_circuit: Generator,
        pytket_nested_conditionals_file_name: str,
    ) -> None:
        with open(pytket_nested_conditionals_file_name, "r") as input_file:
            data = input_file.readlines()

        test_file_path = qir_files_dir / pytket_nested_conditionals_file_name

        with open(test_file_path, "r") as input_file:
            exp_data = input_file.readlines()

        for line in data:
            assert (
                line in exp_data
            )  # Identical up to some ordering of the function declarations.


class TestIrAndBcFileGeneration:
    """A class to test the generation of .ll and .bc files and their equivalence."""

    def test_generate_bell_circuit(self, bell_circuit) -> None:
        ll_file_name = "BellTestCircuit.ll"
        bc_file_name = "BellTestCircuit.bc"
        write_qir_file(bell_circuit, ll_file_name)
        write_qir_file(bell_circuit, bc_file_name)

        with open(ll_file_name, "r") as input_file:
            data = input_file.readlines()
        with open(bc_file_name, "rb") as input_file:
            bc_data = input_file.read()

        ll = bitcode_to_ir(bc_data)

        for line in data[1:]:  # Header info about module name is not contained.
            assert line in ll

        os.remove(ll_file_name)
        os.remove(bc_file_name)
