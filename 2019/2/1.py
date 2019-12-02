#!/usr/bin/env python

filename = 'input.txt'

with open(filename, 'r') as fp:
    line = fp.readline().strip()

v = [int(v) for v in line.split(',')]

v[1] = 12
v[2] = 2

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


print("OUY", v[0])