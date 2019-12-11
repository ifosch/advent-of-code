#!/usr/bin/env python

filename = 'input.txt'
with open(filename, 'r') as fp:
    line = fp.readline().strip()

items = [int(item) for item in line.split(',')]


class Intcode(object):
    def __init__(self, program, input=None):
        self.mem = program
        self.input = input

        self.outputs = []

        self.ip = 0  # Instruction Pointer
        self.halt = False
        self.override_ip = None

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

    def run(self):
        while self.step():
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

    # Opcode Definition
    def o_add(self, a, b, c):
        self.write(c, a + b)

    def o_mul(self, a, b, c):
        self.write(c, a * b)

    def o_in(self, a):
        if self.input is None:
            raise

        self.write(a, self.input)

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


machine = Intcode(list(items), input=5)
machine.run()
print(machine.get_outputs())
