#!/usr/bin/env python
import argparse
from collections import namedtuple

Ingredient = namedtuple("Ingredient", ["name", "amount", "units"])

MASTER_RECIPE = [
    Ingredient("Water", 101.66, "g"),
    Ingredient("Fresh Yeast", 0.5, "g"),
    Ingredient("Dry Yeast", 0.2, "g"),
    Ingredient("Olive Oil", 3.33, "ml"),
    Ingredient("00 Flour", 166.66, "g"),
    Ingredient("Sea Salt", 4, "g"),
]


def scale_recipe(multiplier: int, fresh: bool=False):
    if fresh:
        base = filter(lambda x: x.name != "Dry Yeast", MASTER_RECIPE)
    else:
        base = filter(lambda x: x.name != "Fresh Yeast", MASTER_RECIPE)

    scaled = [
        Ingredient(x.name, round(x.amount * multiplier, 2), x.units)
        for x in base]

    return scaled


def format_recipe(recipe, multiplier: int) -> str:
    t = f"INGREDIENTS FOR {multiplier} DOUGH BALL{'S' if multiplier != 1 else ''}\n"
    t += "-" * (len(t) - 1) + "\n"
    s = "\n".join(
        [f"{x.name:<8}\t{x.amount:>7,.1f} {x.units:<3}" for x in recipe])

    return t + s + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("multiplier", type=int, default=1)
    parser.add_argument("-f", "--fresh-yeast", action="store_true")
    args = parser.parse_args()

    scaled = scale_recipe(args.multiplier, args.fresh_yeast)
    print(format_recipe(scaled, args.multiplier))


if __name__ == '__main__':
    main()
