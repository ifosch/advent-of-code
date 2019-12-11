#!/usr/bin/env python

parent = {}
children = {}

filename = 'input.txt'
with open(filename, 'r') as fp:
    lines = (l.strip() for l in fp)

    for line in lines:
        a, b = line.split(')')
        print(a,b)

        parent[b] = a
        if a not in children:
            children[a] = []
        children[a].append(b)

tot_count = 0

def traverse(cur, depth):
    global tot_count
    tot_count += depth
    if cur in children:
        for c in children[cur]:
            traverse(c, depth+1)

traverse('COM', 0)


#prog = intcode.Program(data)
print(tot_count)

def chain(cur, l):
    l.append(cur)
    if cur in parent:
        chain(parent[cur], l)

yc=[]
sc=[]
chain('YOU', yc)
chain('SAN', sc)

dist={}
c=0
for y in yc:
    dist[y] = c
    c += 1

c = 0
for s in sc:
    if s in dist:
        print(dist[s] + c - 2)
        exit()
    c += 1