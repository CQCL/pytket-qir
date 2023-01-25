from collections import OrderedDict
from pathlib import Path

from pytket import Circuit  # type: ignore

from pytket_qir.converter import topological_sort, circuit_from_qir


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

        assert topological_ordering == {
            "B": ["E", "C"],
            "E": ["A", "C"],
            "A": ["C", "D"],
            "C": ["D"],
            "D": [],
        }

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

    def test_single_conditional_diamond_opposite(
        self, simple_conditional_opposite_cfg, one_conditional_diamond_opposite_circuit
    ) -> None:
        one_conditional_diamond_bc_path = (
            qir_files_dir / "one_conditional_diamond_opposite.bc"
        )

        circuit = circuit_from_qir(one_conditional_diamond_bc_path)
        assert circuit.cfg == simple_conditional_opposite_cfg

        coms = circuit.get_commands()
        exp_coms = one_conditional_diamond_opposite_circuit.get_commands()

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

    def test_nested_conditionals_then(
        self, nested_conditionals_then_cfg: OrderedDict
    ) -> None:
        nested_conditionals_then_circuit = qir_files_dir / "nested_conditionals_then.bc"

        circuit = circuit_from_qir(nested_conditionals_then_circuit)

        assert circuit.cfg == nested_conditionals_then_cfg

    def test_nested_conditionals_else(
        self, nested_conditionals_else_cfg: OrderedDict
    ) -> None:
        nested_conditionals_else = qir_files_dir / "nested_conditionals_else.bc"

        circuit = circuit_from_qir(nested_conditionals_else)

        assert circuit.cfg == nested_conditionals_else_cfg

    def test_nested_conditionals_crossed(
        self, nested_conditionals_crossed_cfg: OrderedDict
    ) -> None:
        nested_conditionals_crossed = qir_files_dir / "nested_conditionals_crossed.bc"

        circuit = circuit_from_qir(nested_conditionals_crossed)

        assert circuit.cfg == nested_conditionals_crossed_cfg

    def test_multiple_successive_conditionals(
        self, multiple_successive_conditionals_cfg: OrderedDict
    ) -> None:
        multiple_conditionals_bc_file_path = (
            qir_files_dir / "teleportchain_baseprofile.bc"
        )

        circuit = circuit_from_qir(multiple_conditionals_bc_file_path)

        assert circuit.cfg == multiple_successive_conditionals_cfg

    def test_nested_conditionals_mixed(
        self,
        nested_conditionals_mixed_cfg: Circuit,
    ) -> None:
        nested_conditionals_bc_file_path = qir_files_dir / "nested_conditionals.bc"

        circuit = circuit_from_qir(nested_conditionals_bc_file_path)

        assert circuit.cfg == nested_conditionals_mixed_cfg


class TestCfgOptimisations:
    def test_collapse_simple_instr_chain(
        self, collapsed_simple_chain_cfg, collapse_simple_chain_circuit
    ) -> None:
        collapse_simple_chain_path = qir_files_dir / "collapse_simple_instr_chain.bc"

        circuit = circuit_from_qir(collapse_simple_chain_path, optimisation_level=1)
        assert circuit.cfg == collapsed_simple_chain_cfg

        coms = circuit.get_commands()
        exp_coms = collapse_simple_chain_circuit.get_commands()

        assert coms[0] == exp_coms[0]
        assert str(coms[1].op.get_exp()) == str(exp_coms[1].op.get_exp())

        circ = coms[2].op.op.get_circuit()
        exp_circ = exp_coms[2].op.op.get_circuit()

        assert circ == exp_circ

    def test_collapse_jump_left(
        self, collapsed_jump_left_cfg, collapse_jump_left_circuit
    ) -> None:
        collapse_jump_left = qir_files_dir / "collapse_jump_left.bc"

        circuit = circuit_from_qir(collapse_jump_left, optimisation_level=1)

        assert circuit.cfg == collapsed_jump_left_cfg

        coms = circuit.get_commands()
        exp_coms = collapse_jump_left_circuit.get_commands()

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

    def test_collapse_jump_right(
        self, collapsed_jump_right_cfg, collapse_jump_right_circuit
    ) -> None:
        collapse_jump_right = qir_files_dir / "collapse_jump_right.bc"

        circuit = circuit_from_qir(collapse_jump_right, optimisation_level=1)

        assert circuit.cfg == collapsed_jump_right_cfg

        coms = circuit.get_commands()
        exp_coms = collapse_jump_right_circuit.get_commands()

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

    def test_collapse_complex_instr_chains(
        self, collapsed_complex_chain, collapse_complex_chain_circuit
    ) -> None:
        collapse_complex_chain = qir_files_dir / "collapse_jump_instr.bc"

        circuit = circuit_from_qir(collapse_complex_chain, optimisation_level=1)

        assert circuit.cfg == collapsed_complex_chain

        coms = circuit.get_commands()
        exp_coms = collapse_complex_chain_circuit.get_commands()

        assert coms[0] == exp_coms[0]
        assert str(coms[1].op.get_exp()) == str(exp_coms[1].op.get_exp())
        assert coms[2].op.op.get_circuit() == exp_coms[2].op.op.get_circuit()

        assert str(coms[3].op.get_exp()) == str(exp_coms[3].op.get_exp())
        com4 = coms[4].op.op.get_circuit().get_commands()
        exp_com4 = exp_coms[4].op.op.get_circuit().get_commands()

        for com1, com2 in zip(com4, exp_com4):
            assert com1 == com2
        assert str(coms[5].op.get_exp()) == str(exp_coms[5].op.get_exp())

        com6 = coms[6].op.op.get_circuit().get_commands()
        exp_com6 = exp_coms[6].op.op.get_circuit().get_commands()

        for com1, com2 in zip(com6, exp_com6):
            assert com1 == com2

        assert str(coms[7].op.get_exp()) == str(exp_coms[7].op.get_exp())

        com8 = coms[8].op.op.get_circuit().get_commands()
        exp_com8 = exp_coms[8].op.op.get_circuit().get_commands()

        for com1, com2 in zip(com8, exp_com8):
            assert com1 == com2

    def test_collapse_nested_chains(self, collapsed_nested_chains) -> None:
        collapse_nested_chains_bc = qir_files_dir / "collapse_nested_jump_instr.bc"

        circuit = circuit_from_qir(collapse_nested_chains_bc, optimisation_level=1)

        assert circuit.cfg == collapsed_nested_chains