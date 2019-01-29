#!/usr/bin/env python

import fileinput
from pprint import pprint
w, h = 1000, 1000
M = [[0 for x in range(w)] for y in range(h)] 

def input():
    for l in fileinput.input():
        if not l:
            continue
        yield l.strip()

def items():
    for v in input():
        id_tmp, d = v.split("@")
        id = id_tmp.split("#")[1].strip()
        d = [a.strip() for a in d.split(':')]

        posx, posy = [int(a) for a in d[0].split(',')]
        sizex, sizey = [int(a) for a in d[1].split('x')]

        yield (posx, posy, sizex, sizey)

def main():
    for i in items():
        posx, posy, sizex, sizey = i

        for y in range(posy, posy + sizey):
            for x in range(posx, posx + sizex):
                M[x][y] += 1
    

    ov = 0
    for x in range(w):
        for y in range(h):
            v = M[x][y]
            if v > 1:
                ov += 1
    
    print(ov)

if __name__ == "__main__":
    main()