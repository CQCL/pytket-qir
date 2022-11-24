from pathlib import Path
from string import Template
from typing import cast

from pyqir.generator import bitcode_to_ir, types  # type: ignore
from pytket import OpType  # type: ignore
from pytket.passes import FullPeepholeOptimise  # type: ignore

from pytket_qir.gatesets.base import (
    CustomGateSet,
    CustomQirGate,
    FuncName,
    FuncNat,
    FuncSpec,
    QirGate,
)
from pytket_qir.gatesets.pyqir import _TK_TO_PYQIR
from pytket_qir.generator import circuit_to_qir
from pytket_qir.parser import circuit_from_qir


qir_files_dir = Path("./qir_test_files")


class TestRoundTripValidation:
    """Test round trips from QIR to QIR by validating inputs and outputs."""

    def test_teleportchain_baseprofile(self) -> None:
        bc_teleport_chain_file_path = qir_files_dir / "teleportchain_baseprofile.bc"
        ll_teleport_chain_file_path = qir_files_dir / "teleportchain_baseprofile.ll"

        with open(ll_teleport_chain_file_path, "r") as f:
            exp_data = f.read()

        qis_read_result = CustomQirGate(
            opnat=FuncNat.QIS,
            opname=FuncName.READ_RES,
            opspec=FuncSpec.BODY,
            function_signature=[types.RESULT],
            return_type=types.BOOL,
        )

        _PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}

        ext_pyqir_gates = CustomGateSet(
            name="ExtPyQir",
            template=Template("__quantum__${opnat}__${opname}__${opspec}"),
            base_gateset=set(_TK_TO_PYQIR.keys()),
            gateset={"read_result": qis_read_result},
            tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
            gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
        )
        circuit = circuit_from_qir(bc_teleport_chain_file_path)

        ir_bytes = cast(bytes, circuit_to_qir(circuit, gateset=ext_pyqir_gates))

        ll = bitcode_to_ir(ir_bytes)

        # At least check that function calls exist in the expected file
        # up to some ordering.
        for line in ll.splitlines():
            if line.startswith("call"):
                assert line in exp_data

    def test_grover_baseprofile(self) -> None:
        bc_grover_file_path = qir_files_dir / "SimpleGroverSample.BaseProfile.bc"
        ll_grover_file_path = qir_files_dir / "SimpleGroverSample.BaseProfile.ll"
        ll_grover_opt_file_path = qir_files_dir / "SimpleGroverSampleOptimised.ll"

        with open(ll_grover_file_path, "r") as input_file:
            exp_data = input_file.read()

        with open(ll_grover_opt_file_path, "r") as input_file:
            opt_exp_data = input_file.read()

        circuit = circuit_from_qir(bc_grover_file_path)

        # Extend PyQir base gateset to account for Barrier.
        qir_gate = QirGate(
            opnat=FuncNat.RT,
            opname=FuncName.RES,
            opspec=FuncSpec.REC_OUT,
        )

        _TK_TO_PYQIR[OpType.Barrier] = qir_gate

        qis_res_rec = CustomQirGate(
            opnat=FuncNat.RT,
            opname=FuncName.RES,
            opspec=FuncSpec.REC_OUT,
            function_signature=[types.RESULT],
            return_type=types.VOID,
        )

        _PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}

        ext_pyqir_gates = CustomGateSet(
            name="ExtPyQir",
            template=Template("__quantum__${opnat}__${opname}__${opspec}"),
            base_gateset=set(_TK_TO_PYQIR.keys()),
            gateset={"read_result": qis_res_rec},
            tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
            gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
        )

        ir_bytes = cast(bytes, circuit_to_qir(circuit, gateset=ext_pyqir_gates))

        ll = bitcode_to_ir(ir_bytes)

        # Round trip identical up to some reordering.
        for line in ll.splitlines():
            if line.startswith("call"):
                assert line in exp_data

        # Optimise circuit
        FullPeepholeOptimise().apply(circuit)

        ir_bytes = cast(bytes, circuit_to_qir(circuit, gateset=ext_pyqir_gates))

        ll = bitcode_to_ir(ir_bytes)

        assert ll == opt_exp_data
