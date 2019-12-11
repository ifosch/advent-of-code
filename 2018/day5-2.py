#!/usr/bin/env python

from pprint import pprint
import sys
from string import ascii_lowercase as letters


def equal(a, b):
    return (a != b) and (a.lower() == b.lower())


def main():
    original = list(sys.stdin.read().strip())

    best = len(original)
    for letter in letters:
        discard = {letter, letter.upper()}

        i = 1
        c = original.copy()
        while i < len(c):
            if c[i-1] in discard:
                del(c[i-1])
                continue

            if c[i] in discard:
                del(c[i])
                continue

            if equal(c[i-1], c[i]):
                del(c[i-1])
                del(c[i-1])
                i = max(1, i - 1)
            else:
                i += 1

        best = min(best, len(c))

    print(best)

if __name__ == "__main__":
    main()
