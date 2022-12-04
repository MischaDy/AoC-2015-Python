RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = day2_part1 if part == 1 else day2_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def day2_part1(input_):
    total_paper = 0
    for line in input_:
        l, w, h = map(int, line.split('x'))
        min_side_area = l * w * h / max(l, w, h)
        paper_amt = 2 * (l * w + l * h + w * h) + min_side_area
        total_paper += paper_amt
    return int(total_paper)


def day2_part2(input_):
    total_ribbon = 0
    for line in input_:
        l, w, h = map(int, line.split('x'))
        wrap_ribbon = 2 * (l + w + h - max(l, w, h))
        bow_ribbon = l * w * h
        total_ribbon += wrap_ribbon + bow_ribbon
    return int(total_ribbon)


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read().split('\n')

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
