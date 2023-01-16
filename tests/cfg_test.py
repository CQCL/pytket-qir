from pathlib import Path

from pytket_qir.cfg import CfgAnalyser


qir_files_dir = Path("./qir_test_files")


class TestCfgAnalyser:
    def test_build_cfg_for_simple_conditional(self, simple_conditional_cfg) -> None:
        one_conditional_diamond_path = qir_files_dir / "one_conditional_diamond.bc"

        cfg = CfgAnalyser(one_conditional_diamond_path)

        assert cfg.cfg == simple_conditional_cfg

    def test_collapse_simple_instr_chain(self, collapsed_simple_chain_cfg) -> None:
        collapse_simple_chain_path = qir_files_dir / "collapse_simple_instr_chain.bc"

        cfg = CfgAnalyser(collapse_simple_chain_path)

        cfg.collapse_blocks()

        assert cfg.rewritten_cfg == collapsed_simple_chain_cfg

    def test_collapse_jump_left(self, collapsed_jump_left_cfg) -> None:
        collapse_jump_left = qir_files_dir / "collapse_jump_left.bc"

        cfg = CfgAnalyser(collapse_jump_left)

        cfg.collapse_blocks()

        assert cfg.rewritten_cfg == collapsed_jump_left_cfg

    def test_collapse_jump_right(self, collapsed_jump_right_cfg) -> None:
        collapse_jump_right = qir_files_dir / "collapse_jump_right.bc"

        cfg = CfgAnalyser(collapse_jump_right)

        cfg.collapse_blocks()

        assert cfg.rewritten_cfg == collapsed_jump_right_cfg

    def test_collapse_complex_instr_chains(self, collapsed_complex_chain) -> None:
        collapse_complex_chain = qir_files_dir / "collapse_jump_instr.bc"

        cfg = CfgAnalyser(collapse_complex_chain)

        cfg.collapse_blocks()

        assert cfg.rewritten_cfg == collapsed_complex_chain

    def test_collapse_nested_chains(self, collapsed_nested_chains) -> None:
        collapse_nested_chains_bc = qir_files_dir / "collapse_nested_jump_instr.bc"

        cfg = CfgAnalyser(collapse_nested_chains_bc)

        cfg.collapse_blocks()

        assert cfg.rewritten_cfg == collapsed_nested_chains

    def test_insert_block_right(self, insert_block_right) -> None:
        one_conditional_if = qir_files_dir / "one_conditional_if.bc"

        cfg = CfgAnalyser(one_conditional_if)

        cfg.collapse_blocks()

        cfg.insert_trivial_blocks()

        assert cfg.rewritten_cfg == insert_block_right

    def test_insert_block_left(self, insert_block_left) -> None:
        one_conditional_then = qir_files_dir / "one_conditional_then.bc"

        cfg = CfgAnalyser(one_conditional_then)

        cfg.collapse_blocks()

        cfg.insert_trivial_blocks()

        assert cfg.rewritten_cfg == insert_block_left

    def test_nested_blocks_right(self, insert_nested_blocks_right) -> None:
        teleport_chain = qir_files_dir / "teleportchain_baseprofile.bc"

        cfg = CfgAnalyser(teleport_chain)

        cfg.collapse_blocks()

        # Last operation must leave CFG identical.
        assert cfg.cfg == cfg.rewritten_cfg

        cfg.insert_trivial_blocks()

        assert cfg.rewritten_cfg == insert_nested_blocks_right
