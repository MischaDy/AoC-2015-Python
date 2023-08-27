import json
import re

RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt' if PART == 1 else 'test_input2.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(*map(day_function, input_))


def run_part1(input_):
    matches = re.finditer(r'(-?\d+)', input_)
    num_strs = (m[0] for m in matches)
    nums = map(int, num_strs)
    return sum(nums)


def sum_no_red(data):
    if isinstance(data, int):
        return data
    if isinstance(data, str):
        return 0
    if isinstance(data, list):
        return sum(map(sum_no_red, data))
    if isinstance(data, dict):
        if 'red' in data.values():
            return 0
        return sum_no_red(list(data.keys())) + sum_no_red(list(data.values()))


def run_part2(input_):
    data = json.loads(input_)
    return sum_no_red(data)


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
