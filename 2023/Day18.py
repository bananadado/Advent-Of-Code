# Original naive approach was to plot on a grid and then floodfill
# I then needed to research and learn Pick's Theorem
with open("input.txt", "r") as f:
    inp = [line.strip().split() for line in f.readlines()]

move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
def solve(nums, part2):
    coords = [(0, 0)]

    # perimeter
    p = 0
    for l in nums:
        r, c = coords[-1]
        rd, cd = move[l[0] if not part2 else "RDLU"[int(l[2][-2])]]
        n = int(l[1]) if not part2 else int(l[2][2:-2], 16)
        p += n
        coords.append((r + rd * n, c + cd * n))

    # shoelace
    s = 0
    for i, (x, y) in enumerate(coords):
        s += x * coords[(i + 1) % len(coords)][1] - y * coords[(i + 1) % len(coords)][0]
    return (abs(s) + p) // 2 + 1

print(f"Part 1: {solve(inp, False)}")
print(f"Part 2: {solve(inp, True)}")
