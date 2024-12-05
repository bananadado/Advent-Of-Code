from functools import cmp_to_key

with open("input.txt", "r") as f:
    spl = f.read().split("\n\n")
    order = [[int(x) for x in line.strip().split("|")] for line in spl[0].split("\n")]
    pgs = [[int(x) for x in line.strip().split(",")] for line in spl[1].split("\n")]

def plc(a, b):
    for x in order:
        if x[1] == b and x[0] == a:
            return -1
    return 1

p1, p2 = 0, 0
for ls in pgs:
    ys = sorted(ls, key = cmp_to_key(plc))
    if ls == ys:
        p1 += ls[(len(ls) - 1)//2]
    else:
        p2 += ys[(len(ls) - 1)//2]

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")