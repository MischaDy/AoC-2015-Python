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
    num_str_chars = 0
    num_mem_chars = 0
    for line in input_:
        num_str_chars += len(line)
        num_mem_chars += count_mem_chars(line)
    return num_str_chars - num_mem_chars


def count_mem_chars(string):
    num_mem_chars = 0
    is_escaping = False
    hex_chars_left = 0
    unquoted_string = string[1:-1]
    for char in unquoted_string:
        if char == '\\':
            # TODO: Check!
            is_escaping = not is_escaping
            if not is_escaping:  # *current* char is not escaped
                num_mem_chars += 1
            continue

        if char == 'x':
            if is_escaping:
                hex_chars_left = 2
            num_mem_chars += 1
        elif hex_chars_left > 0:
            hex_chars_left -= 1
        else:
            num_mem_chars += 1

        is_escaping = False
    return num_mem_chars


def run_part2(input_):
    num_str_chars = 0
    num_code_chars = 0
    for line in input_:
        num_str_chars += len(line)
        num_code_chars += len(encode(line))
    return num_code_chars - num_str_chars
    # nums_mem_chars = []
    # for line in input_:
    #     nums_mem_chars.append(encode(line))
    # return '  ;  '.join(nums_mem_chars)


def encode(string):
    encoded_str = ''
    for char in string:
        if char == '"':
            encoded_str += fr'\{char}'
        elif char == '\\':
            encoded_str += 2 * char
        else:
            encoded_str += char
    return '"' + encoded_str + '"'


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read().split('\n')

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
