#!/usr/bin/env python

from collections import Counter
# Open Single Line File and iterate char by char
filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

a , b = [i for i in line.split('-')]

i = int(a) + 1
total = 0
while i <= int(b):
    chars = str(i)

    if not(list(chars) == sorted(chars)):
        i += 1
        continue

    if len(chars) == len(set(chars)):
        i += 1
        continue

    if len(chars) != len(set(chars)):
        found = False
        for c in set(chars):
            if c*2 in chars:
                if c*3 not in chars:
                    found = True
        
        if not found:
            i += 1
            continue
            


    total += 1
    i += 1

print(total)