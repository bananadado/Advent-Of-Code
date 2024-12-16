# 300/296 - decent
# this sourish guy is cracked tho wtf
# also if king hang ma fails to wake up again i actually have a shot at first :D

# solution today is just dijkstra's. kind of messy, mostly due to trying to do part 2 in the same function.
# part 2 i just go through dijkstra's again and count against the part 1's path. (i had a slow delta figuring this out)
import heapq

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

for r, row in enumerate(inp):
    for c, char in enumerate(row):
        if char == 'S':
            start = (r, c)
        elif char == 'E':
            end = (r, c)

def solve(part2=False, main_path=set()):
    q = [(0, start[0], start[1], 0, set())]  # (score, row, col, direction, path taken)
    visited = set()
    s = float('inf')
    paths = set()

    while q:
        score, r, c, d, vis = heapq.heappop(q)

        if (r, c, d) in visited:
            if part2 and (r, c, d, score) in main_path:
                paths = paths.union((rr, cc) for rr, cc, _, _, in vis)
            continue
        visited.add((r, c, d))

        if (r, c) == end:
            s = min(s, score) # we know we will reach the minimum score first courtesy of dijkstra's
            if (r, c, d, score) in main_path:
                paths = paths.union((rr, cc) for rr, cc, _, _, in vis)
            if score > s: # all minimum paths completed
                if not part2:
                    return s, vis
                return len(paths) + 1

        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        if inp[nr][nc] != '#':
            heapq.heappush(q, (score + 1, nr, nc, d, vis.union({(r, c, d, score)})))

        # left
        nd = (d - 1) % 4
        heapq.heappush(q, (score + 1000, r, c, nd, vis.union({(r, c, d, score)})))

        # right
        nd = (d + 1) % 4
        heapq.heappush(q, (score + 1000, r, c, nd, vis.union({(r, c, d, score)})))



p1, last_minimum_path = solve()
print(f"Part 1: {p1}")
print(f"Part 2: {solve(True, last_minimum_path)}")