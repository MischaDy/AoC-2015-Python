import operator
from itertools import starmap
from typing import List

from Day7.instruction import Instruction


class Circuit:
    OP_DICT = {
        'AND': operator.and_,
        'OR': operator.or_,
        'NOT': operator.inv,
        'LSHIFT': operator.lshift,
        'RSHIFT': operator.rshift,
        'ID': lambda x: x
    }
    MAX_VALUE = 2 ** 16  # exclusive

    def __init__(self, instrs: List[Instruction]):
        self.instrs = instrs
        self.wires = self.get_wires(instrs)

    @classmethod
    def get_wires(cls, instrs):
        wires = {}
        for instr in instrs:
            wires[instr.out_wire] = 0
            for in_wire in instr.get_in_wires():
                wires[in_wire] = 0

        return wires

    def run(self):
        for instr in self.instrs:
            op = self.OP_DICT[instr.op]
            inputs = map(self.inp_str_to_val, instr.op_inputs)
            self.wires[instr.out_wire] = op(*inputs) % self.MAX_VALUE

    def inp_str_to_val(self, op_input):
        if op_input.isdigit():
            return int(op_input)
        return self.wires[op_input]

    def get_signal(self, wire):
        return self.wires[wire]

    def __str__(self):
        return get_sorted_dict_str(self.wires)


def get_sorted_dict_str(dict_):
    dict_strs = starmap(lambda k, v: f'{k}: {v}', sorted(dict_.items()))
    return '{' + ', '.join(dict_strs) + '}'
