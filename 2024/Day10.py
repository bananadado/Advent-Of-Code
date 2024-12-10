# most average AOC problem ever to be made ever
# fast again today 382/535. kind of misread part 2 so long delta of 3:53 :(
from collections import deque

with open("input.txt") as f:
    G = [list(map(int, line.strip())) for line in f]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
R, C = len(G), len(G[0])

def bfs(sr, sc):
    paths, trails = set(), set()
    q = deque([(sr, sc, [(sr, sc)])])

    while q:
        r, c, path = q.popleft()
        if G[r][c] == 9:
            paths.add((r, c)) # p1
            trails.add(tuple(path)) # p2
            continue

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == G[r][c] + 1 and (nr, nc) not in path:
                q.append((nr, nc, path + [(nr, nc)]))

    return len(paths), len(trails)

p1, p2 = 0, 0
for r in range(R):
    for c in range(C):
        if G[r][c] == 0:
            pp1, pp2 = bfs(r, c)
            p1 += pp1
            p2 += pp2

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")