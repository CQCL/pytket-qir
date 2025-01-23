# Copyright Quantinuum
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

from utilities import check_qir_result  # type: ignore

from pytket.circuit import (
    Circuit,
    reg_eq,
    reg_geq,
    reg_gt,
    reg_leq,
    reg_lt,
    reg_neq,
)
from pytket.qir.conversion.api import QIRFormat, pytket_to_qir


def test_pytket_qir_rangepredicate() -> None:
    # test conditional handling with range predicate

    circ = Circuit(3)
    a = circ.add_c_register("a", 5)
    circ.H(0, condition=reg_eq(a, 1))
    circ.H(0, condition=reg_neq(a, 1))
    circ.H(0, condition=reg_lt(a, 1))
    circ.H(0, condition=reg_gt(a, 1))
    circ.H(0, condition=reg_leq(a, 1))
    circ.H(0, condition=reg_geq(a, 1))

    result = pytket_to_qir(
        circ, name="test_pytket_qir_rangepredicate", qir_format=QIRFormat.STRING
    )

    check_qir_result(result, "test_pytket_qir_rangepredicate")


if __name__ == "__main__":
    test_pytket_qir_rangepredicate()
