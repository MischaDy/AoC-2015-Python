import re
from collections import defaultdict
from pprint import pprint

from numpy import product

RUN_TEST = True
PART = 1

TEST_INPUT_PATH = 'test_input.txt'
INPUT_PATH = 'input.txt'


def main(run_test, part, test_input_path, input_path):
    file_path = test_input_path if run_test else input_path
    day_function = run_part1 if part == 1 else run_part2
    input_ = get_input(file_path, line_sep='\n')
    pprint(day_function(input_))


def run_part1(input_):
    teaspoons = 100
    ingredients = get_ingredients(input_)
    distr = find_optimal_distribution(ingredients, teaspoons)
    score = compute_score(distr, ingredients)
    return score


def find_optimal_distribution(ingredients, teaspoons):
    # seed(0)
    amount1 = 44  # randint(0, 100)
    amount2 = teaspoons - amount1
    return {ing: amount for ing, amount in zip(ingredients, [amount1, amount2])}


def get_ingredients(input_):
    ingredients = {}
    for line in input_:
        ingredient = line.split(':')[0]
        matches = (re.finditer(r'(\w+) (-?\d+)', line))
        ing_dict = {}
        for match in matches:
            property, value = match.groups()
            ing_dict[property] = int(value)
        ingredients[ingredient] = ing_dict
    return ingredients


def compute_score(distribution, ingredients):
    property_scores = defaultdict(lambda: 0)
    for ing, amount in distribution.items():
        for property, value in ingredients[ing].items():
            if property == 'calories':
                continue
            property_scores[property] += amount * value
    return product(list(property_scores.values()))


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
