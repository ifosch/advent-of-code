#!/usr/bin/env python

filename = 'input.txt'


def fr(i):
    a = i // 3
    b = a - 2

    if b > 0:
        b += fr(b)

    if b < 0:
        return 0

    return b


with open(filename, 'r') as fp:
    lines = (l.strip() for l in fp)

    s = 0

    for line in lines:
        i = int(line)

        s = s + fr(i)

print(s)
