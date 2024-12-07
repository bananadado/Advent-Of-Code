with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]
    LHS = [int(line.split(":")[0]) for line in inp]
    RHS = [[int(x) for x in line.split(":")[1].strip().split(" ")] for line in inp]

def pos(trgt, xs, pt = False):
    if len(xs) == 1:
        return trgt == xs[0]

    return (pos(trgt, [xs[0] * xs[1]] + xs[2:], pt)
            or pos(trgt, [xs[0] + xs[1]] + xs[2:], pt)
            or pt and pos(trgt, [int(f"{xs[0]}{xs[1]}")] + xs[2:], pt))

p1, p2 = 0, 0
for x in range(len(LHS)):
    p1 += pos(LHS[x], RHS[x], False) * LHS[x]
    p2 += pos(LHS[x], RHS[x], True) * LHS[x]

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")