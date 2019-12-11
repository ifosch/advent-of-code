#!/usr/bin/env python

from aocd import data, submit, AocdError
from pprint import pprint


def A():
    s = 0
    for line in data.splitlines():
        i = int(line)
        d = i // 3
        e = d - 2
        s = s + e

    return s


def B():
    s = 0

    for line in data.splitlines():
        i = int(line)
        s = s + fr(i)

    return s


def fr(i):
    a = i // 3
    b = a - 2

    if b > 0:
        b += fr(b)

    if b < 0:
        return 0

    return b


def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
