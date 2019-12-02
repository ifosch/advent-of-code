#!/usr/bin/env python

filename = 'input.txt'

with open(filename, 'r') as fp:
    line = fp.readline().strip()

items = [int(v) for v in line.split(',')]


def process(v, noun=None, verb=None):
    if noun:
        v[1] = noun

    if verb:
        v[2] = verb

    i = 0
    while i < len(v):
        c = v[i]

        if c == 99:
            break
        elif c == 1:
            v[v[i+3]] = v[v[i+1]] + v[v[i+2]]
            i = i + 4
        elif c == 2:
            v[v[i+3]] = v[v[i+1]] * v[v[i+2]]
            i = i + 4
        else:
            raise

    return v[0]


print(process(items, 12, 2))
