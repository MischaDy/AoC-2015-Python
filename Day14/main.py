import re

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
    duration = 1000 if RUN_TEST else 2503
    reindeer = get_reindeer(input_)
    reindeer_pos = race(reindeer, duration)
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


def race(reindeer_dict, duration):
    reindeer_pos = {}
    for reindeer, (fly_speed, fly_duration, rest_duration) in reindeer_dict.items():
        dist_single = fly_speed * fly_duration
        time = fly_duration + rest_duration
        time_full, time_partial = divmod(duration, time)
        dist_total = time_full * dist_single
        dist_total += fly_speed * min(time_partial, fly_duration)
        reindeer_pos[reindeer] = dist_total
    return reindeer_pos


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
