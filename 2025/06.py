# advent of reading comprehension i have never comprehended an easy problem this slowly
from itertools import groupby
from math import prod
with open("input.txt","r") as f:
   inp = [line.strip("\n") for line in f.readlines()]
   data, ops = inp[:-1], inp[-1].split()
   # rotation trick from many moons ago of unzipping then zipping
   nums = list(zip(*(map(int, l.split()) for l in data)))
   nums2 = [list(map(int, g)) for k, g in groupby(("".join(l).strip() for l in zip(*data)), bool) if k]

p1, p2 = 0, 0
for op, n1, n2 in zip(ops, nums, nums2):
    f = prod if op == "*" else sum
    p1 += f(n1)
    p2 += f(n2)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
