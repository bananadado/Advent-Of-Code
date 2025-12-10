# Favourite problem this year so far
# I realised in part 1 that its just a linear system over F2
# Then for part 2 its a linear system (domain >= 0)
# i could've gotten a much better part 1 time via brute force though (combinations)
from z3 import *
import re

# from template
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers


def parse(line):
    parts = line.split()
    diag = [0 if c == '.' else 1 for c in parts[0][1:-1]]
    buttons = [tuple(extract_integers(b)) for b in parts[1:-1]]
    joltages = extract_integers(parts[-1])
    return diag, buttons, joltages


def solve(target, buttons, mod2=True):
    x = [Int(f"x{i}") for i in range(len(buttons))]
    opt = Optimize()

    # domain for each button
    # I originally had a boolean domain for part 1 but it shouldn't matter,
    # since choosing x[j] = 3 can never be true since we're minimising and x[j] = 1 does the same thing over F2
    for xi in x:
        opt.add(xi>=0)

    # constraints for each position
    for i in range(len(target)):
        affected = [x[j] for j, b in enumerate(buttons) if i in b]

        if mod2:
            opt.add(Sum(affected) % 2 == target[i])
        else:
            opt.add(Sum(affected) == target[i])

    total = Sum(x)
    opt.minimize(total)

    # its aoc, system always solvable
    if opt.check() != sat:
        raise ValueError

    return opt.model().evaluate(total).as_long()


with open("input.txt") as f:
    inp = [line.strip() for line in f]

p1 = p2 = 0
for line in inp:
    diag, buttons, joltages = parse(line)
    p1 += solve(diag, buttons, mod2=True)
    p2 += solve(joltages, buttons, mod2=False)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")