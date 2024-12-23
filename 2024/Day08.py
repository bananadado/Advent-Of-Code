from collections import defaultdict

with open("input.txt", "r") as f:
    G = [line.strip() for line in f.readlines()]

R, C = len(G), len(G[0])
antennas = defaultdict(list)

for r in range(R):
    for c in range(C):
        if G[r][c] != '.':
            antennas[G[r][c]].append((r, c))


p1, p2 = set(), set()

# thanks zadukk for neatening my code
def find_antinode(c1, c2):
    (x1, y1), (x2, y2) = c1, c2
    dx, dy = x2 - x1, y2 - y1
    nx, ny = x2 + dx, y2 + dy

    if 0 <= nx < R and 0 <= ny < C:
        p1.add((nx, ny))

    p2.add((x2, y2))
    while 0 <= nx < R and 0 <= ny < C:
        p2.add((nx, ny))
        nx += dx
        ny += dy

# thanks flameded for neatening this part 😎
for freq, positions in antennas.items():
    for i, c1 in enumerate(positions):
        for c2 in positions[i+1:]:
            find_antinode(c1, c2)
            find_antinode(c2, c1)


print(f"Part 1: {len(p1)}")
print(f"Part 2: {len(p2)}")