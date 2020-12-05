#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    s = 0
    for c in data:
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1

    return s


def B():
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
