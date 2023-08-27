import re
from collections import defaultdict
from itertools import permutations, pairwise

RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    people_changes = build_people_changes_dict(input_)
    arrangements = permutations(people_changes.keys())
    changes = map(lambda a: compute_change(a, people_changes), arrangements)
    return max(changes)


def build_people_changes_dict(input_):
    people_changes = defaultdict(dict)
    for line in input_:
        words = line.rstrip('.').split(' ')
        person1, person2 = words[0], words[-1]
        sign = +1 if 'gain' in words else -1
        units = re.search(r'(\d+) happiness units', line).groups()[0]
        signed_units = sign * int(units)
        people_changes[person1][person2] = signed_units
    return people_changes


def compute_change(arrangement, people_changes):
    change = 0
    pairs = pairwise([*arrangement, arrangement[0]])
    for person1, person2 in pairs:
        change += people_changes[person1][person2]
        change += people_changes[person2][person1]
    return change


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
