RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = dayX_part1 if part == 1 else dayX_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def dayX_part1(input_):
    pass


def dayX_part2(input_):
    pass


def get_input(file_path):
    with open(file_path) as f:
        input_ = ...

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
