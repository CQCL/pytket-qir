from string import Template

from pytket import OpType  # type: ignore

from pyqir.generator import types  # type: ignore

from pytket_qir.gatesets.base import (
    CustomQirGate,
    CustomGateSet,
    OpNat,
    OpName,
    OpSpec,
    QirGate,
)


_TK_TO_PYQIR = {
    OpType.H: QirGate(opnat=OpNat.QIS, opname=OpName.H, opspec=OpSpec.BODY),
    OpType.X: QirGate(opnat=OpNat.QIS, opname=OpName.X, opspec=OpSpec.BODY),
    OpType.Y: QirGate(opnat=OpNat.QIS, opname=OpName.Y, opspec=OpSpec.BODY),
    OpType.Z: QirGate(opnat=OpNat.QIS, opname=OpName.Z, opspec=OpSpec.BODY),
    OpType.S: QirGate(opnat=OpNat.QIS, opname=OpName.S, opspec=OpSpec.BODY),
    OpType.Sdg: QirGate(opnat=OpNat.QIS, opname=OpName.S, opspec=OpSpec.ADJ),
    OpType.T: QirGate(opnat=OpNat.QIS, opname=OpName.T, opspec=OpSpec.BODY),
    OpType.Tdg: QirGate(opnat=OpNat.QIS, opname=OpName.T, opspec=OpSpec.ADJ),
    OpType.Reset: QirGate(opnat=OpNat.QIS, opname=OpName.RESET, opspec=OpSpec.BODY),
    OpType.CX: QirGate(opnat=OpNat.QIS, opname=OpName.CX, opspec=OpSpec.BODY),
    OpType.CZ: QirGate(opnat=OpNat.QIS, opname=OpName.CZ, opspec=OpSpec.BODY),
    OpType.Measure: QirGate(opnat=OpNat.QIS, opname=OpName.MEASUREZ, opspec=OpSpec.BODY),
    OpType.Rx: QirGate(opnat=OpNat.QIS, opname=OpName.Rx, opspec=OpSpec.BODY),
    OpType.Ry: QirGate(opnat=OpNat.QIS, opname=OpName.Ry, opspec=OpSpec.BODY),
    OpType.Rz: QirGate(opnat=OpNat.QIS, opname=OpName.Rz, opspec=OpSpec.BODY),
    OpType.WASM: QirGate(opnat=OpNat.HYBRID, opname=OpName.WASM, opspec=OpSpec.BODY),
}


_PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}
# Resolve some naming ambiguities.
_PYQIR_TO_TK[
    QirGate(opnat=OpNat.QIS, opname=OpName.CNOT, opspec=OpSpec.BODY)
] = OpType.CX


PYQIR_GATES = CustomGateSet(
    name="PyQir",
    template=Template("__quantum__${opnat}__${opname}__${opspec}"),
    gateset={
        "wasm": CustomQirGate(
            opnat=OpNat.HYBRID,
            opname=OpName.WASM,
            opspec=OpSpec.BODY,
            function_signature=[types.INT],
            return_type=types.INT,
        ),
    },
    tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
    gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
)
