from hashlib import md5

RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def run_part1(input_):
    num_zeros = 5
    k = 1
    digest = get_md5(input_ + str(k))
    while not digest.startswith(num_zeros * '0'):
        k += 1
        digest = get_md5(input_ + str(k))
    return k


def get_md5(string):
    input_bytes = bytes(string, encoding='utf-8')
    return md5(input_bytes).hexdigest()


def run_part2(input_):
    num_zeros = 6
    k = 1
    digest = get_md5(input_ + str(k))
    zeros = num_zeros * '0'
    while not digest.startswith(zeros):
        k += 1
        digest = get_md5(input_ + str(k))
    return k


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read()

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
