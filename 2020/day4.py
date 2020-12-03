#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    valid = 0
    for line in data.splitlines():
        tokens = line.split()

        min_r, max_r = map(int, tokens[0].split('-'))
        ch = tokens[1].rstrip(":")
        pw = tokens[2]

        reps = 0
        for e in pw:
            if e == ch:
                reps += 1

        if reps >= min_r and reps <= max_r:
            valid += 1

    return valid


def B():
    return 0


def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
