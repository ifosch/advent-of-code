#!/usr/bin/env python

import fileinput
from pprint import pprint
from collections import Counter

twos, threes = 0, 0
for line in fileinput.input():
    c = Counter(line.strip())
    v_counter = Counter([v for k, v in c.items()])
    twos += int(v_counter[2] >= 1)
    threes += int(v_counter[3] >= 1)

print(twos * threes)