import re

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    duration = 2503
    reindeer = get_reindeer(input_)
    reindeer_pos = race(reindeer, duration)
    print(reindeer_pos)
    max_dist = max(reindeer_pos.values())
    return max_dist


def get_reindeer(input_):
    reindeer = {}
    for line in input_:
        name = line.split(' ')[0]
        fly_speed, fly_duration = re.search(r'(\d+) km/s for (\d+) seconds', line).groups()
        rest_duration = re.search(r'rest for (\d+) seconds', line).groups()[0]
        reindeer[name] = list(map(int, (fly_speed, fly_duration, rest_duration)))
    return reindeer


def race(reindeer, duration):
    pass


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
