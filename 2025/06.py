# advent of reading comprehension i have never comprehended an easy problem this slowly
from itertools import groupby
from math import prod
with open("input.txt","r") as f:
   inp = [line.strip("\n") for line in f.readlines()]
   data = inp[:-1]
   # rotation trick from many moons ago of unzipping then zipping
   nums = list(zip(*(map(int, l.split()) for l in data)))
   nums2 = [list(map(int, g)) for k, g in groupby(("".join(l).strip() for l in zip(*data)), bool) if k]
   ops = inp[-1].split()

p1, p2 = 0, 0
for i in range(len(ops)):
    p1 += prod(nums[i]) if ops[i] == "*" else sum(nums[i])
    p2 += prod(nums2[i]) if ops[i] == "*" else sum(nums2[i])

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
