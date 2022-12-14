from Day7.circuit import Circuit
from Day7.instruction import Instruction

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'

# TODO: Bug! Gate provides no signal until all its inputs have signals.
#       --> diff approach needed!


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def run_part1(input_):
    instrs = get_instrs(input_)
    circuit = Circuit(instrs)
    circuit.run()
    return circuit


def get_instrs(lines):
    instrs = list(map(Instruction.from_line, lines))
    return instrs


def run_part2(input_):
    pass


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read().split('\n')

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
