#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    pairs = set()
    x, y = 0, 0

    for c in data:
        pairs.add((x, y,))
        if c == '>':
            x += 1
        elif c == '<':
            x -= 1
        elif c == '^':
            y -= 1
        elif c == 'v':
            y += 1
        else:
            raise Exception

    return len(pairs)


def B():
    pairs = set()

    pos = [[0, 0], [0, 0]]
    pairs.add((0, 0, ))

    for i, c in enumerate(data):
        if c == '>':
            pos[i % 2][0] += 1
        elif c == '<':
            pos[i % 2][0] -= 1
        elif c == '^':
            pos[i % 2][1] -= 1
        elif c == 'v':
            pos[i % 2][1] += 1
        else:
            raise Exception

        pairs.add(tuple(pos[i % 2]))

    return len(pairs)


    return 0
    s = 0
    p = 0
    for c in data:
        p += 1
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1

        if s < 0:
            return p

def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
