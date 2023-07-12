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

"""
public api for qir conversion from pytket
"""

from typing import Union

# import pyqir
import llvmlite.ir as ll  # type: ignore
import pyqir

from pytket.circuit import Circuit, OpType

from pytket.circuit import (  # type: ignore
    BitRegister,
    ClassicalExpBox,
    Command,
    Conditional,
    RangePredicateOp,
    CopyBitsOp,
    Op,
    MetaOp,
    SetBitsOp,
    WASMOp,
    OpType,
)


def pytket_to_qir_ll(
    circ: Circuit,
    name: str = "Generated from input pytket circuit",
    pyqir_compatibility: bool = True,
) -> Union[str, bytes, None]:
    """converts given pytket circuit to qir

    :param circ: given circuit
    :type circ: pytket circuit
    :param name: name for the qir module created
    :type name: str
    """

    if len(circ.q_registers) > 1 or (
        len(circ.q_registers) == 1 and circ.q_registers[0].name != "q"
    ):
        raise ValueError(
            """The circuit that should be converted should only have the default
            quantum register. You can convert it using the pytket
            compiler pass `FlattenRelabelRegistersPass`."""
        )

    for creg in circ.c_registers:
        if creg.size > 64:
            raise ValueError("classical registers must not have more than 64 bits")

    module = ll.Module(name)

    bit = ll.IntType(1)
    int8 = ll.IntType(8)
    int32 = ll.IntType(32)
    int64 = ll.IntType(64)
    int8ptr = int8.as_pointer()
    void = ll.VoidType()

    module.add_named_metadata(
        "llvm.module.flags", ["qir_major_version", ll.Constant(int32, 1)]
    )
    module.add_named_metadata(
        "llvm.module.flags", ["qir_minor_version", ll.Constant(int32, 0)]
    )
    module.add_named_metadata(
        "llvm.module.flags", ["dynamic_qubit_management", ll.Constant(bit, 0)]
    )
    module.add_named_metadata(
        "llvm.module.flags", ["dynamic_result_management", ll.Constant(bit, 0)]
    )

    r = ll.global_context.get_identified_type("Result")
    rp = ll.PointerType(r)

    if circ.depth() > 0:
        q = ll.global_context.get_identified_type("Qubit")
        qp = ll.PointerType(q)

    register = [None]

    print(circ.bits)
    print(type(circ.bits))

    if len(circ.bits) > 0:
        register[0] = (int8ptr("c"), int64(0))

    main_fntype = ll.FunctionType(void, [])
    main_func = ll.Function(module, main_fntype, name="main")

    main_func.attributes.add("alwaysinline")
    main_func.attributes.add("readonly")
    main_func.attributes.add("optsize")

    bb_entry = main_func.append_basic_block(name="entry")

    builder = ll.IRBuilder()
    builder.position_at_end(bb_entry)

    qir_functions = {}

    for command in circ:
        op = command.op

        if op.type == OpType.H:

            assert len(command.bits) == 0
            assert len(command.qubits) == 1
            assert len(op.params) == 0

            if OpType.H not in qir_functions:
                h_fntype = ll.FunctionType(void, [qp])
                qir_functions[OpType.H] = ll.GlobalVariable(
                    module, h_fntype, name="__quantum__qis__h__body"
                )

            builder.call(
                qir_functions[OpType.H],
                [ll.Constant(int64, command.qubits[0].index[0]).inttoptr(qp)],
            )

        elif isinstance(op, Conditional):

            # conditional_circuit = self._rebase_op_to_gateset(
            #    op.op, command.args[op.width :]
            # )
            # condition_name = command.args[0].reg_name
            # condition_bit_index = command.args[0].index[0]

            classical_fntype = ll.FunctionType(int64, [int64])
            cl_fun = ll.GlobalVariable(module, classical_fntype, name="__something__")

            value0 = builder.call(
                cl_fun,
                [ll.Constant(int64, command.args[0].index[0])],
            )

            cond = builder.call(
                cl_fun,
                [ll.Constant(int64, command.args[0].index[0])],
            )

            with builder.if_else(cond) as (then, otherwise):
                with then:
                    bb_1 = builder.basic_block
                    value1 = builder.call(
                        cl_fun,
                        [ll.Constant(int64, command.args[0].index[0])],
                    )

                with otherwise:
                    # emit instructions for when the predicate is false
                    # emit instructions following the if-else block
                    bb_2 = builder.basic_block
                    value2 = builder.call(
                        cl_fun,
                        [ll.Constant(int64, command.args[0].index[0])],
                    )

            p = builder.phi(int64)
            p.add_incoming(value1, bb_1)  # value2)
            p.add_incoming(value2, bb_2)  # value2)

            value3 = builder.call(
                cl_fun,
                [p],
            )
            value4 = ll.Constant(int64, command.args[0].index[0])
            value5 = builder.call(
                cl_fun,
                [value4],
            )

        else:
            assert 1 == 0

    start_output_fntype = ll.FunctionType(void, [])
    start_output_func = ll.GlobalVariable(
        module, start_output_fntype, name="__quantum__rt__tuple_start_record_output"
    )
    builder.call(start_output_func, [])

    if len(circ.bits) > 0:
        int_output_fntype = ll.FunctionType(void, [int64, int8ptr])
        int_output_func = ll.GlobalVariable(
            module, int_output_fntype, name="__quantum__rt__int_record_output"
        )
        builder.call(int_output_func, [register[0][1], register[0][0]])

    end_output_fntype = ll.FunctionType(void, [])
    end_output_func = ll.GlobalVariable(
        module, end_output_fntype, name="__quantum__rt__tuple_end_record_output"
    )
    builder.call(end_output_func, [])

    if pyqir_compatibility:

        initial_result = str(module)

        # print(initial_result)
        # exit()

        replacements = {}

        replacements['"Qubit"'] = "Qubit"
        replacements['"Result"'] = "Result"
        replacements['"main"'] = "main"
        replacements[
            '"__quantum__rt__tuple_start_record_output"'
        ] = "__quantum__rt__tuple_start_record_output"
        replacements[
            '"__quantum__rt__int_record_output"'
        ] = "__quantum__rt__int_record_output"
        replacements[
            '"__quantum__rt__tuple_end_record_output"()'
        ] = "__quantum__rt__tuple_end_record_output()\n  ret void"
        replacements["alwaysinline optsize readonly"] = "#0"
        replacements["define void @main() #0\n{"] = "\ndefine void @main() #0 {"
        replacements[
            f'; ModuleID = "{name}"'
        ] = f"; ModuleID = '{name}'\nsource_filename = \"{name}\""

        long_str = """declare i1 @read_bit_from_reg(i64, i64)

declare void @set_one_bit_in_reg(i64, i64, i1)

declare void @set_all_bits_in_reg(i64, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()"""

        if circ.depth() > 0:
            long_str = long_str + "\n\ndeclare void @__quantum__qis__h__body(%Qubit*)"

        replacements[
            """@__quantum__rt__tuple_start_record_output = external global void ()
@"__quantum__rt__tuple_end_record_output" = external global void ()"""
        ] = long_str

        replacements[
            """!llvm.module.flags = !{ !0, !1, !2, !3 }
!0 = !{ !"qir_major_version", i32 1 }
!1 = !{ !"qir_minor_version", i32 0 }
!2 = !{ !"dynamic_qubit_management", i1 0 }
!3 = !{ !"dynamic_result_management", i1 0 }"""
        ] = """\nattributes #0 = { "entry_point" "num_required_qubits"="NUMQUBITS" "num_required_results"="NUMQUBITS" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}\n"""
        replacements[
            "%Result = type opaque\n%Qubit = type opaque"
        ] = "%Qubit = type opaque\n%Result = type opaque"
        replacements['"__quantum__qis__h__body"'] = "__quantum__qis__h__body"
        replacements["inttoptr (i64 0 to %Qubit*)"] = "null"
        replacements["NUMQUBITS"] = f"{len(circ.qubits)}"
        # replacements[""] = ""

        for s, r in replacements.items():
            initial_result = initial_result.replace(s, r)

        def keep_line(line: str) -> bool:
            return (
                ('target triple = "unknown-unknown-unknown"' not in line)
                and ('target datalayout = ""' not in line)
                and (
                    "@__quantum__qis__h__body = external global void (%Qubit*)"
                    not in line
                )
            )

        result = "\n".join(filter(keep_line, initial_result.split("\n")))

        # pyqir.Module.from_ir(pyqir.Context(), result)

        # replace the use of the removed register variable with i64 0
        # result = result.replace("i64 %0", "i64 0")

        for _ in range(10):
            result = result.replace("\n\n\n\n", "\n\n")

        return result  # type: ignore

    else:
        return str(module)
