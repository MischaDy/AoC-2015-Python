from itertools import filterfalse


class Instruction:
    def __init__(self, op_inputs, out_wire, op='ID'):
        self.op_inputs = op_inputs
        self.out_wire = out_wire
        self.op = op

    @classmethod
    def from_line(cls, line):
        wire_input, out_wire = line.split(' -> ')
        tokens = wire_input.split(' ')
        if len(tokens) == 1:
            op_inputs = [tokens.pop()]
            op = 'ID'
        elif len(tokens) == 2:
            op = tokens[0]  # = 'NOT', because only operator of arity 1
            op_inputs = [tokens.pop()]
        else:  # 3 tokens
            op = tokens.pop(1)
            op_inputs = tokens
        return cls(op_inputs, out_wire, op)

    def get_in_wires(self):
        return list(filterfalse(str.isdigit, self.op_inputs))

    def __str__(self):
        input_list_str = ', '.join(self.op_inputs)
        return f"{self.op}({input_list_str}) -> {self.out_wire}"

    def __repr__(self):
        return str(self)
