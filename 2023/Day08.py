from itertools import count
from math import lcm

with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]
    instr = inp[0]
    nodes = {x[0].strip(): [x[1][2:5], x[1][7:10]] for x in [y.split('=') for y in inp[2:]]}


def findEnd(current, ZZZ=False):
    for i in count():
        if instr[i % len(instr)] == 'L':
            current = nodes[current][0]
        else:
            current = nodes[current][1]

        if current == "ZZZ" or not ZZZ and current[-1] == 'Z':
            return i + 1


print(f"Part 1: {findEnd('AAA', True)}")
print(f"Part 2: {lcm(*[findEnd(x) for x in nodes.keys() if x[-1] == 'A'])}")
