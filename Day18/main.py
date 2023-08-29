from pprint import pprint

import numpy as np
from more_itertools import ilen

RUN_TEST = False
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    pprint(day_function(input_))


def run_part1(input_):
    num_steps = 4 if RUN_TEST else 100
    grid = build_grid(input_)
    if RUN_TEST:
        print_grid(0, grid)
    for iteration in range(1, num_steps+1):
        grid = compute_next_grid(grid)
        if RUN_TEST:
            print_grid(iteration, grid)
    return count_lights_on(grid.flatten())


def build_grid(input_):
    grid_size = len(input_)
    inp_list = [1 if char == '#' else 0
                for row in input_
                for char in row]
    grid = np.array(inp_list, dtype=int).reshape((grid_size, grid_size))
    return grid


def compute_next_grid(old_grid):
    """
    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    """
    new_grid = np.zeros_like(old_grid)
    for row_ind, row in enumerate(old_grid):
        for col_ind, light in enumerate(row):
            neighborhood = get_neighborhood(row_ind, col_ind, old_grid)
            num_neighbors_on = count_lights_on(neighborhood) - light
            if light == 1:
                new_light = 1 if num_neighbors_on in {2, 3} else 0
            else:
                new_light = 1 if num_neighbors_on == 3 else 0
            new_grid[row_ind][col_ind] = new_light
    return new_grid


def count_lights_on(neighbors):
    return ilen(filter(lambda n: n == 1, neighbors))


def get_neighborhood(row_ind, col_ind, grid):
    row_ind_min, col_ind_min = max(row_ind-1, 0), max(col_ind-1, 0)
    max_ind = len(grid) - 1
    row_ind_max, col_ind_max = min(row_ind+1, max_ind), min(col_ind+1, max_ind)
    neighborhood = grid[row_ind_min:row_ind_max+1, col_ind_min:col_ind_max+1]
    return neighborhood.flatten()


def print_grid(iteration, grid):
    row_strs = map(lambda r: ''.join(map(str, r)),
                   grid)
    grid_str = '\n'.join(row_strs)
    grid_str_canon = grid_str.replace('1', '#').replace('0', '.')
    print(f'=== {iteration} ===')
    print(grid_str_canon, end=2*'\n')


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
