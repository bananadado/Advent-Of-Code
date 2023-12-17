# There's some minor adjustments I'd like to make because the heapq doesn't seem to be working as I want it but I'm going back to bed
# Also can't believe Nathan beat me on part 2 by 1 second!
import heapq
with open("input.txt", "r") as f:
    inp = [[int(x) for x in line.strip()] for line in f.readlines()]


move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
back = {'R': 'L', 'U': 'D', 'L': 'R', 'D': 'U'}
def solve(part2):
    q = [(0, 0, 0, 'R', 0)]
    seen = set()
    m = float('inf')
    while q:
        s, r, c, d, n = heapq.heappop(q)

        if (r, c, d, n) in seen:
            continue
        seen.add((r, c, d, n))

        if r == len(inp) - 1 and c == len(inp[0]) - 1:
            m = min(m, s)
            continue

        for k, (rd, cd) in move.items():
            if back[d] == k or not part2 and k == d and n == 2 or part2 and (k != d and n < 3 or k == d and n > 8):
                continue
            if 0 <= r + rd < len(inp) and 0 <= c + cd < len(inp[0]):
                heapq.heappush(q, (s + inp[r + rd][c + cd], r + rd, c + cd, k, n + 1 if k == d else 0))
    return m

print(f"Part 1: {solve(False)}")
print(f"Part 2: {solve(True)}")
