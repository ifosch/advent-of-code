#!/usr/bin/env python

# Open Single Line File and iterate char by char
filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

a , b = [i for i in line.split('-')]

i = int(a) + 1
total = 0
while i <= int(b):
    chars = str(i)
    if len(chars) == len(set(chars)):
        i += 1
        continue

    if not(list(chars) == sorted(chars)):
        i += 1
        continue

    total += 1
    i += 1

print(total)