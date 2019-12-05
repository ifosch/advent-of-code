#!/usr/bin/env python

filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

items = [int(item) for item in line.split(',')]

def process(v, input):
    outputs = []

    i = 0
    while i < len(v):
        c = v[i]

        if c < 100:
            opcode = c
            modes = list()
        else:
            opcode = c % 100
            modes = [int(a) for a in str(c // 100)[::-1]]

        if opcode == 99:
            break
        elif opcode == 1:
            if len(modes) >= 1 and modes[0]:
                p1 = v[i+1]
            else:
                p1 = v[v[i+1]]

            if len(modes) >= 2 and modes[1]:
                p2 = v[i+2]
            else:
                p2 = v[v[i+2]]

            v[v[i+3]] = p1 + p2
            i = i + 4
        elif opcode == 2:
            if len(modes) >= 1 and modes[0]:
                p1 = v[i+1]
            else:
                p1 = v[v[i+1]]

            if len(modes) >= 2 and modes[1]:
                p2 = v[i+2]
            else:
                p2 = v[v[i+2]]

            v[v[i+3]] = p1 * p2
            i = i + 4
        elif opcode == 3:
            v[v[i+1]] = input
            i = i + 2
        elif opcode == 4:
            if len(modes) >= 1 and modes[0]:
                p1 = v[i+1]
            else:
                p1 = v[v[i+1]]

            outputs.append(p1)
            i = i + 2
        elif opcode == 5:
            if len(modes) >= 1 and modes[0]:
                p1 = v[i+1]
            else:
                p1 = v[v[i+1]]

            if len(modes) >= 2 and modes[1]:
                p2 = v[i+2]
            else:
                p2 = v[v[i+2]]

            if p1:
                i = p2
            else:
                i = i + 3
        elif opcode == 6:
            if len(modes) >= 1 and modes[0]:
                p1 = v[i+1]
            else:
                p1 = v[v[i+1]]

            if len(modes) >= 2 and modes[1]:
                p2 = v[i+2]
            else:
                p2 = v[v[i+2]]

            if not p1:
                i = p2
            else:
                i = i + 3
        elif opcode == 7:
            if len(modes) >= 1 and modes[0]:
                p1 = v[i+1]
            else:
                p1 = v[v[i+1]]

            if len(modes) >= 2 and modes[1]:
                p2 = v[i+2]
            else:
                p2 = v[v[i+2]]
            
            if p1 < p2:
                v[v[i+3]] = 1
            else:
                v[v[i+3]] = 0

            i = i + 4
        elif opcode == 8:
            if len(modes) >= 1 and modes[0]:
                p1 = v[i+1]
            else:
                p1 = v[v[i+1]]

            if len(modes) >= 2 and modes[1]:
                p2 = v[i+2]
            else:
                p2 = v[v[i+2]]
            
            if p1 == p2:
                v[v[i+3]] = 1
            else:
                v[v[i+3]] = 0

            i = i + 4
        else:
            print(c)
            raise

    return outputs


print(process(items, 5))
