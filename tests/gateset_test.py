# Copyright 2020-2023 Cambridge Quantum Computing
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

from pytket.qir.conversion.gatesets import _TK_TO_PYQIR

from pytket.circuit import OpType  # type: ignore


def test_gateset() -> None:
    assert OpType.H in _TK_TO_PYQIR
    assert OpType.X in _TK_TO_PYQIR
    assert OpType.Y in _TK_TO_PYQIR
    assert OpType.Z in _TK_TO_PYQIR
    assert OpType.S in _TK_TO_PYQIR
    assert OpType.Sdg in _TK_TO_PYQIR
    assert OpType.T in _TK_TO_PYQIR
    assert OpType.Tdg in _TK_TO_PYQIR
    assert OpType.Reset in _TK_TO_PYQIR
    assert OpType.CX in _TK_TO_PYQIR
    assert OpType.CZ in _TK_TO_PYQIR
    assert OpType.Measure in _TK_TO_PYQIR
    assert OpType.Rx in _TK_TO_PYQIR
    assert OpType.Ry in _TK_TO_PYQIR
    assert OpType.Rz in _TK_TO_PYQIR
    assert OpType.CopyBits in _TK_TO_PYQIR


def test_gateset_ii() -> None:
    for opt in _TK_TO_PYQIR:
        assert type(opt) == type(OpType.H)


if __name__ == "__main__":
    test_gateset()
    test_gateset_ii()
