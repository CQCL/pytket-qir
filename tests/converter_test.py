from pathlib import Path
import pytest

from pytket import Circuit  # type: ignore
from pytket.circuit import OpType  # type: ignore
from pytket.wasm import WasmFileHandler  # type: ignore

from pytket_qir.converter import topological_sort, circuit_from_qir, QirConverter


qir_files_dir = Path("./qir_test_files")


class TestConvertToCircuit:
    def test_topological_ordering(self) -> None:
        digraph = {
            "A": ["C", "D"],
            "B": ["E", "C"],
            "C": ["D"],
            "D": [],
            "E": ["A", "C"],
        }

        topological_ordering = topological_sort(digraph)

        assert topological_ordering == ["B", "E", "A", "C", "D"]

    def test_circuit_for_simple_conditional(
        self, simple_conditional_cfg, one_conditional_diamond_circuit
    ) -> None:

        one_conditional_diamond_path = qir_files_dir / "one_conditional_diamond.bc"
        circuit = circuit_from_qir(str(one_conditional_diamond_path))

        assert circuit.cfg == simple_conditional_cfg

        coms = circuit.get_commands()
        exp_coms = one_conditional_diamond_circuit.get_commands()

        com0 = coms[0]
        exp_com0 = exp_coms[0]
        assert com0 == exp_com0
        com1 = coms[1]
        exp_com1 = exp_coms[1]
        assert com1.op.get_exp() == exp_com1.op.get_exp()
        com2 = coms[2]
        exp_com2 = exp_coms[2]
        assert com2.op.op.get_circuit() == exp_com2.op.op.get_circuit()
        com3 = coms[3]
        exp_com3 = exp_coms[3]
        assert com3.op.get_exp() == exp_com3.op.get_exp()
        com4_circ = coms[4].op.op.get_circuit()
        exp_com4_circ = exp_coms[4].op.op.get_circuit()

        for com4, exp_com4 in zip(
            com4_circ.get_commands(), exp_com4_circ.get_commands()
        ):
            assert com4 == exp_com4
        com5 = coms[5]
        exp_com5 = exp_coms[5]
        assert com5.op.get_exp() == exp_com5.op.get_exp()

        com6_circ = coms[6].op.op.get_circuit()
        exp_com6_circ = exp_coms[6].op.op.get_circuit()

        for com6, exp_com6 in zip(
            com6_circ.get_commands(), exp_com6_circ.get_commands()
        ):
            assert com6 == exp_com6
        com7 = coms[7]
        exp_com7 = exp_coms[7]
        assert com7.op.get_exp() == exp_com7.op.get_exp()

        com8_circ = coms[8].op.op.get_circuit()
        exp_com8_circ = exp_coms[8].op.op.get_circuit()

        for com8, exp_com8 in zip(
            com8_circ.get_commands(), exp_com8_circ.get_commands()
        ):
            assert com8 == exp_com8

    def test_fallthrough_right(self, one_conditional_else_circuit) -> None:
        one_conditional_if = qir_files_dir / "one_conditional_else.bc"

        circuit = circuit_from_qir(one_conditional_if)

        coms = circuit.get_commands()
        exp_coms = one_conditional_else_circuit.get_commands()

        com0 = coms[0]
        exp_com0 = exp_coms[0]
        assert com0 == exp_com0

        com1 = coms[1]
        exp_com1 = exp_coms[1]
        assert com1.op.get_exp() == exp_com1.op.get_exp()

        com2_circ = coms[2].op.op.get_circuit()
        exp_com2_circ = exp_coms[2].op.op.get_circuit()

        for com2, exp_com2 in zip(        
            com2_circ.get_commands(), exp_com2_circ.get_commands()
        ):
            assert com2 == exp_com2

        com3 = coms[3]
        exp_com3 = exp_coms[3]
        assert com3.op.get_exp() == exp_com3.op.get_exp()

        com4_circ = coms[4].op.op.get_circuit()
        exp_com4_circ = exp_coms[4].op.op.get_circuit()

        for com4, exp_com4 in zip(
            com4_circ.get_commands(), exp_com4_circ.get_commands()
        ):
            assert com4 == exp_com4
        com5 = coms[5]
        exp_com5 = exp_coms[5]
        assert com5.op.get_exp() == exp_com5.op.get_exp()

        com6_circ = coms[6].op.op.get_circuit()
        exp_com6_circ = exp_coms[6].op.op.get_circuit()

        for com6, exp_com6 in zip(
            com6_circ.get_commands(), exp_com6_circ.get_commands()
        ):
            assert com6 == exp_com6

    def test_fallthrough_left(self, one_conditional_then_circuit) -> None:
        one_conditional_else = qir_files_dir / "one_conditional_then.bc"

        circuit = circuit_from_qir(one_conditional_else)

        coms = circuit.get_commands()
        exp_coms = one_conditional_then_circuit.get_commands()

        com0 = coms[0]
        exp_com0 = exp_coms[0]
        assert com0 == exp_com0

        com1 = coms[1]
        exp_com1 = exp_coms[1]
        assert com1.op.get_exp() == exp_com1.op.get_exp()

        com2_circ = coms[2].op.op.get_circuit()
        exp_com2_circ = exp_coms[2].op.op.get_circuit()

        for com2, exp_com2 in zip(        
            com2_circ.get_commands(), exp_com2_circ.get_commands()
        ):
            assert com2 == exp_com2

        com3 = coms[3]
        exp_com3 = exp_coms[3]
        assert com3.op.get_exp() == exp_com3.op.get_exp()

        com4_circ = coms[4].op.op.get_circuit()
        exp_com4_circ = exp_coms[4].op.op.get_circuit()

        for com4, exp_com4 in zip(
            com4_circ.get_commands(), exp_com4_circ.get_commands()
        ):
            assert com4 == exp_com4
        com5 = coms[5]
        exp_com5 = exp_coms[5]
        assert com5.op.get_exp() == exp_com5.op.get_exp()

        com6_circ = coms[6].op.op.get_circuit()
        exp_com6_circ = exp_coms[6].op.op.get_circuit()

        for com6, exp_com6 in zip(
            com6_circ.get_commands(), exp_com6_circ.get_commands()
        ):
            assert com6 == exp_com6

class TestCfgOptimisations:

    def test_collapse_simple_instr_chain(self, collapsed_simple_chain_cfg) -> None:
        collapse_simple_chain_path = qir_files_dir / "collapse_simple_instr_chain.bc"

        converter = QirConverter(str(collapse_simple_chain_path))
        converter.collapse_blocks()

        assert converter.rewritten_cfg == collapsed_simple_chain_cfg

    def test_collapse_jump_left(self, collapsed_jump_left_cfg) -> None:
        collapse_jump_left = qir_files_dir / "collapse_jump_left.bc"

        converter = QirConverter(str(collapse_jump_left))
        converter.collapse_blocks()

        assert converter.rewritten_cfg == collapsed_jump_left_cfg

    def test_collapse_jump_right(self, collapsed_jump_right_cfg) -> None:
        collapse_jump_right = qir_files_dir / "collapse_jump_right.bc"

        converter = QirConverter(str(collapse_jump_right))
        converter.collapse_blocks()

        assert converter.rewritten_cfg == collapsed_jump_right_cfg

    def test_collapse_complex_instr_chains(self, collapsed_complex_chain) -> None:
        collapse_complex_chain = qir_files_dir / "collapse_jump_instr.bc"

        converter = QirConverter(str(collapse_complex_chain))
        converter.collapse_blocks()

        assert converter.rewritten_cfg == collapsed_complex_chain

    def test_collapse_nested_chains(self, collapsed_nested_chains) -> None:
        collapse_nested_chains_bc = qir_files_dir / "collapse_nested_jump_instr.bc"

        converter = QirConverter(str(collapse_nested_chains_bc))
        converter.collapse_blocks()

        assert converter.rewritten_cfg == collapsed_nested_chains


class TestQirToPytketConditionals:
    """A class to test circuit translation containing conditionals."""

    @pytest.mark.skip
    def test_single_conditional_diamond_opposite(self) -> None:
        one_conditional_diamond_bc_path = (
            qir_files_dir / "one_conditional_diamond_opposite.bc"
        )

        circuit = circuit_from_qir(one_conditional_diamond_bc_path)

    @pytest.mark.skip
    def test_collapse_jump_instr(self, collapse_jump_instr: Circuit) -> None:
        collapse_jump_instr_file = qir_files_dir / "collapse_jump_instr.bc"

        circuit = circuit_from_qir(collapse_jump_instr_file)

        circuit_coms = circuit.get_commands()
        exp_circuit_coms = collapse_jump_instr.get_commands()

        for com1, com2 in zip(circuit_coms[:5], exp_circuit_coms[:5]):
            assert com1 == com2

        else_circuit_coms = circuit_coms[5].op.op.get_circuit().get_commands()
        exp_else_circuit_coms = exp_circuit_coms[5].op.op.get_circuit().get_commands()

        for com1, com2 in zip(else_circuit_coms, exp_else_circuit_coms):
            assert com1 == com2

        import pdb

        pdb.set_trace()
        then_circuit_coms = circuit_coms[6].op.op.get_circuit().get_commands()
        exp_then_circuit_coms = exp_circuit_coms[6].op.op.get_circuit().get_commands()

        for com1, com2 in zip(then_circuit_coms, exp_then_circuit_coms):
            assert com1 == com2

        for com1, com2 in zip(circuit_coms[7:11], exp_circuit_coms[7:11]):
            assert com1 == com2

        leftbr1_coms = circuit_coms[11].op.op.get_circuit().get_commands()
        exp_leftbr1_coms = exp_circuit_coms[11].op.op.get_circuit().get_commands()

        for com1, com2 in zip(leftbr1_coms, exp_leftbr1_coms):
            assert com1 == com2

        rightbr1_coms = circuit_coms[12].op.op.get_circuit().get_commands()
        exp_rightbr1_coms = exp_circuit_coms[12].op.op.get_circuit().get_commands()

        for com1, com2 in zip(rightbr1_coms, exp_rightbr1_coms):
            assert com1 == com2

        for com1, com2 in zip(circuit_coms[13:], exp_circuit_coms[13:]):
            assert com1 == com2

    @pytest.mark.skip
    def test_nested_conditionals_then(self, nested_conditionals_then: Circuit) -> None:
        nested_conditionals_then_circuit = qir_files_dir / "nested_conditionals_then.bc"

        circuit = circuit_from_qir(nested_conditionals_then_circuit)

        circuit_coms = circuit.get_commands()
        exp_circuit_coms = nested_conditionals_then.get_commands()

        for com1, com2 in zip(circuit_coms[:5], exp_circuit_coms[:5]):
            assert com1 == com2

        then_circuit_coms = circuit_coms[5].op.op.get_circuit().get_commands()
        exp_then_circuit_coms = exp_circuit_coms[5].op.op.get_circuit().get_commands()

        for com1, com2 in zip(then_circuit_coms[:4], exp_then_circuit_coms[:4]):
            assert com1 == com2

        then_circuit_coms_1 = then_circuit_coms[5].op.op.get_circuit()
        exp_then_circuit_coms_1 = exp_then_circuit_coms[5].op.op.get_circuit()

        assert then_circuit_coms_1 == exp_then_circuit_coms_1

        else_circuit_coms_1 = then_circuit_coms[6].op.op.get_circuit()
        exp_else_circuit_coms_1 = exp_then_circuit_coms[6].op.op.get_circuit()

        assert else_circuit_coms_1 == exp_else_circuit_coms_1

        else_circuit_coms = circuit_coms[6].op.op.get_circuit().get_commands()
        exp_else_circuit_coms = exp_circuit_coms[6].op.op.get_circuit().get_commands()

        for com1, com2 in zip(else_circuit_coms, exp_else_circuit_coms):
            assert com1 == com2

        for com1, com2 in zip(circuit_coms[7:], exp_circuit_coms[7:]):
            assert com1 == com2

    @pytest.mark.skip
    def test_nested_conditionals_else(self) -> None:
        nested_conditionals_else = qir_files_dir / "nested_conditionals_else.bc"

        circuit = circuit_from_qir(nested_conditionals_else)

        import pdb

        pdb.set_trace()

    @pytest.mark.skip
    def test_nested_conditionals_crossed(self) -> None:
        nested_conditionals_crossed = qir_files_dir / "nested_conditionals_crossed.bc"

        circuit = circuit_from_qir(nested_conditionals_crossed)

        import pdb

        pdb.set_trace()

    @pytest.mark.skip
    def test_multiple_successive_conditionals(
        self,
    ) -> None:
        multiple_conditionals_bc_file_path = (
            qir_files_dir / "teleportchain_baseprofile.bc"
        )

        circuit = circuit_from_qir(multiple_conditionals_bc_file_path)

        inv_reg_map = {v: k for k, v in circuit.ssa_vars.items()}

        coms = circuit.get_commands()
        com0 = coms[0]
        assert com0.op.type == OpType.H
        assert com0.qubits[0].index[0] == 0
        com1 = coms[1]
        assert com1.op.type == OpType.H
        assert com1.qubits[0].index[0] == 2
        com2 = coms[2]
        assert com2.op.type == OpType.H
        assert com2.qubits[0].index[0] == 3
        com3 = coms[3]
        assert com3.op.type == OpType.CX
        assert com3.qubits[0].index[0] == 0
        assert com3.qubits[1].index[0] == 1
        com4 = coms[4]
        assert com4.op.type == OpType.CX
        assert com4.qubits[0].index[0] == 2
        assert com4.qubits[1].index[0] == 4
        com5 = coms[5]
        assert com5.op.type == OpType.CX
        assert com5.qubits[0].index[0] == 3
        assert com5.qubits[1].index[0] == 5
        com6 = coms[6]
        assert com6.op.type == OpType.CX
        assert com6.qubits[0].index[0] == 1
        assert com6.qubits[1].index[0] == 2
        com7 = coms[7]
        assert com7.op.type == OpType.H
        assert com7.qubits[0].index[0] == 1
        com8 = coms[8]
        assert com8.op.type == OpType.Measure
        assert com8.qubits[0].index[0] == 1
        assert com8.bits[0].index[0] == 0
        assert com8.bits[0].reg_name == "c"
        com9 = coms[9]
        assert com9.op.type == OpType.CopyBits
        assert com9.args[0].reg_name == "c"
        assert com9.args[0].index[0] == 0
        assert com9.args[1].reg_name == "c"
        assert com9.args[1].index[0] == 6
        com10 = coms[10]
        assert com10.op.type == OpType.Reset
        assert com10.qubits[0].index[0] == 1
        com11 = coms[11]
        assert com11.args[0].reg_name == "c"
        assert com11.args[0].index[0] == 6  # Equivalent to bit %0[0].
        assert inv_reg_map[com11.args[0]] == "%0"
        condition_circuit_coms = com11.op.op.get_circuit().get_commands()
        ccc0 = condition_circuit_coms[0]
        assert ccc0.op.type == OpType.Z
        assert ccc0.qubits[0].index[0] == 4
        com12 = coms[12]
        assert (
            len(com12.op.op.get_circuit().get_commands()) == 0
        )  # Empty circuit to hold false condition.
        com13 = coms[13]
        assert com13.op.type == OpType.Measure
        assert com13.qubits[0].index[0] == 2
        assert com13.bits[0].index[0] == 1
        com14 = coms[14]
        assert com14.op.type == OpType.CopyBits
        assert com14.args[0].reg_name == "c"
        assert com14.args[0].index[0] == 1
        assert com14.args[1].reg_name == "c"
        assert com14.args[1].index[0] == 7
        com15 = coms[15]
        import pdb

        pdb.set_trace()
        assert com15.op.type == OpType.Reset
        assert com15.qubits[0].index[0] == 2
        com16 = coms[16]
        assert com16.args[0].reg_name == "c"
        assert com16.args[0].index[0] == 7  # Equivalent to bit %1[0].
        assert inv_reg_map[com16.args[0]] == "%1"
        condition_circuit_coms = com16.op.op.get_circuit().get_commands()
        ccc0 = condition_circuit_coms[0]
        assert ccc0.op.type == OpType.X
        assert ccc0.qubits[0].index[0] == 4
        com17 = coms[17]
        assert (
            len(com17.op.op.get_circuit().get_commands()) == 0
        )  # Empty circuit to hold false condition.
        com18 = coms[18]
        assert com18.op.type == OpType.CX
        assert com18.qubits[0].index[0] == 4
        assert com18.qubits[1].index[0] == 3
        com19 = coms[19]
        assert com19.op.type == OpType.H
        assert com19.qubits[0].index[0] == 4
        com20 = coms[20]
        assert com20.op.type == OpType.Measure
        assert com20.qubits[0].index[0] == 4
        assert com20.bits[0].index[0] == 2
        com21 = coms[21]
        assert com21.op.type == OpType.CopyBits
        assert com21.args[0].reg_name == "c"
        assert com21.args[0].index[0] == 2
        assert com21.args[1].reg_name == "c"
        assert com21.args[1].index[0] == 8
        com22 = coms[22]
        assert com22.op.type == OpType.Reset
        assert com22.qubits[0].index[0] == 4
        com23 = coms[23]
        assert com23.args[0].reg_name == "c"
        assert com23.args[0].index[0] == 8  # Equivalent to bit %2[0].
        assert inv_reg_map[com23.args[0]] == "%2"
        condition_circuit_coms = com23.op.op.get_circuit().get_commands()[0]
        assert condition_circuit_coms.op.type == OpType.Z
        assert condition_circuit_coms.qubits[0].index[0] == 5
        com24 = coms[24]
        assert (
            len(com24.op.op.get_circuit().get_commands()) == 0
        )  # Empty circuit to hold false condition.
        com25 = coms[25]
        assert com25.op.type == OpType.Measure
        assert com25.qubits[0].index[0] == 3
        assert com25.bits[0].index[0] == 3
        com26 = coms[26]
        assert com26.op.type == OpType.CopyBits
        assert com26.args[0].reg_name == "c"
        assert com26.args[0].index[0] == 3
        assert com26.args[1].reg_name == "c"
        assert com26.args[1].index[0] == 9
        com27 = coms[27]
        assert com27.op.type == OpType.Reset
        assert com27.qubits[0].index[0] == 3
        com28 = coms[28]
        assert com28.args[0].reg_name == "c"
        assert com28.args[0].index[0] == 9  # Equivalent to bit %3[0].
        assert inv_reg_map[com28.args[0]] == "%3"
        condition_circuit_coms = com28.op.op.get_circuit().get_commands()[0]
        assert condition_circuit_coms.op.type == OpType.X
        assert condition_circuit_coms.qubits[0].index[0] == 5
        com29 = coms[29]
        assert (
            len(com29.op.op.get_circuit().get_commands()) == 0
        )  # Empty circuit to hold false condition.
        com30 = coms[30]
        assert com30.op.type == OpType.Measure
        assert com30.qubits[0].index[0] == 0
        assert com30.bits[0].index[0] == 4
        com31 = coms[31]
        assert com31.op.type == OpType.Measure
        assert com31.qubits[0].index[0] == 5
        assert com31.bits[0].index[0] == 5
        com32 = coms[32]
        assert com32.op.type == OpType.Reset
        assert com32.qubits[0].index[0] == 0
        com33 = coms[33]
        assert com33.op.type == OpType.Reset
        assert com33.qubits[0].index[0] == 5

    @pytest.mark.skip
    def test_nested_conditionals_mixed(
        self,
        nested_conditionals_circuit: Circuit,
    ) -> None:
        nested_conditionals_bc_file_path = qir_files_dir / "nested_conditionals.bc"
        circuit = circuit_from_qir(nested_conditionals_bc_file_path)

        import pdb

        pdb.set_trace()

        inv_reg_map = {v: k for k, v in circuit.ssa_vars.items()}

        for com1, com2 in zip(
            circuit.get_commands()[:16], nested_conditionals_circuit.get_commands()[:16]
        ):
            assert com1 == com2
        for com1, com2 in zip(
            circuit.get_commands()[17:32],
            nested_conditionals_circuit.get_commands()[17:32],
        ):
            assert com1 == com2
        for com1, com2 in zip(
            circuit.get_commands()[33:], nested_conditionals_circuit.get_commands()[33:]
        ):
            assert com1 == com2

        condition_com = circuit.get_commands()[16]
        assert condition_com.args[0].reg_name == "c"
        assert condition_com.args[0].index[0] == 13  # Equivalent to bit %0[0].
        assert inv_reg_map[condition_com.args[0]] == "%0"

        condition_circuit = condition_com.op.op.get_circuit()
        exp_condition_circuit = nested_conditionals_circuit.get_commands()[
            16
        ].op.op.get_circuit()

        for com1, com2 in zip(
            condition_circuit.get_commands()[:16],
            exp_condition_circuit.get_commands()[:16],
        ):
            assert com1 == com2

        for com1, com2 in zip(
            condition_circuit.get_commands()[17:],
            exp_condition_circuit.get_commands()[17:],
        ):
            assert com1 == com2

        nested_condition_com = condition_circuit.get_commands()[16]
        assert nested_condition_com.args[0].reg_name == "c"
        assert nested_condition_com.args[0].index[0] == 14  # Equivalent to bit %1[0].

        nested_condition_circuit = nested_condition_com.op.op.get_circuit()
        exp_nested_condition_circuit = exp_condition_circuit.get_commands()[
            16
        ].op.op.get_circuit()

        for com1, com2 in zip(
            nested_condition_circuit.get_commands(),
            exp_nested_condition_circuit.get_commands(),
        ):
            assert com1 == com2

        condition_com = circuit.get_commands()[32]
        assert condition_com.args[0].reg_name == "c"
        assert condition_com.args[0].index[0] == 14  # Equivalent to bit %2[0].
        assert inv_reg_map[condition_com.args[0]] == "%2"

        condition_circuit = condition_com.op.op.get_circuit()
        exp_condition_circuit = nested_conditionals_circuit.get_commands()[
            32
        ].op.op.get_circuit()

        for com1, com2 in zip(
            condition_circuit.get_commands(),
            exp_condition_circuit.get_commands(),
        ):
            assert com1 == com2

    @pytest.mark.skip(reason="Temporary disable non-simple circuits work around.")
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

    @pytest.mark.skip(reason="Temporary disable non-simple circuits work around.")
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

    @pytest.mark.skip(reason="Temporary disable non-simple circuits work around.")
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
