#!/usr/bin/env python

filename = 'input.txt'

with open(filename, 'r') as fp:
    lines = (l.strip() for l in fp)

    for line in lines:
        i = int(line)

        print(line, i)
