from collections import OrderedDict
from dataclasses import dataclass
import os
from typing import Optional, cast, List, Union

from pytket import Circuit
from pytket.circuit import CircBox  # type: ignore
from pytket.circuit.logic_exp import BitNot, if_bit
from pytket.wasm import WasmFileHandler

from pyqir.parser import (
    QirBlock,
    QirBrTerminator,
    QirCondBrTerminator,
    QirLocalOperand,
    QirModule,
    QirRetTerminator,
)
from pyqir.generator import ir_to_bitcode, types  # type: ignore

from pytket_qir.gatesets.base import CustomGateSet
from pytket_qir.parser import QirParser
from pytket_qir.utils import CfgException


@dataclass
class Block:
    name: str
    succs: List
    preds: List
    composition: List
    visited: bool = False


def topological_sort(digraph: dict):
    """Topologically sort a digraph, a dict of <nodes, set of successors>."""
    # Mapping nodes to indegrees.
    indegrees = {node: 0 for node in digraph}
    for node in digraph:
        for succ in digraph[node]:
            indegrees[succ] += 1

    nodes_with_empty_preds = []
    for node in digraph:
        if indegrees[node] == 0:
            nodes_with_empty_preds.append(node)

    topological_ordering = []
    while len(nodes_with_empty_preds) > 0:
        node = nodes_with_empty_preds.pop()
        topological_ordering.append(node)
        for succ in digraph[node]:
            indegrees[succ] -= 1
            if indegrees[succ] == 0:
                nodes_with_empty_preds.append(succ)

    if len(topological_ordering) == len(digraph):
        return topological_ordering
    else:
        raise CfgException(
            "A cycle exists in the graph, there is no topological order to be found."
        )


class QirConverter:
    """
    A class to build and convert the QIR control-flow graph to a pytket circuit.
    """

    def __init__(
        self,
        file_path: str,
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
        self.circuit = self.cfg_to_circuit()

    @property
    def successors(self):
        return self._successors

    @successors.setter
    def successors(self, value):
        self._successors = OrderedDict()
        for block in self.module.functions[0].blocks:
            block_name = block.name
            term = block.terminator
            # self.conditions[block_name] = True

            # import pdb; pdb.set_trace()
            if block_name == "entry":
                # self.conditions["entry_pred"] = True
                # self.local_conditions["entry_pred"] = True
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

    @property
    def predecessors(self):
        return self._predecessors

    @predecessors.setter
    def predecessors(self, value):
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
        # import pdb; pdb.set_trace()
        self.conditions = {}
        self.edges = {}
        self.local_conditions = {}
        self.successors = {}
        self.predecessors = {}
        # import pdb; pdb.set_trace()

        sorted_dag = topological_sort(self.successors)

        self._cfg = value
        if not value:  # Checking for empty input dict.
            for block_name in sorted_dag:
                block_inst = Block(
                    name=block_name,
                    succs=self.successors[block_name],
                    preds=self.predecessors[block_name],
                    composition=[block_name],
                    visited=False,
                )
                # f = lambda b: b if b.condition else None
                self._cfg[block_name] = block_inst
        # import pdb; pdb.set_trace()

    def cfg_to_circuit(self) -> Circuit:
        main_circuit = Circuit(self.parser.qubits, self.parser.bits + 2)
        # Setting condition and local condition to True
        # for the predecessor of the entry block.
        main_circuit.add_c_setbits([1, 1], [self.parser.bits, self.parser.bits + 1])
        condition_bit = main_circuit.get_c_register("c")[self.parser.bits]
        self.conditions["entry_pred"] = condition_bit
        local_condition_bit = main_circuit.get_c_register("c")[self.parser.bits + 1]
        self.local_conditions["entry_pred"] = local_condition_bit
        for block_name in self.cfg:
            block = cast(QirBlock, self.module_function.get_block_by_name(block_name))
            new_circuit = Circuit(self.parser.qubits, self.parser.bits + 2)
            # Setting the condition True for each block.
            new_circuit.add_c_setbits([1], [self.parser.bits])
            condition_bit = new_circuit.get_c_register("c")[self.parser.bits]
            self.conditions[block_name] = condition_bit
            circuit = self.parser.block_to_circuit(block, new_circuit)
            term = block.terminator
            if isinstance(term, QirCondBrTerminator):
                term_condition = cast(QirLocalOperand, term.condition)
                condition_name = "%" + str(term_condition.name)
                # Retrieving the condition bit from the circuit log.
                self.local_conditions[block_name] = self.parser.ssa_vars[condition_name]
            elif isinstance(term, (QirBrTerminator, QirRetTerminator)):
                # Return is considered an unconditional branch.
                self.local_conditions[block_name] = condition_bit
            preds = self.predecessors[block_name]
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

    def apply_contraction(self, block) -> Block:
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

    def collapse_blocks(self) -> dict:
        """
        Detect and collapse chains of linear blocks.

        Return a rewritten CFG where all blocks have in-degree exactly one
        and out-degree greater or equal to two.
        """
        rewritten_cfg = {}
        for block in self.module.functions[0].blocks:
            if not self.cfg[block.name].visited:
                contracted_block = self.apply_contraction(block)
                if contracted_block is not self.cfg[block.name]:
                    rewritten_cfg[block.name] = contracted_block
                    # Update successors's predecessors to contracted block.
                    for succ in contracted_block.succs:
                        preds = [
                            pred.replace(contracted_block.composition[-1], block.name)
                            for pred in self.cfg[succ].preds
                        ]
                        self.cfg[succ].preds = preds
                else:
                    rewritten_cfg[block.name] = self.cfg[block.name]
        # Reset values for later reuse.
        for block_name in self.cfg:
            self.cfg[block_name].visited = False
        self.rewritten_cfg = rewritten_cfg
        return rewritten_cfg

    def insert_trivial_blocks(self) -> None:
        """
        Insert trivial blocks to conform the CFG to CircBox unique input and
        output conditions.
        """
        trivial_blocks = {}
        for block_name, curr_block in self.rewritten_cfg.items():
            succs = curr_block.succs
            for succ in succs:
                next_succs = self.rewritten_cfg[succ].succs
                if match_succ := list(set(next_succs).intersection(succs)):
                    first_succ = match_succ[0]
                    match_block = self.rewritten_cfg[first_succ]
                    # Create a trivial block with a unique name.
                    trivial_block_name = block_name + "_trivial_block"
                    trivial_blocks[trivial_block_name] = Block(
                        name=trivial_block_name,
                        succs=[match_block.name],
                        preds=[block_name],
                        composition=[trivial_block_name],
                        visited=False,
                    )
                    # Update successor and predecessor.
                    match_block.preds = [
                        pred.replace(block_name, trivial_block_name)
                        for pred in match_block.preds
                    ]
                    curr_block.succs = [
                        succ.replace(match_block.name, trivial_block_name)
                        for succ in curr_block.succs
                    ]

        self.rewritten_cfg.update(trivial_blocks)

    def split_fork_to_binary(self) -> None:
        def cart_prod(l: List):
            """
            Return a Cartesian product without reflective nor symmetric elements
            which pair of elements have common ancestor in the CFG.
            """
            for index1, el1 in enumerate(l[:-1]):
                el1_block = self.rewritten_cfg[el1]
                for el2 in l[index1 + 1 :]:
                    el2_block = self.rewritten_cfg[el2]
                    if set(el1_block.preds).intersection(el2_block.preds):
                        yield (el1, el2)

        trivial_blocks = {}
        for block_name, curr_block in self.rewritten_cfg.items():
            if len(curr_block.preds) > 2:
                # Find pairs of distinct predecessors with common branching ancestor.
                print(curr_block.preds)
                for pair in cart_prod(curr_block.preds):
                    print(pair)
                    import pdb

                    pdb.set_trace()
                    # Create a trivial block with a unique name.
                    trivial_block_name = block_name + "_trivial_block"
                    trivial_blocks[trivial_block_name] = Block(
                        name=trivial_block_name,
                        succs=[curr_block.name],
                        preds=list(pair),
                        composition=[trivial_block_name],
                        visited=False,
                    )
                    # Update successor and predecessor.
                    d = {pair[0]: trivial_block_name, pair[1]: trivial_block_name}
                    curr_block.preds = list(
                        dict.fromkeys(
                            [d.get(el, el) for el in curr_block.preds]
                        )  # Remove duplicates and guarantee order.
                    )
                    for el in pair:
                        self.rewritten_cfg[el].succs = [trivial_block_name]
        self.rewritten_cfg.update(trivial_blocks)


def circuit_from_qir(
    input_file: Union[str, os.PathLike],
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
    converter = QirConverter(input_file_str, gateset, wasm_handler, wasm_int_type)
    circuit = converter.circuit
    # Attach few fields to the circuit.
    circuit.cfg = converter.cfg
    circuit.ssa_vars = converter.parser.ssa_vars
    return circuit
