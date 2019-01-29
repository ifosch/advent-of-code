#!/usr/bin/env python

import fileinput
from pprint import pprint
import itertools

def distance(e1, e2):
    d = 0
    for a, b in zip(e1, e2):
        if a != b:
            d += 1

    return d

def common_chars(e1, e2):
    out = ""
    for a, b in zip(e1, e2):
        if a == b:
            out += a
    
    return out

elems = [v.strip() for v in fileinput.input()]
print(len(elems))

pairs = list(itertools.combinations(elems, 2))

shortest = None
shortest_pair = None
for p in pairs:
    d = distance(*p)

    if not shortest or d < shortest:
        shortest = d
        shortest_pair = p

print(shortest, shortest_pair, common_chars(*shortest_pair))
