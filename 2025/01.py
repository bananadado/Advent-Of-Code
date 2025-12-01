# actually sold on part 2 forgot about rotations > 100
with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]
    inp = [(r[0], int(r[1:])) for r in inp]


pos = 50
cz = 0 #p1
cpz = 0 #p2

for d, l in inp:

    if d == 'L':
        pos = (pos - l)
        if pos <= 0:
            cpz += abs(pos // 100)

    else:  # 'R'
        pos = (pos + l)
        if pos >= 100:
            cpz += pos // 100

    pos %= 100

    if pos == 0:
        cz += 1

print(f"Part 1: {cz}")
print(f"Part 2: {cpz}")