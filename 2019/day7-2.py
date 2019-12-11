#!/usr/bin/env python

from random import randint

filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

items = [int(item) for item in line.split(',')]


class Intcode(object):
    def __init__(self, program, input=None):
        self.ID = randint(0, 1000000)

        print("{}: Starting Machine".format(self.ID))
        self.mem = program
        self.input = []

        self.outputs = []

        self.ip = 0  # Instruction Pointer
        self.halt = False
        self.override_ip = None

        self.blocked = False

    def add_input(self, val):
        print("{}: Unblocking Machine".format(self.ID))

        self.input.append(val)
        self.blocked = False

    def get_input(self):
        if not len(self.input):
            print("{}: Blocking Machine".format(self.ID))

            self.blocked = True
            return -1

        return self.input.pop(0)

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

        # print(instr_name, modes, num_params, params)

        operation(self, *params)

        if self.halt:
            return False

        if self.override_ip:
            self.ip = self.override_ip
            self.override_ip = None
        else:
            self.ip += 1 + num_params

        return True
    
    def is_halted(self):
        return self.halt

    def run(self):
        while (not self.blocked) and self.step():
            pass

    def set_nounverb(self, noun, verb):
        self.write(1, noun)
        self.write(2, verb)

    def write(self, addr, data):
        self.mem[addr] = data

    def read(self, addr):
        return self.mem[addr]

    def get_outputs(self):
        return self.outputs

    def get_output(self):
        return self.get_outputs()[0]

    # Opcode Definition
    def o_add(self, a, b, c):
        self.write(c, a + b)

    def o_mul(self, a, b, c):
        self.write(c, a * b)

    def o_in(self, a):
        input = self.get_input()
        if input != -1:
            self.write(a, input)
        else:
            self.override_ip = self.ip

    def o_out(self, a):
        self.outputs.append(a)

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
        print("{}: Machine Execution Completed".format(self.ID))

        self.halt = True

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

from itertools import permutations, cycle
phase_combinations = list(permutations(range(5, 10))) 

max = 0
for phases in phase_combinations:
    machines = {}

    print("Trying phases {}".format(phases))
    for m in range(0, len(phases)):
        print(m)
        machines[m] = Intcode(list(items))

    for m in range(0, len(phases)):
        machines[m].run()

    break

    outputs = {}
    for m in cycle(range(0, 5)):
        if len(outputs) == 5:
            break

        if m in outputs:
            continue

        if m not in machines:
            machines[m] = Intcode(list(items))
            machines[m].add_input(phase[m])

        if m == 0:
            machines[m].add_input(0)
        
        machines[m].run()

        if m > 0 and machines[m].blocked:
            if (m-1) in outputs:
                machines[m].add_input(outputs[m-1])

        if machines[m].is_halted():
            outputs[m] = machines[m].get_output()


    if outputs[4] > max:
        max = outputs[4]
    
print("Max", max)
