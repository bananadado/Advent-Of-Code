# simple problem today but only 1118/790
# originally i had my own dict to handle memoization but now ive just switched to functools.cache
from functools import cache

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n\n")
    towels = set(data[0].split(", "))
    designs = data[1].split("\n")

@cache
def solve(design):
    if design == "":
        return 1

    ways = 0
    for i in range(1, len(design) + 1):
        if design[:i] in towels:
            ways += solve(design[i:])
    return ways

arrs = [solve(design) for design in designs]
print(f"Part 1: {sum(1 for x in arrs if x)}")
print(f"Part 2: {sum(arrs)}")