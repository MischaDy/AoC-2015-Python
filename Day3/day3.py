RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = day3_part1 if part == 1 else day3_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def day3_part1(input_):
    dir_to_delta = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    pos = [0, 0]
    houses = {str(pos)}
    for direction in input_:
        delta_x, delta_y = dir_to_delta[direction]
        pos[0] += delta_x
        pos[1] += delta_y
        houses.add(str(pos))
    return len(houses)


def day3_part2(input_):
    dir_to_delta = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    positions = ([0, 0], [0, 0])
    houses = {str(positions[0])}
    for ind, direction in enumerate(input_):
        pos = positions[ind % 2]
        delta_x, delta_y = dir_to_delta[direction]
        pos[0] += delta_x
        pos[1] += delta_y
        houses.add(str(pos))
    return len(houses)


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read()  # .split('\n')

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
