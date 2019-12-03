#!/usr/bin/env python

# Open Single Line File and iterate char by char
filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

items = [int(char) for char in line]

first = items[0]
brk = False
total = 0
i = 0
while True:
    try:
        nxt = items[i+1]
    except Exception:
        brk = True
        nxt = first

    if items[i] == nxt:
        total += items[i]

    if brk:
        break

    i = i + 1

print(total)
