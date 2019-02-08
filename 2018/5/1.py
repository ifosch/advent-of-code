#!/usr/bin/env python

from pprint import pprint
import sys


def equal(a, b):
    return (a != b) and (a.lower() == b.lower())


def main():
    c = list(sys.stdin.read().strip())

    i = 1
    while i < len(c):
        if equal(c[i-1], c[i]):
            del(c[i-1])
            del(c[i-1])
            i = max(1, i - 1)
        else:
            i += 1

    print(''.join(c))
    print(len(c))

if __name__ == "__main__":
    main()
