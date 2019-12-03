#!/usr/bin/env python
# Open Single Line File and iterate (split by comma)

filename = 'input.txt'
with open(filename, 'r') as fp:
    line1 = fp.readline().strip()
    line2 = fp.readline().strip()

items1 = [item for item in line1.split(',')]
items2 = [item for item in line2.split(',')]

x = 0
y = 0
visited1 = set()
sv1 = {}
steps = 0
for i1 in items1:
    d = i1[0]
    n = int(i1[1:])
    if d == 'R':
        for a in range(1, n+1):
            x = x + 1
            steps += 1
            if (x, y) not in visited1:
                sv1[(x, y)] = steps
            visited1.add((x, y))
    elif d == 'U':
        for a in range(1, n+1):
            y = y - 1
            steps += 1
            if (x, y) not in visited1:
                sv1[(x, y)] = steps
            visited1.add((x, y))
    elif d == 'D':
        for a in range(1, n+1):
            y = y + 1
            steps += 1
            if (x, y) not in visited1:
                sv1[(x, y)] = steps
            visited1.add((x, y))
    elif d == 'L':
        for a in range(1, n+1):
            x = x - 1
            steps += 1
            if (x, y) not in visited1:
                sv1[(x, y)] = steps
            visited1.add((x, y))
    else:
        raise

x = 0
y = 0
visited2 = set()
sv2 = {}
steps = 0
for i2 in items2:
    d = i2[0]
    n = int(i2[1:])
    if d == 'R':
        for a in range(1, n+1):
            x = x + 1
            steps += 1
            if (x, y) not in visited2:
                sv2[(x, y)] = steps
            visited2.add((x, y))
    elif d == 'U':
        for a in range(1, n+1):
            y = y - 1
            steps += 1
            if (x, y) not in visited2:
                sv2[(x, y)] = steps
            visited2.add((x, y))
    elif d == 'D':
        for a in range(1, n+1):
            y = y + 1
            steps += 1
            if (x, y) not in visited2:
                sv2[(x, y)] = steps
            visited2.add((x, y))
    elif d == 'L':
        for a in range(1, n+1):
            x = x - 1
            steps += 1
            if (x, y) not in visited2:
                sv2[(x, y)] = steps
            visited2.add((x, y))
    else:
        raise

both = visited1 & visited2

ds = []
for point in both:
    comb = sv1[point] + sv2[point]
    ds.append(comb)

print(min(ds))
