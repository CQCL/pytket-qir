from string import Template

from pytket import OpType  # type: ignore

from pytket_qir.gatesets.base import (
    CustomGateSet,
    FuncNat,
    FuncName,
    FuncSpec,
    QirGate,
)


_TK_TO_PYQIR = {
    OpType.H: QirGate(opnat=FuncNat.QIS, opname=FuncName.H, opspec=FuncSpec.BODY),
    OpType.X: QirGate(opnat=FuncNat.QIS, opname=FuncName.X, opspec=FuncSpec.BODY),
    OpType.Y: QirGate(opnat=FuncNat.QIS, opname=FuncName.Y, opspec=FuncSpec.BODY),
    OpType.Z: QirGate(opnat=FuncNat.QIS, opname=FuncName.Z, opspec=FuncSpec.BODY),
    OpType.S: QirGate(opnat=FuncNat.QIS, opname=FuncName.S, opspec=FuncSpec.BODY),
    OpType.Sdg: QirGate(opnat=FuncNat.QIS, opname=FuncName.S, opspec=FuncSpec.ADJ),
    OpType.T: QirGate(opnat=FuncNat.QIS, opname=FuncName.T, opspec=FuncSpec.BODY),
    OpType.Tdg: QirGate(opnat=FuncNat.QIS, opname=FuncName.T, opspec=FuncSpec.ADJ),
    OpType.Reset: QirGate(opnat=FuncNat.QIS, opname=FuncName.RESET, opspec=FuncSpec.BODY),
    OpType.CX: QirGate(opnat=FuncNat.QIS, opname=FuncName.CX, opspec=FuncSpec.BODY),
    OpType.CZ: QirGate(opnat=FuncNat.QIS, opname=FuncName.CZ, opspec=FuncSpec.BODY),
    OpType.Measure: QirGate(
        opnat=FuncNat.QIS, opname=FuncName.MEASUREZ, opspec=FuncSpec.BODY
    ),
    OpType.Rx: QirGate(opnat=FuncNat.QIS, opname=FuncName.Rx, opspec=FuncSpec.BODY),
    OpType.Ry: QirGate(opnat=FuncNat.QIS, opname=FuncName.Ry, opspec=FuncSpec.BODY),
    OpType.Rz: QirGate(opnat=FuncNat.QIS, opname=FuncName.Rz, opspec=FuncSpec.BODY),
    OpType.CopyBits: QirGate(
        opnat=FuncNat.QIS, opname=FuncName.READ_RES, opspec=FuncSpec.BODY
    ),
}


_PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}
# Resolve some naming ambiguities.
_PYQIR_TO_TK[
    QirGate(opnat=FuncNat.QIS, opname=FuncName.CNOT, opspec=FuncSpec.BODY)
] = OpType.CX


PYQIR_GATES = CustomGateSet(
    name="PyQir",
    template=Template("__quantum__${opnat}__${opname}__${opspec}"),
    base_gateset=set(_TK_TO_PYQIR.keys()),
    gateset={},
    tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
    gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
)
