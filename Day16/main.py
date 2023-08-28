import re
from pprint import pprint

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
    present_aunt_dict = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    present_aunt_set = set(present_aunt_dict.items())
    aunts = get_aunts(input_)
    for number, compounds in aunts.items():
        aunt_set = set(compounds.items())
        if aunt_set.issubset(present_aunt_set):
            return number


def get_aunts(input_):
    aunts = {}
    for line in input_:
        # _, number, compounds_str = re.split(r'^Sue (\d)+:', line, maxsplit=1)
        number_match = re.search(r'^Sue (\d+):', line)
        number = number_match.groups()[0]
        compounds_str = line[number_match.end():]
        compounds = re.findall(r'(\w+): (\d+)', compounds_str)
        aunts[int(number)] = {k: int(v) for k, v in compounds}
    return aunts


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
