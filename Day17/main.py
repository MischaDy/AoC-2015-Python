from itertools import combinations_with_replacement
from pprint import pprint

from more_itertools import powerset, ilen

RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    pprint(day_function(input_))


def run_part1(input_):
    max_amount = 25 if RUN_TEST else 150
    containers = list(map(int, input_))
    valid_combos = filter(lambda c: sum(c) == max_amount, powerset(containers))
    return ilen(valid_combos)


def run_part2(input_):
    pass


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
