from string import ascii_lowercase as CHARS
from more_itertools import windowed


RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'

STRAIGHTS = list(map(''.join, windowed(CHARS, 3)))


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    print(day_function(input_))


def run_part1(input_):
    pass


def run_part2(input_):
    pass


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


def next_valid_password(password):
    while not is_valid(password):
        password = increment(password)
    return password


def is_valid(password):
    return not has_illegal_char(password) and has_straight(password) and has_char_pairs(password)


def increment(password):
    next_int = int(password, base=26) + 1



def has_illegal_char(password):
    for char in 'iol':
        if char in password:
            return True
    return False


def has_straight(password):
    for straight in STRAIGHTS:
        if straight in password:
            return True
    return False


def has_char_pairs(password):
    ind = find_char_pair(password)
    if ind == -1:
        return False
    pw_slice = password[ind+2:]
    return find_char_pair(pw_slice) != ind


def find_char_pair(password):
    for char in CHARS:
        pair = 2 * char
        ind = password.find(pair)
        if ind != -1:
            break
    return ind


def test():
    assert not is_valid('hijklmmn')
    assert not is_valid('abbceffg')
    assert not is_valid('abbcegjk')

    assert next_valid_password('abbcegjk') == 'abcdffaa'
    assert next_valid_password('ghijklmn') == 'ghjaabcc'


if __name__ == '__main__':
    if RUN_TEST:
        test()
    else:
        main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
