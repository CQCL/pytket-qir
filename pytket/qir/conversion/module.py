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

"""
This module defines an extension for the PyQir SimpleModule
for the needs of generating QIR from Pytket circuits.
"""

from typing import Optional

from pyqir import BasicQisBuilder, SimpleModule

from pytket.wasm import WasmFileHandler

from .gatesets import PYQIR_GATES


class tketqirModule:
    """
    PyQir module extension to account for custom defined input gate set
    and calls to WASM files.
    """

    def __init__(
        self,
        name: str,
        num_qubits: int,
        num_results: int,
        wasm_handler: Optional[WasmFileHandler] = None,
    ) -> None:
        self.module = SimpleModule(name, num_qubits, num_results)

        self.builder = self.module.builder
        self.context = self.module.context
        self.qis = BasicQisBuilder(self.builder)
        self.gateset = PYQIR_GATES
        self.wasm_handler = wasm_handler
