#!/usr/bin/env python

filename = 'input.txt'

with open(filename, 'r') as fp:
    lines = (l.strip() for l in fp)

    s = 0

    for line in lines:
        i = int(line)
        d = i // 3
        e = d - 2
        s = s + e


print(s)
