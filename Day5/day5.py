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
    VOWELS = set('aeiou')
    BAD_SUBS = {'ab', 'cd', 'pq', 'xy'}

    def is_nice(string):
        num_distinct_vowels = int(string[0] in VOWELS)
        has_double_char = False
        for char1, char2 in zip(string[:-1], string[1:]):
            if char1 + char2 in BAD_SUBS:
                return False
            if char1 == char2:
                has_double_char = True
            if char2 in VOWELS:
                num_distinct_vowels += 1
        return has_double_char and num_distinct_vowels >= 3

    return sum(map(is_nice, input_))


def run_part2(input_):
    def is_nice(string):
        # check if has repeat letter
        has_repeat_letter = False
        for i, char in enumerate(string[:-2]):
            char_skip_1 = string[i + 2]
            if char == char_skip_1:
                has_repeat_letter = True
        if not has_repeat_letter:
            return False

        # check if has double pair
        for i, (char1, char2) in enumerate(zip(string[:-3], string[1:-1])):
            pair = char1 + char2
            if pair in string[i+2:]:
                return True
        return False

    return sum(map(is_nice, input_))


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read().split('\n')

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
