#!/usr/bin/env python

map = """
.#..#
.....
#####
....#
...##
"""

asteroids = set()
y = 0
for line in map.split():
    x = 0
    for char in line:
        if char == '#':
            asteroids.add((x,y))
        x += 1
    y += 1

from math import sqrt

def is_between(a,c,b):
    x1, y1 = a
    x2, y2 = b
    x, y = c

    if not(x1 <= x <= x2 or x1 >= x >= x2) and not(y1 <= y <= y2 or y1 >= y >= y2):
        return False

    return True


def direct_sight(asteroids, x, y):
    print('checking asteroids in direct sight from {}'.format((x,y)))
    if (x, y) not in asteroids:
        return False

    found = -1
    for x1, y1 in asteroids:
        if x1 == x and y1 == y:
            continue

        print('checking asteroids between {} and {}'.format((x,y),(x1,y1)))
        dx1 = x1 - x
        dy1 = y1 - y

        obstacle = False
        for x2, y2 in asteroids:
            if x2 == x and y2 == y:
                break

            if x2 == x1 and y2 == y1:
                break

            dx2 = x2 - x
            dy2 = y2 - y

            cross = dx1 * dy2 - dx2 * dy1
            if not cross:
                print("Found", x2, y2)
                obstacle = True
                break

        if obstacle:
            continue

        found += 1
    
    return found

print(direct_sight(asteroids, 1, 2))
m = 0
for x, y in asteroids:
    c = 0
    #c = direct_sight(asteroids, x, y)
    #print(x, y, c)
    if c > m:
        m = c

#print(m)