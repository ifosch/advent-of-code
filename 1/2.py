#!/usr/bin/env python

import fileinput
from pprint import pprint

freq = 0
seen = set()

changes = [int(line.strip()) for line in fileinput.input()]

while True:
    for c in changes:
        if freq in seen:
            pprint(freq)
            break
        
        seen.add(freq)
        
        freq += c

    else:
        continue
    
    break
