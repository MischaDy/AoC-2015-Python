from collections import defaultdict


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
    dists = list(get_dists(input_))
    return sum(dists) - max(dists)


def get_dists(lines):
    for line in lines:
        dist_str = line.split(' = ')[-1]
        yield int(dist_str)


def temp(input_):
    locations = get_locations_dict(input_)
    min_dist = float('inf')
    for start in dists.keys():
        dist = tour(locations, start)
        min_dist = min(min_dist, dist)
    return min_dist


def get_locations_dict(lines):
    """
    return a nested dict: {start1 -> {target1 -> dist1, ...}, ...}
    """
    locations = defaultdict(dict)
    for line in lines:
        parts = line.split(' ')
        loc1 = parts[0]
        loc2 = parts[2]
        dist = int(parts[4])
        locations[loc1][loc2] = dist
        locations[loc2][loc1] = dist
    return locations


def tour(locations, start):
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
