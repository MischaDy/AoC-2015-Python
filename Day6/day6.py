RUN_TEST = False
PART = 2

TEST_INPUT_PATH = 'test_input2.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path)
    print(day_function(input_))


def run_part1(input_):
    n = 1000
    lights = [n * [False] for _ in range(n)]
    # show(lights)
    for instr in input_:
        set_lights(lights, *parse_instr1(instr))
        # show(lights)

    return sum(map(sum, lights))


def set_lights(lights, val_func, start, end):
    start_col, start_row = start
    end_col, end_row = end
    light_rows = lights[start_row:end_row+1]
    for light_row in light_rows:
        light_row[start_col:end_col+1] = list(map(val_func, light_row[start_col:end_col+1]))


def parse_instr1(instr):
    if instr.startswith('turn on'):
        def val_func(val):
            return True

        cutoff = len('turn on ')
    elif instr.startswith('turn off'):
        def val_func(val):
            return False

        cutoff = len('turn off ')
    else:
        def val_func(val):
            return not val

        cutoff = len('toggle ')
    points_strs = instr[cutoff:].split(' through ')
    start, end = map(point_str_to_tuple, points_strs)
    return val_func, start, end


def parse_instr2(instr):
    if instr.startswith('turn on'):
        def val_func(val):
            return val + 1

        cutoff = len('turn on ')
    elif instr.startswith('turn off'):
        def val_func(val):
            return max(0, val - 1)

        cutoff = len('turn off ')
    else:
        def val_func(val):
            return val + 2

        cutoff = len('toggle ')
    points_strs = instr[cutoff:].split(' through ')
    start, end = map(point_str_to_tuple, points_strs)
    return val_func, start, end


def point_str_to_tuple(point_str):
    return tuple(map(int, point_str.split(',')))


def show(lights):
    str_lights = [[str(int(light)) for light in light_row]
                  for light_row in lights]
    print('\n'.join(map('  '.join, str_lights)), '\n')


def run_part2(input_):
    n = 1000
    lights = [n * [0] for _ in range(n)]
    # show(lights)
    for instr in input_:
        set_lights(lights, *parse_instr2(instr))
        # show(lights)

    return sum(map(sum, lights))


def get_input(file_path):
    with open(file_path) as f:
        input_ = f.read().split('\n')

    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
