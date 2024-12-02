with open("input.txt", "r") as f:
    inp = [[int(x) for x in line.strip().split()] for line in f.readlines()]
    inp1 = sorted(x for (x, _) in inp)
    inp2 = sorted(y for (_, y) in inp)

d = 0
s = 0
for x in range(len(inp)):
    d += abs(inp1[x] - inp2[x])
    s += inp1[x] * inp2.count(inp1[x])

print(f"Part 1: {d}")
print(f"Part 2: {s}")