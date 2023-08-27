from itertools import dropwhile, pairwise
from string import ascii_lowercase as chars

from more_itertools import windowed, first, last, always_reversible

from Day11.helpers import generate_next_char_map

RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'

CHARS = chars
STRAIGHTS = set(windowed(CHARS, 3))
ILLEGAL_CHARS = 'iol'
NEXT_CHAR_MAP = generate_next_char_map(CHARS, ILLEGAL_CHARS)


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep=None)
    print(day_function(input_))


def run_part1(input_):
    password = list(input_)
    next_password = next_valid_password(password)
    return ''.join(next_password)


def run_part2(input_):
    password1 = run_part1(input_)
    init_password2 = increment(list(password1))
    password2 = run_part1(init_password2)
    return password2


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


def next_valid_password(password: list[str]):
    if is_valid(password):
        return password

    # handle the case where the intial password contains illegal chars
    password = next_password_legal_chars_only(password)
    while not is_valid(password):
        password = increment(password)
    return password


def next_password_legal_chars_only(password):
    next_password = []
    for ind, char in enumerate(password):
        # todo: handle edge case of a/z being illegal char
        if char in ILLEGAL_CHARS:
            break
        next_password.append(char)
    else:
        return increment(next_password)

    next_char = NEXT_CHAR_MAP[char]
    next_password.append(next_char)
    next_password += ['a'] * (len(password) - ind - 1)
    return next_password


def is_valid(password: list[str]):
    return not has_illegal_char(password) and has_straight(password) and has_char_pairs(password)


def increment(password: list[str]):
    # next_int = int(password, base=26) + 1
    first_non_z_inds = list(map(first, dropwhile(lambda p: last(p) == CHARS[-1],
                                                 always_reversible(enumerate(password)))))
    if not first_non_z_inds:
        return CHARS[0] * (len(password) + 1)
    first_non_z_ind = first_non_z_inds[0]
    next_char = NEXT_CHAR_MAP[password[first_non_z_ind]]
    postfix = ['a'] * (len(password) - first_non_z_ind - 1)
    next_password = password[:first_non_z_ind] + [next_char] + postfix
    return next_password


def has_illegal_char(password):
    for char in ILLEGAL_CHARS:
        if char in password:
            return True
    return False


def has_straight(password):
    for window in windowed(password, 3):
        if window in STRAIGHTS:
            return True
    return False


def has_char_pairs(password: list[str]):
    ind = find_char_pair_ind(password)
    if ind is None:
        return False
    password_rest = password[ind+2:]
    return find_char_pair_ind(password_rest) is not None


def find_char_pair_ind(password: list[str]):
    # pairs = dropwhile(lambda p: p[0] == p[1], pairwise(password))
    # ind = first(pairs)[0]
    # return ind
    for ind, (c1, c2) in enumerate(pairwise(password)):
        if c1 == c2:
            return ind


def test():
    assert not is_valid(list('hijklmmn'))
    assert not is_valid(list('abbceffg'))
    assert not is_valid(list('abbcegjk'))

    assert next_valid_password(list('abcdefgh')) == list('abcdffaa')
    assert next_valid_password(list('ghijklmn')) == list('ghjaabcc')


if __name__ == '__main__':
    if RUN_TEST:
        test()
    else:
        main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
