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

"""
This module defines an extension for the PyQir SimpleModule
for the needs of parsing and generating QIR back and forth
Pytket circuits.
"""

from typing import cast, Optional
from pytket.wasm import WasmFileHandler  # type: ignore

from pyqir import (  # type: ignore
    BasicQisBuilder,
    SimpleModule,
)

from pytket_qir.gatesets.base import CustomGateSet
from pytket_qir.gatesets.pyqir import PYQIR_GATES  # type: ignore


class Module:
    """
    PyQir module extension to account for custom defined input gate set
    and calls to WASM files.
    """

    def __init__(
        self,
        module: Optional[SimpleModule] = None,
        name: Optional[str] = None,
        num_qubits: Optional[int] = None,
        num_results: Optional[int] = None,
        gateset: Optional[CustomGateSet] = None,
        wasm_handler: Optional[WasmFileHandler] = None,
    ) -> None:
        if module is None:
            if any([name, num_qubits, num_results]) == None:
                raise ValueError(
                    "Arguments are not provided correctly for the input module."
                )
            name = cast(str, name)
            num_qubits = cast(int, num_qubits)
            num_results = cast(int, num_results)
            self.module = SimpleModule(name, num_qubits, num_results)
        else:
            self.module = module
        self.builder = self.module.builder
        self.qis = BasicQisBuilder(self.builder)
        self.gateset = gateset if gateset else PYQIR_GATES
        self.wasm_handler = wasm_handler

    @property
    def gateset(self):
        """A getter for the gateset."""
        assert self._gateset is not None
        return self._gateset

    @gateset.setter
    def gateset(self, new_gateset):
        self._gateset = new_gateset
        for v in self._gateset.gateset.values():
            self.__setattr__(
                v.opname.value,
                self.module.add_external_function(
                    self._gateset.template.substitute(
                        opnat=v.opnat.value,
                        opname=v.opname.value,
                        opspec=v.opspec.value,
                    ),
                    self.module.types.function(v.return_type, v.function_signature),
                ),
            )
