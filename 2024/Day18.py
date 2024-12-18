# very easy today - 328/339, could've been faster but i just didn't read there was a byte restriction and also slow delta somehow idk it felt fast but apparently not
from collections import deque

# Read input from "input.txt"
with open("input.txt", "r") as f:
    data = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

corrupted = set(data[:1024])

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = 70
end = (N, N)
def find_path(part1):
    q = deque([(0, 0, 0)]) # (r, c, steps)
    visited = {(0, 0)}

    while q:
        r, c, steps = q.popleft()
        if (r, c) == end:
            return steps if part1 else True
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr <= N and 0 <= nc <= N and (nr, nc) not in corrupted and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, steps + 1))
    return False

print(f"Part 1: {find_path(True)}")
for x, y in data[1024:]:
    corrupted.add((x, y))
    if not find_path(False):
        print(f"Part 2: {x},{y}")
        break