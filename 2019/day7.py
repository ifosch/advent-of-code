#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")

from queue import Queue, Empty


class Intcode(object):
    def __init__(self, program, input=None):
        self.mem = program

        self.input = Queue()
        self.output = Queue()

        self.exit = False
        self.blocked = False

        self.ip = 0  # Instruction Pointer
        self.override_ip = None

    def add_input(self, val):
        self.input.put(val)
        self.blocked = False

    def get_input(self):
        try:
            return self.input.get(block=False)
        except Empty:
            return None

    def get_output(self):
        try:
            return self.output.get(block=False)
        except Empty:
            return None

    def step(self):
        curr = self.read(self.ip)

        opcode = curr % 100
        modes = curr // 100

        instr_name, operation, num_params, ret_param = self.opcodes[opcode]

        params = []
        for i in range(num_params):
            val = self.read(self.ip + i + 1)
            if i != ret_param:
                if modes % 10 == 0:
                    val = self.read(val)

            modes = modes // 10
            params.append(val)

        #print(instr_name, modes, num_params, params)

        operation(self, *params)

        if any((self.exit, self.blocked)):
            return False

        if self.override_ip:
            self.ip = self.override_ip
            self.override_ip = None
        else:
            self.ip += 1 + num_params

        return True

    def run(self):
        while not any((self.exit, self.blocked)) and self.step():
            pass

    def set_nounverb(self, noun, verb):
        self.write(1, noun)
        self.write(2, verb)

    def write(self, addr, data):
        self.mem[addr] = data

    def read(self, addr):
        return self.mem[addr]

    def done(self):
        return self.exit

    def waiting(self):
        return self.blocked

    # Opcode Definition
    def o_add(self, a, b, c):
        self.write(c, a + b)

    def o_mul(self, a, b, c):
        self.write(c, a * b)

    def o_in(self, a):
        input = self.get_input()
        if input is None:
            self.blocked = True
        else:
            self.write(a, input)

    def o_out(self, a):
        self.output.put(a)

    def o_jump_if_true(self, a, b):
        if a != 0:
            self.override_ip = b

    def o_jump_if_false(self, a, b):
        if a == 0:
            self.override_ip = b

    def o_equals(self, a, b, c):
        if a == b:
            self.write(c, 1)
        else:
            self.write(c, 0)

    def o_less_than(self, a, b, c):
        if a < b:
            self.write(c, 1)
        else:
            self.write(c, 0)

    def o_exit(self):
        self.exit = True

    opcodes = {
        1: ('ADD', o_add, 3, 2),
        2: ('MUL', o_mul, 3, 2),
        3: ('IN', o_in, 1, 0),
        4: ('OUT', o_out, 1, None),
        5: ('JMPT', o_jump_if_true, 2, None),
        6: ('JMPF', o_jump_if_false, 2, None),
        7: ('LT', o_less_than, 3, 2),
        8: ('EQ', o_equals, 3, 2),
        99: ('EXIT', o_exit, 0, None),
    }


def A():
    return None
    items = [int(item) for item in data.split(',')]

    from itertools import permutations
    phases = list(permutations(range(0, 5)))

    max = 0
    for s in phases:
        input = 0
        for phase in s:
            machine = Intcode(list(items))
            machine.add_input(phase)
            machine.add_input(input)
            machine.run()
            output = machine.get_output()
            input = output

        if output > max:
            max = output

    return max


def get_phase(items, s):
    from itertools import cycle

    machines = [Intcode(list(items)) for _ in range(len(s))]
    queues = [Queue() for _ in range(len(s))]
    for i in range(len(s)):
        queues[i].put(s[i])

    done = [False] * len(s)

    # Kickstart
    queues[0].put(0)

    for i in cycle(range(len(s))):
        m = machines[i]
        q = queues[i]

        print(i, s[i], m.blocked)

        m.run()

        try:
            m.add_input(q.get(block=False))
        except Empty:
            pass

        if m.done():
            done[i] = True

        o = m.get_output()
        if o is not None:
            queues[i % len(s)].put(o)

        if all(done):
            break

    return 3


def B():
    data = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    items = [int(item) for item in data.split(',')]

    o = get_phase(items, (9,8,7,6,5))
    print("output", o)

    return 0

    from itertools import permutations
    phases = list(permutations(range(5, 9 + 1)))

    max = 0
    output = 0
    for s in phases:
        output = get_phase(items, s)

    return max


def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
