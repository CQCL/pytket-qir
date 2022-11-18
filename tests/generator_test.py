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

import json
import os
from pathlib import Path
from string import Template
from typing import Generator, List, cast
import pytest  # type: ignore
from pytket import Circuit, OpType  # type: ignore
from pytket.wasm import WasmFileHandler  # type: ignore

from pyqir.generator import bitcode_to_ir, types  # type: ignore

from pytket_qir.gatesets.base import OpName, OpNat, OpSpec, QirGate  # type: ignore

from pytket_qir.gatesets.base import CustomGateSet, CustomQirGate
from pytket_qir.gatesets.pyqir import _TK_TO_PYQIR
from pytket_qir.generator import (
    circuit_to_qir,
    write_qir_file,
)
from pytket_qir.utils import ClassicalExpBoxError, SetBitsOpError


qir_files_dir = Path("./qir_test_files")


class TestPytketToQirGateTranslation:
    """A class to test the gate translation from a pytket circuit to a QIR program."""

    def test_rebase_circuit(self) -> None:
        rebased_circuit_file_name = "RebasedCircuit.ll"
        c = Circuit(2)
        c.CY(0, 1)
        write_qir_file(c, rebased_circuit_file_name)

        with open("RebasedCircuit.ll", "r") as input_file:
            data = input_file.readlines()

        with open(qir_files_dir / "RebasedCircuit.ll", "r") as input_file:
            exp_data = input_file.readlines()

        for line in data:
            assert line in exp_data
        os.remove(rebased_circuit_file_name)

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

    def test_raises_empty_setbit_error(self) -> None:
        c = Circuit(0)
        a = c.add_c_register("a", 0)
        c.add_c_setreg(0, a)  # Only value assignable to empty register.
        with pytest.raises(SetBitsOpError):
            write_qir_file(c, "empty_setbit_circuit.ll")

    def test_raises_empty_classicalexpbox_error(self) -> None:
        c = Circuit(0)
        a = c.add_c_register("a", 0)
        b = c.add_c_register("b", 0)
        c.add_classicalexpbox_register(a ^ b, b)
        with pytest.raises(ClassicalExpBoxError):
            write_qir_file(c, "empty_classicalexpbox_circuit.ll")

    def test_classical_arithmetic(
        self, circuit_classical_arithmetic: Circuit, operators: List
    ):
        with open("ClassicalCircuit.ll", "r") as input_file:
            data = input_file.read()

        with open(qir_files_dir / "ClassicalCircuit.ll", "r") as input_file:
            exp_data = input_file.read()

        assert data == exp_data

    def test_classical_reg2const_arithmetic(
        self, circuit_classical_reg2const_arithmetic: Circuit
    ):
        with open("ClassicalReg2ConstCircuit.ll", "r") as input_file:
            data = input_file.readlines()

        with open(qir_files_dir / "ClassicalReg2ConstCircuit.ll", "r") as input_file:
            exp_data = input_file.readlines()

        for line in data:
            assert line in exp_data

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

    def test_generate_rt_int_record_output_function(self) -> None:
        rt_int_record_output = qir_files_dir / "RtIntRecordOutput.ll"

        with open(rt_int_record_output, "r") as f:
            exp_data = f.read()

        # mod = SimpleModule("test", 0, 0)
        # types = mod.types

        circuit = Circuit()
        c_reg_1 = circuit.add_c_register("c_reg_1", 64)
        c_reg_2 = circuit.add_c_register("c_reg_2", 64)
        output_reg = circuit.add_c_register("output_reg", 64)
        circuit.add_c_setreg(1, c_reg_1)
        circuit.add_c_setreg(2, c_reg_2)
        circuit.add_classicalexpbox_register(c_reg_1 + c_reg_2, output_reg)

        # Extend PyQir base gateset to account for Barrier.
        qir_gate = QirGate(
            opnat=OpNat.RT,
            opname=OpName.INT,
            opspec=OpSpec.REC_OUT,
        )

        _TK_TO_PYQIR[OpType.Barrier] = qir_gate

        qir_barrier = CustomQirGate(
            opnat=OpNat.RT,
            opname=OpName.INT,
            opspec=OpSpec.REC_OUT,
            function_signature=[types.Int(64)],
            return_type=types.VOID,
        )

        _PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}

        ext_pyqir_gates = CustomGateSet(
            name="ExtPyQir",
            template=Template("__quantum__${opnat}__${opname}__${opspec}"),
            base_gateset=set(_TK_TO_PYQIR.keys()),
            gateset={"rt_int": qir_barrier},
            tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
            gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
        )

        data = {"name": "__quantum__rt__integer__record_output", "arg": "output_reg"}
        circuit.add_barrier(units=output_reg, data=json.dumps(data))

        ir_bytes = cast(bytes, circuit_to_qir(circuit, gateset=ext_pyqir_gates))
        ll = str(bitcode_to_ir(ir_bytes))

        assert ll == exp_data

    def test_generate_rt_bool_record_output_function(self) -> None:
        rt_bool_record_output = qir_files_dir / "RtBoolRecordOutput.ll"

        with open(rt_bool_record_output, "r") as f:
            exp_data = f.read()

        # mod = SimpleModule("test", 0, 0)
        # types = mod.types

        circuit = Circuit()
        c_reg_1 = circuit.add_c_register("c_reg_1", 64)
        c_reg_2 = circuit.add_c_register("c_reg_2", 64)
        output_reg = circuit.add_c_register("output_reg", 64)
        circuit.add_c_setreg(1, c_reg_1)
        circuit.add_c_setreg(0, c_reg_2)
        circuit.add_classicalexpbox_register(c_reg_1 + c_reg_2, output_reg)

        # Extend PyQir base gateset to account for Barrier.
        qir_gate = QirGate(
            opnat=OpNat.RT,
            opname=OpName.BOOL,
            opspec=OpSpec.REC_OUT,
        )

        _TK_TO_PYQIR[OpType.Barrier] = qir_gate

        qir_barrier = CustomQirGate(
            opnat=OpNat.RT,
            opname=OpName.BOOL,
            opspec=OpSpec.REC_OUT,
            function_signature=[types.Int(64)],
            return_type=types.VOID,
        )

        _PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}

        ext_pyqir_gates = CustomGateSet(
            name="ExtPyQir",
            template=Template("__quantum__${opnat}__${opname}__${opspec}"),
            base_gateset=set(_TK_TO_PYQIR.keys()),
            gateset={"rt_bool": qir_barrier},
            tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
            gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
        )

        data = {"name": "__quantum__rt__bool__record_output", "arg": "output_reg"}
        circuit.add_barrier(units=output_reg, data=json.dumps(data))

        ir_bytes = cast(bytes, circuit_to_qir(circuit, gateset=ext_pyqir_gates))
        ll = str(bitcode_to_ir(ir_bytes))

        assert ll == exp_data

    def test_generate_rt_result_record_output_function(self) -> None:
        rt_result_record_output = qir_files_dir / "RtResultRecordOutput.ll"

        with open(rt_result_record_output, "r") as f:
            exp_data = f.read()

        # mod = SimpleModule("test", 0, 1)
        # types = mod.types

        circuit = Circuit(0, 1)
        c_reg = circuit.get_c_register("c")

        # Extend PyQir base gateset to account for Barrier.
        qir_gate = QirGate(
            opnat=OpNat.RT,
            opname=OpName.RES,
            opspec=OpSpec.REC_OUT,
        )

        _TK_TO_PYQIR[OpType.Barrier] = qir_gate

        qir_barrier = CustomQirGate(
            opnat=OpNat.RT,
            opname=OpName.RES,
            opspec=OpSpec.REC_OUT,
            function_signature=[types.RESULT],
            return_type=types.VOID,
        )

        _PYQIR_TO_TK = {v: k for k, v in _TK_TO_PYQIR.items()}

        ext_pyqir_gates = CustomGateSet(
            name="ExtPyQir",
            template=Template("__quantum__${opnat}__${opname}__${opspec}"),
            base_gateset=set(_TK_TO_PYQIR.keys()),
            gateset={"rt_bool": qir_barrier},
            tk_to_gateset=lambda optype: _TK_TO_PYQIR[optype],
            gateset_to_tk=lambda gate: _PYQIR_TO_TK[gate],
        )

        data = {"name": "__quantum__rt__result__record_output", "arg": "c", "index": 0}
        circuit.add_barrier(units=c_reg, data=json.dumps(data))

        ir_bytes = cast(bytes, circuit_to_qir(circuit, gateset=ext_pyqir_gates))
        ll = str(bitcode_to_ir(ir_bytes))

        assert ll == exp_data

    def test_generate_read_result(self) -> None:
        read_result_file_path = qir_files_dir / "ReadResult.ll"

        with open(read_result_file_path, "r") as f:
            exp_data = f.read()

        circuit = Circuit(0, 2)
        result_register = circuit.get_c_register("c")
        target_register = circuit.add_c_register("%0", result_register.size)

        circuit.add_c_copybits([result_register[0]], [target_register[0]])
        circuit.add_c_copybits([result_register[1]], [target_register[1]])

        # Extend PyQir base gateset to account for Barrier.
        # qir_gate = _TK_TO_PYQIR[OpType.CopyBits]

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

        ir_bytes = cast(bytes, circuit_to_qir(circuit, gateset=ext_pyqir_gates))
        ll = str(bitcode_to_ir(ir_bytes))

        assert ll == exp_data

    @pytest.mark.skip
    def test_generate_wasmop_with_nonempty_inputs(self) -> None:
        wasm_file_path = qir_files_dir / "wasm_adder.wasm"
        wasm_handler = WasmFileHandler(str(wasm_file_path))

        with open(qir_files_dir / "WASM.ll", "r") as input_file:
            exp_data = input_file.read()

        circuit = Circuit()
        c0 = circuit.add_c_register("c0", 64)
        c1 = circuit.add_c_register("c1", 64)

        circuit.add_wasm_to_reg("add_one", wasm_handler, [c0], [c1])

        ir_bytes = cast(bytes, circuit_to_qir(circuit))
        ll = str(bitcode_to_ir(ir_bytes))

        assert ll in exp_data

    @pytest.mark.skip
    def test_generate_wasmop_with_empty_inputs(self) -> None:
        wasm_file_path = qir_files_dir / "wasm_empty_adder.wasm"
        wasm_handler = WasmFileHandler(str(wasm_file_path))

        with open(qir_files_dir / "WASM_noinputs.ll", "r") as input_file:
            exp_data = input_file.read()

        circuit = Circuit()
        c1 = circuit.add_c_register("c1", 64)

        circuit.add_wasm_to_reg("empty_add_one", wasm_handler, [], [c1])
        ir = circuit_to_qir(circuit, wasm_path=wasm_file_path)
        ir_bytes = cast(bytes, ir)

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
            data = input_file.read()

        test_file_path = qir_files_dir / pytket_nested_conditionals_file_name

        with open(test_file_path, "r") as input_file:
            exp_data = input_file.read()

        assert data == exp_data

class TestIrAndBcFileGeneration:
    """A class to test the generation of .ll and .bc files and their equivalence."""

    def test_bell_circuit(self) -> None:

        bell_circuit = Circuit(2, name="Bell Test")
        bell_circuit.H(0)
        bell_circuit.CX(0, 1)
        bell_circuit.measure_all()

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

    @pytest.mark.skip
    def test_roundtrip_teleport_chain(self):
        pass
