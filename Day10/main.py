RUN_TEST = 0
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def do_look_and_say(line, iterations):
    cur_seq = list(line)
    for i in range(iterations):
        cur_seq = get_next_seq(cur_seq)
        # print_state(cur_seq, i)
    return cur_seq


def run_part1(input_):
    iterations = 5 if RUN_TEST else 40
    seq = list(input_)
    final_seq = do_look_and_say(seq, iterations)
    return len(final_seq)


def get_next_seq(seq):
    next_seq = []
    char_old = seq[0]
    char_count = 1
    for char_new in seq[1:]:
        if char_new != char_old:
            next_seq += [str(char_count), char_old]
            char_old = char_new
            char_count = 1
        else:
            char_count += 1
    next_seq += [str(char_count), char_old]
    return next_seq


def print_state(seq, i=None):
    seq_str = ''.join(seq)
    if RUN_TEST:
        if i is None:
            print(seq_str)
        else:
            print(i, seq_str)
    else:
        print(i)


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
