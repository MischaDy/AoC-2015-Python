RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = day1_part1 if part == 1 else day1_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def day1_part1(input_):
    return input_.count('(') - input_.count(')')


def day1_part2(input_):
    level = 0
    for ind, char in enumerate(input_, start=1):
        if char == '(':
            level += 1
        else:
            level -= 1
        if level < 0:
            return ind


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read()  # .split('\n')

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
