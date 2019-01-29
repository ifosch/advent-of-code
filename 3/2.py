#!/usr/bin/env python

import fileinput
from pprint import pprint
w, h = 1000, 1000
M = [[set() for x in range(w)] for y in range(h)] 

non_overlapping = set()

def input():
    for l in fileinput.input():
        if not l:
            continue
        yield l.strip()

def items():
    for v in input():
        id_tmp, d = v.split("@")
        id = int(id_tmp.split("#")[1].strip())
        d = [a.strip() for a in d.split(':')]

        posx, posy = [int(a) for a in d[0].split(',')]
        sizex, sizey = [int(a) for a in d[1].split('x')]

        yield (id, posx, posy, sizex, sizey)

def main():
    for i in items():
        id, posx, posy, sizex, sizey = i

        overlaps = False
        for y in range(posy, posy + sizey):
            for x in range(posx, posx + sizex):
                if M[x][y]:
                    overlaps = True
                for a in M[x][y]:
                    if a in non_overlapping:
                        non_overlapping.remove(a)

                M[x][y].add(id)
        
        if not overlaps:
            non_overlapping.add(id)
    
    print(non_overlapping)

if __name__ == "__main__":
    main()