#!/usr/bin/env python

# Open Single Line File and iterate (split by comma)
filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

items = [int(item) for item in line.split(',')]


class Intcode(object):
    def __init__(self, program):
        self.mem = program

        self.ip = 0  # Instruction Pointer
        self.halt = False

    def step(self):
        curr = self.mem[self.ip]
        instr_name, operation, num_params = self.opcodes[curr]
        params = [self.mem[self.ip + i + 1] for i in range(num_params)]

        operation(self, params)

        if self.halt:
            return False

        self.ip += 1 + num_params

        return True

    def run(self):
        while self.step():
            pass

    def set_nounverb(self, noun, verb):
        self.mem[1] = noun
        self.mem[2] = verb

    def get_mempos(self, pos):
        return self.mem[pos]

    # Opcode Definition
    def o_add(self, params):
        self.mem[params[2]] = self.mem[params[0]] + self.mem[params[1]]

    def o_mul(self, params):
        self.mem[params[2]] = self.mem[params[0]] * self.mem[params[1]]

    def o_exit(self, params):
        self.halt = True

    opcodes = {
        1: ('ADD', o_add, 3),
        2: ('MUL', o_mul, 3),
        99: ('EXIT', o_exit, 0),
    }


machine = Intcode(list(items))
machine.set_nounverb(12, 2)
machine.run()
print(machine.get_mempos(0))
