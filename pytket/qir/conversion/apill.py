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

from pytket.circuit import Circuit


def pytket_to_qir_ll(
    circ: Circuit,
    name: str = "Generated from input pytket circuit",
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
    # int8 = ll.IntType(8)
    int32 = ll.IntType(32)
    # int64 = ll.IntType(64)
    # int8ptr = int8.as_pointer()
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

    q = ll.global_context.get_identified_type("Qubit")
    qp = ll.PointerType(q)
    # r = ll.global_context.get_identified_type("Result")

    main_fntype = ll.FunctionType(void, [])
    main_func = ll.Function(module, main_fntype, name="main")

    # main_func.attributes.add("alwaysinline")
    # main_func.attributes.add("readonly")
    # main_func.attributes.add("optsize")

    bb_entry = main_func.append_basic_block(name="entry")

    builder = ll.IRBuilder()
    builder.position_at_end(bb_entry)

    if circ.depth() > 0:

        h_fntype = ll.FunctionType(void, [qp])
        h_func = ll.GlobalVariable(module, h_fntype, name="__quantum__qis__h__body")
        builder.call(h_func, [ll.Constant(qp, 0)])

    result = str(module)

    return result
