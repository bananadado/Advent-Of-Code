# very aoc day i was extremely ready for this kind of problem
# first day of not completely selling
from itertools import count
with open("input.txt") as f:
    inp = [list(l.strip()) for l in f.readlines()]

H = len(inp)
W = len(inp[0])

dirs = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1), (1,0), (1,1),
]

t = 0
locs = set()
for i in count():
    for r in range(H):
        for c in range(W):
            if inp[r][c] != "@":
                continue

            count = 0
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < H and 0 <= nc < W and inp[nr][nc] == "@":
                    count += 1
            if count < 4:
                t += 1
                locs.add((r,c))

    if len(locs) == 0: # all unaccessible
        break

    #overwrite inp
    for r, c in locs:
        inp[r][c] = "#"
    locs.clear()

    # part 1
    if i == 0:
        print(f"Part 1: {t}")

print(f"Part 2: {t}")