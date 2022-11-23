from pathlib import Path
from string import Template
from typing import cast

from pyqir.generator import bitcode_to_ir, types  # types: ignore

from pytket_qir.gatesets.base import (
    CustomGateSet,
    CustomQirGate,
    OpName,
    OpNat,
    OpSpec,
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
            opnat=OpNat.QIS,
            opname=OpName.READ_RES,
            opspec=OpSpec.BODY,
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
