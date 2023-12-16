from collections import deque
with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
bslash = {'R': 'D', 'D': 'R', 'L': 'U', 'U': 'L'}
fslash = {'R': 'U', 'D': 'L', 'U': 'R', 'L': 'D'}
def tile(r, c, d, q, seen, energised):
    if inp[r][c] == '.' and (r, c, d) not in seen:
        q.append((r, c, d))
        seen.add((r, c, d))
    elif inp[r][c] == '\\' and (r, c, bslash[d]) not in seen:
        q.append((r, c, bslash[d]))
        seen.add((r, c, bslash[d]))
    elif inp[r][c] == '/' and (r, c, fslash[d]) not in seen:
        q.append((r, c, fslash[d]))
        seen.add((r, c, fslash[d]))
    elif inp[r][c] == '|' and (r, c, d) not in seen:
        if d in 'LR':
            q.append((r, c, 'U'))
            seen.add((r, c, 'U'))
            q.append((r, c, 'D'))
            seen.add((r, c, 'D'))
        else:
            q.append((r, c, d))
        seen.add((r, c, d))
    elif inp[r][c] == '-' and (r, c, d) not in seen:
        if d in 'UD':
            q.append((r, c, 'L'))
            seen.add((r, c, 'L'))
            q.append((r, c, 'R'))
            seen.add((r, c, 'R'))
        else:
            q.append((r, c, d))
        seen.add((r, c, d))
    energised[r][c] = True


def beam(r1, c1, d1):
    energised = [[False] * len(inp[0]) for i in range(len(inp))]
    seen = set()
    q = deque()
    tile(r1, c1, d1, q, seen, energised)

    while q:
        r, c, d = q.popleft()
        rD, cD = move[d]
        if r + rD < 0 or c + cD < 0 or r + rD == len(inp) or c + cD == len(inp[0]):
            continue
        tile(r + rD, c + cD, d, q, seen, energised)

    return sum([x.count(True) for x in energised])


m = 0
for r in range(len(inp)):
    m = max(m, beam(r, 0, 'R'))
    if r == 0:
        print(f"Part 1: {m}")
    m = max(m, beam(r, len(inp[0]) - 1, 'L'))
for c in range(len(inp[0])):
    m = max(m, beam(0, c, 'D'))
    m = max(m, beam(len(inp) - 1, c, 'U'))
print(f"Part 2: {m}")
