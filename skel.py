#!/usr/bin/env python

filename = 'input.txt'

# Open Multiline File and iterate line by line
filename = 'input.txt'
with open(filename, 'r') as fp:
    lines = (l.strip() for l in fp)

    for line in lines:
        i = int(line)
        print(line, i)


# Open Single Line File and iterate char by char
filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

for char in line:
    print(char)

chars = [char for char in line]

# Open Single Line File and iterate (split by comma)
filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

for item in line.split(','):
    print(item)

items = [item for item in line.split(',')]
items_num = [int(item) for item in line.split(',')]
