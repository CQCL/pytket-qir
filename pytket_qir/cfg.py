from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional, cast, List

from pyqir.parser import (
    QirBlock,
    QirBrTerminator,
    QirCondBrTerminator,
    QirModule,
    QirRetTerminator,
)


@dataclass
class Block:
    name: str
    succs: List
    preds: List
    composition: List
    visited: bool = False
    condition: Optional[bool] = None


class CfgAnalyser:
    """
    A class to build and analyse the QIR control-flow graph
    and produce a pytket circuit compliant graph.
    """

    def __init__(self, file_path: str) -> None:
        self.module = QirModule(file_path)
        self.cfg = {}

    @property
    def successors(self):
        return self._successors

    @successors.setter
    def successors(self, value):
        self._successors = OrderedDict()
        for block in self.module.functions[0].blocks:
            term = block.terminator
            if isinstance(term, QirCondBrTerminator):
                f = lambda el: el.name == term.true_dest or el.name == term.false_dest
                self._successors[block.name] = list(
                    map(lambda el: el.name, filter(f, self.module.functions[0].blocks))
                )
                self.conditions[term.true_dest] = True
                self.conditions[term.false_dest] = False
            elif isinstance(term, QirBrTerminator):
                self._successors[block.name] = [term.dest]
            elif isinstance(term, QirRetTerminator):
                self._successors[block.name] = []

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

    def _get_preds(self, succs: dict) -> dict:
        """
        Given a dict of successors, invert that mapping an return a dict
        of predecessors.
        """
        preds = OrderedDict()
        reversed_succs = reversed(succs)
        reversed_succs_list = list(reversed_succs)
        for curr_block_index, curr_block_name in enumerate(reversed_succs_list):
            predecessors = []
            for next_block_name in reversed_succs_list[curr_block_index + 1 :]:
                if curr_block_name in self.successors[next_block_name]:
                    predecessors.append(next_block_name)
            preds[curr_block_name] = predecessors
        return preds

    @property
    def cfg(self):
        return self._cfg

    @cfg.setter
    def cfg(self, value) -> None:
        self.conditions = {}
        self.successors = {}
        self.predecessors = {}

        self._cfg = value
        if not value:  # Checking for empty input dict.
            for block in self.module.functions[0].blocks:
                block_inst = Block(
                    name=block.name,
                    succs=self.successors[block.name],
                    preds=self.predecessors[block.name],
                    composition=[block.name],
                    visited=False,
                    condition=self.conditions.get(block.name),
                )
                self._cfg[block.name] = block_inst

    def apply_contraction(self, block) -> None:
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
                    condition=curr_block.condition,
                )
            else:  # Return the current block.
                return curr_block
        return curr_block

    def collapse_blocks(self) -> None:
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
