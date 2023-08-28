import re
from collections import defaultdict
from pprint import pprint

from numpy import product

RUN_TEST = False
PART = 2

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
    distr, opt_score = find_optimal_distribution(ingredients, teaspoons)
    return distr, opt_score


def find_optimal_distribution(ingredients, teaspoons):
    scores = ((distr, compute_score(distr, ingredients))
              for distr in gen_distributions(len(ingredients.keys()), teaspoons))
    return max(scores, key=lambda t: t[1])


def gen_distributions(k, total):
    """
    generate all possible distributions of an integer total over k items/positions

    order not guaranteed
    examples:
        (2, 4) ==> [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]
        (3, 5) ==> [(5, 0, 0),
                    (4, 1, 0), (4, 0, 1),
                    (3, 2, 0), (3, 1, 1), (3, 0, 2),
                    (2, 3, 0), (2, 2, 1), (2, 1, 2), (2, 0, 3),
                    (1, 4, 0), (1, 3, 1), (1, 2, 2), (1, 1, 3), (1, 0, 4),
                    (0, 5, 0), (0, 4, 1), (0, 3, 2), (0, 2, 3), (0, 1, 4), (0, 0, 5)]


    :param k: number of items to distribute amount over
    :param total: amount to distribute over k items
    :return:
    """
    if k == 1:
        yield [total]
    else:
        for amount in reversed(range(0, total+1)):
            for sub_distr in gen_distributions(k-1, total-amount):
                yield [amount] + sub_distr


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
    for ing, amount in zip(ingredients.keys(), distribution):
        for property, value in ingredients[ing].items():
            if property == 'calories':
                continue
            property_scores[property] += amount * value
    if any(map(lambda v: v <= 0, property_scores.values())):
        return 0
    return product(list(property_scores.values()))


def run_part2(input_):
    teaspoons = 100
    ingredients = get_ingredients(input_)
    distr, opt_score = find_optimal_distribution_part2(ingredients, teaspoons)
    return distr, opt_score


def compute_calories(distribution, ingredients):
    calories = sum(
        amount * ing['calories']
        for ing, amount in zip(ingredients.values(), distribution)
    )
    return calories


def find_optimal_distribution_part2(ingredients, teaspoons):
    scores = ((distr, compute_score(distr, ingredients))
              for distr in gen_distributions(len(ingredients.keys()), teaspoons)
              if compute_calories(distr, ingredients) == 500)
    return max(scores, key=lambda t: t[1])


def get_input(file_path, line_sep=None):
    with open(file_path) as f:
        input_ = f.read()

    if line_sep is not None:
        input_ = input_.split(line_sep)
    return input_


if __name__ == '__main__':
    main(RUN_TEST, PART, TEST_INPUT_PATH, INPUT_PATH)
