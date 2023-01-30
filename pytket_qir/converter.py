from collections import OrderedDict
from dataclasses import dataclass
import os
from typing import Optional, cast, List, Union

from pytket import Circuit  # type: ignore
from pytket.circuit import (  # type: ignore
    CircBox,
)
from pytket.circuit.logic_exp import BitNot, if_bit  # type: ignore
from pytket.wasm import WasmFileHandler  # type: ignore

from pyqir.parser import (  # type: ignore
    QirBlock,
    QirBrTerminator,
    QirCondBrTerminator,
    QirLocalOperand,
    QirModule,
    QirRetTerminator,
)
from pyqir.generator import ir_to_bitcode, types, SimpleModule  # type: ignore

from pytket_qir.gatesets.base import CustomGateSet
from pytket_qir.generator import QirGenerator
from pytket_qir.module import Module
from pytket_qir.parser import QirParser
from pytket_qir.utils import (
    ConverterException,
    QirFormat,
)


@dataclass
class Block:
    name: str
    succs: List
    preds: List
    composition: List
    visited: bool = False


def topological_sort(digraph: dict) -> dict:
    """Topologically sort a digraph, a dict of <nodes, list of successors>."""
    # Mapping nodes to indegrees.
    indegrees = {node: 0 for node in digraph}
    for node in digraph:
        for succ in digraph[node]:
            indegrees[succ] += 1

    nodes_with_empty_preds = []
    for node in digraph:
        if indegrees[node] == 0:
            nodes_with_empty_preds.append(node)

    topological_ordering = {}
    while len(nodes_with_empty_preds) > 0:
        node = nodes_with_empty_preds.pop()
        topological_ordering[node] = digraph[node]
        for succ in digraph[node]:
            indegrees[succ] -= 1
            if indegrees[succ] == 0:
                nodes_with_empty_preds.append(succ)

    if len(topological_ordering) == len(digraph):
        return topological_ordering
    else:
        raise ConverterException(
            "A cycle exists in the graph, there is no topological order to be found."
        )


class QirConverter:
    """
    A class to build and convert the QIR control-flow graph to a pytket circuit.

    In more details, it works by following the next steps:
    - Create a CFG from a topologically sort the sequence of blocks from the QIR program.
    - Apply optimisation to the CFG if so.
    - Iterate through each block in the CFG and call the QirParser to return the corresponding
      circuit and compute the guard.
    - Add previously generated circuits to the main one as properly conditioned CircBoxes.
    """

    def __init__(
        self,
        file_path: str,
        optimisation_level: int = 0,
        gateset: Optional[CustomGateSet] = None,
        wasm_handler: Optional[WasmFileHandler] = None,
        wasm_int_type: types.Int = types.Int(32),
        qir_int_type: types.Int = types.Int(64),
    ) -> None:
        self.module = QirModule(file_path)
        self.module_function = self.module.functions[0]
        self.parser = QirParser(
            qir_module=self.module,
            gateset=gateset,
            wasm_handler=wasm_handler,
            wasm_int_type=wasm_int_type,
            qir_int_type=qir_int_type,
        )
        self.cfg = OrderedDict()
        self.rewritten_cfg = self.cfg
        if optimisation_level == 1:
            self.collapse_blocks()
        self.circuit = self.cfg_to_circuit()

    @property
    def successors(self):
        return self._successors

    @successors.setter
    def successors(self, value):
        """
        Iterate through the sequence of blocks from the QIR program
        to create a list of successors and store in the successors
        class member.
        """
        self._successors = OrderedDict()
        for block in self.module.functions[0].blocks:
            block_name = block.name
            term = block.terminator
            if block_name == "entry":
                self.edges[block_name] = {block_name: True}
            if isinstance(term, QirCondBrTerminator):
                f = lambda el: el.name == term.true_dest or el.name == term.false_dest
                self._successors[block_name] = list(
                    map(lambda el: el.name, filter(f, self.module.functions[0].blocks))
                )
                self.edges[block_name] = {
                    term.true_dest: True,
                    term.false_dest: False,
                }
            elif isinstance(term, QirBrTerminator):
                self._successors[block_name] = [term.dest]
                self.edges[block_name] = {term.dest: None}
            elif isinstance(term, QirRetTerminator):
                self._successors[block_name] = []
                self.edges[block_name] = {}
        # Sort the DAG.
        sorted_dag = topological_sort(self._successors)
        # Update (sort) the list of successors.
        for block, succs in sorted_dag.items():
            if len(succs) > 1:
                f = (
                    lambda el: el == self._successors[block][0]
                    or el == self._successors[block][1]
                )
                self._successors[block] = list(filter(f, self._successors))

    @property
    def predecessors(self):
        return self._predecessors

    @predecessors.setter
    def predecessors(self, value):
        """
        Iterate the successors data structure in reverse order to create a
        list of predecessors and store it in the predecessors class member.
        """
        self._predecessors = OrderedDict()
        reversed_succs = reversed(self.successors)
        reversed_succs_list = list(reversed_succs)
        for curr_block_index, curr_block_name in enumerate(reversed_succs_list):
            predecessors = []
            for next_block_name in reversed_succs_list[curr_block_index + 1 :]:
                if curr_block_name in self.successors[next_block_name]:
                    predecessors.append(next_block_name)
            self._predecessors[curr_block_name] = predecessors

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        self._conditions = value

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, value):
        self._edges = value

    @property
    def local_conditions(self):
        return self._local_conditions

    @local_conditions.setter
    def local_conditions(self, value):
        self._local_conditions = value

    @property
    def cfg(self):
        return self._cfg

    @cfg.setter
    def cfg(self, value) -> None:
        """
        Create and store the CFG by iterating through the topologically
        sorted list of blocks and instantiate the Block data structure
        for each one of them.
        """
        # Following three class members are initialised to empty dicts.
        self.conditions = {}
        self.edges = {}
        self.local_conditions = {}
        # Initliase to concrete CFG structure from the QIR program
        #  by calling the setters.
        self.successors = {}
        self.predecessors = {}

        self._cfg = value
        if not value:  # Checking for empty input dict.
            for block_name, succs in self.successors.items():
                block_inst = Block(
                    name=block_name,
                    succs=succs,
                    preds=self.predecessors[block_name],
                    composition=[block_name],
                    visited=False,
                )
                self._cfg[block_name] = block_inst

    def cfg_to_circuit(self) -> Circuit:
        main_circuit = Circuit(self.parser.qubits, self.parser.bits + 2)
        # Setting condition and local condition to True
        # for the predecessor of the entry block.
        main_circuit.add_c_setbits([1, 1], [self.parser.bits, self.parser.bits + 1])
        condition_bit = main_circuit.get_c_register("c")[self.parser.bits]
        self.conditions["entry_pred"] = condition_bit
        local_condition_bit = main_circuit.get_c_register("c")[self.parser.bits + 1]

        self.local_conditions["entry_pred"] = local_condition_bit
        for block_name, block in self.rewritten_cfg.items():
            curr_qir_block = cast(
                QirBlock, self.module_function.get_block_by_name(block_name)
            )
            circuit = Circuit(self.parser.qubits, self.parser.bits + 2)
            # Setting the condition True for each block.
            circuit.add_c_setbits([1], [self.parser.bits])
            condition_bit = circuit.get_c_register("c")[self.parser.bits]
            self.conditions[block_name] = condition_bit
            for compo_block in block.composition:
                qir_block = cast(
                    QirBlock, self.module_function.get_block_by_name(compo_block)
                )
                new_circuit = self.parser.block_to_circuit(
                    qir_block, Circuit(self.parser.qubits, self.parser.bits + 2)
                )
                circuit.append(new_circuit)
            term = curr_qir_block.terminator
            if isinstance(term, QirCondBrTerminator):
                term_condition = cast(QirLocalOperand, term.condition)
                condition_name = "%" + str(term_condition.name)
                # Retrieving the condition bit from the circuit log.
                self.local_conditions[block_name] = self.parser.ssa_vars[condition_name]
            elif isinstance(term, (QirBrTerminator, QirRetTerminator)):
                # Return is considered an unconditional branch.
                self.local_conditions[block_name] = condition_bit
            preds = block.preds
            if not preds:  # Entry block.
                expr = self.local_conditions["entry_pred"]
                self.conditions[block_name] = self.conditions[block_name] | (
                    self.conditions["entry_pred"] & expr
                )
            else:
                for pred in preds:
                    if (
                        self.edges[pred][block_name] == None
                        or self.edges[pred][block_name] == True
                    ):
                        expr = self.local_conditions[pred]
                    elif self.edges[pred][block_name] == False:
                        expr = BitNot(self.local_conditions[pred])
                    self.conditions[block_name] = self.conditions[block_name] | (
                        self.conditions[pred] & expr
                    )

            # Add extra bits created in the sub-circuit to the main one.
            for bit in set(circuit.bits) - set(main_circuit.bits):
                main_circuit.add_bit(bit)
            circ_box = CircBox(circuit)
            arguments = [qubit.index[0] for qubit in circuit.qubits] + [
                bit.index[0] for bit in circuit.bits
            ]  # Order matters.
            main_circuit.add_circbox(
                circ_box, arguments, condition=if_bit(self.conditions[block_name])
            )
        return main_circuit

    def apply_contraction(self, block: QirBlock) -> Block:
        """Attempt to contract blocks recursively."""
        term = block.terminator
        has_jump = isinstance(term, QirBrTerminator)
        curr_block = self.cfg[block.name]
        curr_block.visited = True
        if has_jump:
            next_block = cast(
                QirBlock, self.module.functions[0].get_block_by_name(term.dest)
            )
            # A precondition to apply the rewrite rule.
            continue_next = len(self.cfg[next_block.name].preds) == 1

            if continue_next:  # Recurse through the chain of jumps.
                next_block_inst = self.apply_contraction(next_block)
                return Block(
                    name=curr_block.name,
                    succs=next_block_inst.succs,
                    preds=curr_block.preds,
                    composition=[block.name] + next_block_inst.composition,
                )
            else:  # Return the current block.
                return curr_block
        return curr_block

    def collapse_blocks(self) -> None:
        """Detect and collapse chains of linear blocks."""
        rewritten_cfg = OrderedDict()
        for block_name, block in self.rewritten_cfg.items():
            if not block.visited:
                qir_block = self.module_function.get_block_by_name(block_name)
                contracted_block = self.apply_contraction(qir_block)
                if contracted_block is not block:  # Contractions have occured.
                    rewritten_cfg[block.name] = contracted_block
                    # Update successors's predecessors to contracted block.
                    for succ in contracted_block.succs:
                        preds = [
                            pred.replace(contracted_block.composition[-1], block_name)
                            for pred in self.rewritten_cfg[succ].preds
                        ]
                        self.rewritten_cfg[succ].preds = preds
                    # Update the edges datastructure for later use.
                    self.edges[contracted_block.name] = self.edges[
                        contracted_block.composition[-1]
                    ]
                    for block in contracted_block.composition[1:]:
                        del self.edges[block]
                else:
                    rewritten_cfg[block_name] = block
        # Reset visited fields to false for later reuse.
        for block in rewritten_cfg.values():
            block.visited = False
        self.rewritten_cfg = rewritten_cfg


def circuit_from_qir(
    input_file: Union[str, os.PathLike],
    optimisation_level: int = 0,
    gateset: Optional[CustomGateSet] = None,
    wasm_handler: Optional[WasmFileHandler] = None,
    wasm_int_type: types.Int = types.Int(32),
) -> Circuit:
    root, ext = os.path.splitext(os.path.basename(input_file))
    input_file_str = str(input_file)
    output_bc_file: str = ""
    if ext not in [".ll", ".bc"]:
        raise TypeError("Can only convert '.bc' or '.ll' files.")
    if ext == ".ll":
        with open(input_file_str, "r") as f:
            data = f.read()
        output_bc_file = root + ".bc"
        with open(output_bc_file, "wb") as o:
            o.write(ir_to_bitcode(data))
        input_file_str = output_bc_file
    converter = QirConverter(
        input_file_str, optimisation_level, gateset, wasm_handler, wasm_int_type
    )
    circuit = converter.circuit
    # Attach few fields to the circuit.
    circuit.cfg = converter.rewritten_cfg
    circuit.ssa_vars = converter.parser.ssa_vars
    return circuit
