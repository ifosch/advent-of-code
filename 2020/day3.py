#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    valid = 0
    rows = []
    for line in data.splitlines():
        row = []
        for c in line:
            row.append((c == '#'))
        rows.append(row)
    
    x = 0
    trees = 0
    
    return(trees)


def B():
    valid = 0
    rows = []
    for line in data.splitlines():
        row = []
        for c in line:
            row.append((c == '#'))
        rows.append(row)
    
    total = 1

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    for dx, dy in slopes:
        x, y = 0, 0
        trees = 0
        print(dx, dy)

        while y < len(rows):
            row = rows[y]
            l = len(row)
            x = x % l
            if(row[x]):
                trees += 1

            x += dx
            y += dy

        total *= trees

    return total




    return(total)

def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
