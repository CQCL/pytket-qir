# Copyright 2020-2024 Quantinuum
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

import pytest
from utilities import check_qir_result  # type: ignore

from pytket.circuit import Bit, BitRegister, Circuit, Qubit, if_not_bit
from pytket.circuit.logic_exp import (
    reg_eq,
    reg_geq,
    reg_gt,
    reg_leq,
    reg_lt,
    reg_neq,
)
from pytket.passes import FlattenRelabelRegistersPass
from pytket.qir.conversion.api import QIRFormat, pytket_to_qir
import pyqir

def test_pytket_qir_phi() -> None:
    module = pyqir.SimpleModule("phi_add", 1, 1)
    context = module.context
    builder = module.builder
    entry_point = module.entry_point

    entry = module.entry_block
    body = pyqir.BasicBlock(context, "body", entry_point)
    footer = pyqir.BasicBlock(context, "footer", entry_point)

    builder.insert_at_end(entry)
    i32 = pyqir.IntType(context, 32)
    const1 = pyqir.const(i32, 1)
    const2 = pyqir.const(i32, 2)
    sum_two = builder.add(const1, const1)    
    cmp = builder.icmp(pyqir.IntPredicate.EQ, sum_two, const2)
    builder.condbr(cmp, body, footer)

    builder.insert_at_end(body)
    sum_three = builder.add(sum_two, const1)
    builder.br(footer)

    builder.insert_at_end(footer)
    phi = builder.phi(i32)
    phi.add_incoming(sum_two, entry)
    phi.add_incoming(sum_three, body)
    sum_four = builder.add(phi, const1)

    ir = module.ir()    

    print(ir)

    # assert 1 == 2

if __name__ == "__main__":
    test_pytket_qir_phi()
