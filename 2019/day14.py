#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")

amounts = {}


def get_ore(i, r):
    ore = 0
    q, p = i
    print("Need to make {} {}".format(q, p))
    qs = sorted([a for a in r[p]])
    qt = q
    while qt > 0:
        if q in qs:
            c = q
        else:
            qs2 = list(filter(lambda x: x < q, qs))
            if not qs2:
                c = min(qs)
            else:
                c = max(qs2)
        for a, b in r[p][c]:
            if a == 'ORE':
                print(b)
                ore += b
            else:
                ore += get_ore((b, a), r)
        qt -= c

    return ore


def A():
    data = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

    prod_used = {}

    reactions = {}

    for r in data.splitlines():
        ingredients, product = r.split(' => ')
        prod_amount, prod_type = product.split(' ')
        prod_amount = int(prod_amount)

        if prod_type not in amounts:
            amounts[prod_type] = 0

        reactions[prod_type] = {}
        reactions[prod_type][prod_amount] = []

        for ing in ingredients.split(', '):
            ing_amount, ing_type = ing.split(' ')
            ing_amount = int(ing_amount)

            reactions[prod_type][prod_amount].append((ing_type, ing_amount))

    return get_ore((1, 'FUEL'), reactions)

def B():
    pass


def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
