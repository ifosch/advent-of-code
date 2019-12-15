#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")

from itertools import combinations


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def lcm(a, b):
    return a * b // gcd(a,b)


class MoonSystem(object):
    def __init__(self, moons):
        self.moons = moons
        self.velocities = {}
        self.seen = {}
        self.rep = {}
        for i in range(3):
            self.seen[i] = {}

        for i in range(len(self.moons)):
            self.velocities[i] = [0, 0, 0]

    def run(self, limit=-1):
        i = 0
        while i != limit and len(self.rep) < 3:
            print("Step {}: {}, velocities: {}".format(
                i, self.moons, self.velocities))

            for c in range(3):
                if c not in self.rep:
                    pos = tuple(m[c] for m in self.moons)
                    vel = tuple(self.velocities[v][c] for v in self.velocities)
                    t = pos + vel
                    if t in self.seen[c]:
                        print(self.seen[c])
                        print(t, 'seen in', i, 'and seen in', self.seen[c][t])
                        self.rep[c] = i - self.seen[c][t]
                        break

                    self.seen[c][t] = i

                for a, b in self.moonpairs():
                    if self.moons[a][c] > self.moons[b][c]:
                        self.velocities[a][c] -= 1
                        self.velocities[b][c] += 1
                    elif self.moons[a][c] < self.moons[b][c]:
                        self.velocities[a][c] += 1
                        self.velocities[b][c] -= 1

                for m in range(len(self.moons)):
                    self.moons[m][c] += self.velocities[m][c]

            i += 1

        print("Step {}: {}, velocities: {}".format(
            i, self.moons, self.velocities))
        print(lcm(lcm(self.rep[0], self.rep[1]), self.rep[2]))

    def moonpairs(self):
        return combinations(range(len(self.moons)), 2)

    def get_energy(self):
        total = 0
        for k, moon in enumerate(self.moons):
            pot = sum([abs(i) for i in moon])
            kin = sum([abs(i) for i in self.velocities[k]])

            total += pot*kin

        return total

    def repeated(self):
        if len(self.rep) < 3:
            return False
        else:
            return self.rep


def A():
    return None
    data = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

    moons = []
    for line in data.splitlines():
        moons.append(
            [int(t.split('=')[1].split('>')[0]) for t in line.split(',')]
            )

    ms = MoonSystem(moons)
    ms.run(10)
    energy = ms.get_energy()

    return energy


def B():
    data = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

    moons = []
    for line in data.splitlines():
        moons.append(
            [int(t.split('=')[1].split('>')[0]) for t in line.split(',')]
            )

    ms = MoonSystem(moons)
    ms.run()


def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
