# i sure do love bfs!
# meh 589/465 - i really struggled with part 2 IT JUST WOULDNT WORK AHHHHH
# the idea i had was the "correct" approach at least...

# also somebody please stop Lily Yeung, CoolCoder1149 (if you are them its really obvious...)

# refactoring took a long time today
# originally no defaultdict for sides and I instead stored (nr, nc, dr, dc) in a set
# this however made for more complicated code for the secondary bfs so ive refactored it using a defaultdict
# and now its simpler as I dont check directions as they are all now already grouped as such
from collections import deque, defaultdict

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

R, C = len(inp), len(inp[0])

seen = set()
p1, p2 = 0, 0
for r in range(R):
    for c in range(C):
        if (r, c) in seen:
            continue

        q = deque([(r, c)])
        t = inp[r][c]
        area, perim = 0, 0
        edges = defaultdict(set)

        while q:
            cr, cc = q.popleft()
            if (cr, cc) in seen:
                continue

            seen.add((cr, cc))
            area += 1

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < R and 0 <= nc < C and inp[nr][nc] == t:
                    if (nr, nc) not in seen:
                        q.append((nr, nc))
                else:
                    perim += 1
                    edges[(dr, dc)].add((cr, cc)) # separate by direction

        sides = 0
        for d, perims in edges.items():
            seen_edges = set()
            for (pr, pc) in perims:
                if (pr, pc) not in seen_edges: # non contiguous
                    sides += 1
                    q = deque([(pr, pc)])

                    while q:
                        cr, cc = q.popleft()
                        if (cr, cc) in seen_edges:
                            continue

                        seen_edges.add((cr, cc))
                        for dr, dc in dirs:
                            nr, nc = cr + dr, cc + dc
                            if (nr, nc) in perims:
                                q.append((nr, nc))

        p1 += area * perim
        p2 += area * sides

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")