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
    OpType.H: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.H, func_spec=FuncSpec.BODY
    ),
    OpType.X: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.X, func_spec=FuncSpec.BODY
    ),
    OpType.Y: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Y, func_spec=FuncSpec.BODY
    ),
    OpType.Z: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Z, func_spec=FuncSpec.BODY
    ),
    OpType.S: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.S, func_spec=FuncSpec.BODY
    ),
    OpType.Sdg: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.S, func_spec=FuncSpec.ADJ
    ),
    OpType.T: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.T, func_spec=FuncSpec.BODY
    ),
    OpType.Tdg: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.T, func_spec=FuncSpec.ADJ
    ),
    OpType.Reset: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.RESET, func_spec=FuncSpec.BODY
    ),
    OpType.CX: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.CX, func_spec=FuncSpec.BODY
    ),
    OpType.CZ: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.CZ, func_spec=FuncSpec.BODY
    ),
    OpType.Measure: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.MEASUREZ, func_spec=FuncSpec.BODY
    ),
    OpType.Rx: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Rx, func_spec=FuncSpec.BODY
    ),
    OpType.Ry: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Ry, func_spec=FuncSpec.BODY
    ),
    OpType.Rz: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.Rz, func_spec=FuncSpec.BODY
    ),
    OpType.CopyBits: QirGate(
        func_nat=FuncNat.QIS, func_name=FuncName.READ_RES, func_spec=FuncSpec.BODY
    ),
}


_PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}
# Resolve some naming ambiguities.
_PYQIR_TO_TK[
    QirGate(func_nat=FuncNat.QIS, func_name=FuncName.CNOT, func_spec=FuncSpec.BODY)
] = OpType.CX


PYQIR_GATES = CustomGateSet(
    name="PyQir",
    template=Template("__quantum__${func_nat}__${func_name}__${func_spec}"),
    base_gateset=set(_TK_TO_PYQIR.keys()),
    gateset={},
    tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
    gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
)
