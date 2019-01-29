#!/usr/bin/env python

import fileinput
from pprint import pprint

acc = 0

for line in fileinput.input():
    acc += int(line.strip())

pprint(acc)