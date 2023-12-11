# awful, awful day. Bad code too
# Part 2 essentially just searches outwards as in Day 18 of 2022
# A more optimal solution would be to consider a line (e.g. ..|...|..|.|..),
# where it is evident that the 2nd and 4th gaps would be inside the loop.
from collections import deque

with open("input.txt", "r") as f:
    inp = [[x for x in line.strip()] for line in f.readlines()]

explored = [[False] * len(inp[0]) for _ in range(len(inp))]
q = deque()  # global queue that I will use for everything

# Find S and replace it
# (U, L, D, R)
pipeMap = {(1, 1, 0, 0): 'J', (1, 0, 1, 0): '|', (1, 0, 0, 1): 'L', (0, 1, 1, 0): '7', (0, 1, 0, 1): '-', (0, 0, 1, 1): 'F'}
for i in range(len(inp)):
    if 'S' in inp[i]:
        j = inp[i].index('S')
        q.append((i, j, 0))
        explored[i][j] = True
        inp[i][j] = pipeMap[(inp[i - 1][j] in '7F|', inp[i][j - 1] in 'LF-', inp[i + 1][j] in 'LJ|', inp[i][j + 1] in '7J-')]
        break


# Part 1
def checkNorth1(row, col):
    if not explored[row - 1][col]:
        explored[row - 1][col] = True
        q.append((row - 1, col, dist + 1))

def checkSouth1(row, col):
    if not explored[row + 1][col]:
        explored[row + 1][col] = True
        q.append((row + 1, col, dist + 1))

def checkWest1(row, col):
    if not explored[row][col - 1]:
        explored[row][col - 1] = True
        q.append((row, col - 1, dist + 1))

def checkEast1(row, col):
    if not explored[row][col + 1]:
        explored[row][col + 1] = True
        q.append((row, col + 1, dist + 1))


pipeMap = {v: k for k, v in pipeMap.items()}
high = 0
while q:
    r, c, dist = q.popleft()
    high = max(dist, high)

    n, w, s, e = pipeMap[inp[r][c]]
    if n:
        checkNorth1(r, c)
    if w:
        checkWest1(r, c)
    if s:
        checkSouth1(r, c)
    if e:
        checkEast1(r, c)

print(f"Part 1: {high}")

# Part 2
north = {'LU': 'R', 'LD': 'L', 'JU': 'L', 'JD': 'R'}
def checkNorth2(row, col, d, seen):
    if (row - 1, col) not in seen:
        seen.add((row - 1, col))
        q.append((row - 1, col, north.get(inp[row][col] + d, d)))

south = {'7U': 'R', '7D': 'L', 'FU': 'L', 'FD': 'R'}
def checkSouth2(row, col, d, seen):
    if (row + 1, col) not in seen:
        seen.add((row + 1, col))
        q.append((row + 1, col, south.get(inp[row][col] + d, d)))

west = {'JR': 'D', 'JL': 'U', '7R': 'U', '7L': 'D'}
def checkWest2(row, col, d, seen):
    if (row, col - 1) not in seen:
        seen.add((row, col - 1))
        q.append((row, col - 1, west.get(inp[row][col] + d, d)))

east = {'LR': 'U', 'LL': 'D', 'FR': 'D', 'FL': 'U'}
def checkEast2(row, col, d, seen):
    if (row, col + 1) not in seen:
        seen.add((row, col + 1))
        q.append((row, col + 1, east.get(inp[row][col] + d, d)))


for i in range(len(explored)):
    for j in range(len(explored[0])):
        if explored[i][j] or inp[i][j] in 'OI':
            continue
        loopSet = {(i, j)}
        q = deque()
        q.append((i, j))

        # Find a set of connected non-pipes
        outside = False
        while q:
            r, c = q.popleft()
            outside = outside or r == 0 or r == len(inp) - 1 or c == 0 or c == len(inp[0]) - 1

            if r > 0 and (r - 1, c) not in loopSet and not explored[r - 1][c]:
                q.append((r - 1, c))
                loopSet.add((r - 1, c))
            if r < len(inp) - 1 and (r + 1, c) not in loopSet and not explored[r + 1][c]:
                q.append((r + 1, c))
                loopSet.add((r + 1, c))
            if c < len(inp[0]) - 1 and (r, c + 1) not in loopSet and not explored[r][c + 1]:
                q.append((r, c + 1))
                loopSet.add((r, c + 1))
            if c > 0 and (r, c - 1) not in loopSet and not explored[r][c - 1]:
                q.append((r, c - 1))
                loopSet.add((r, c - 1))

        # Try to find an escape around the pipes
        if not outside:
            rt, ct = list(loopSet)[0]
            q.append((rt, ct, ''))
            seen = set()
            while q:
                r, c, d = q.popleft()
                seen.add((r, c))

                if inp[r][c] == 'I':
                    break

                outside = not explored[r][c] and (r == 0 or r == len(inp) - 1 or c == 0 or c == len(inp[0]) - 1) \
                          or inp[r][c] == 'L' and c > 0 and d in 'LD' and inp[r][c - 1] == 'O' \
                          or inp[r][c] == 'L' and r < len(inp) - 1 and d in 'LD' and inp[r + 1][c] == 'O' \
                          or inp[r][c] == 'J' and c < len(inp) - 1 and d in 'RD' and inp[r][c + 1] == 'O' \
                          or inp[r][c] == 'J' and r < len(inp) - 1 and d in 'RD' and inp[r + 1][c] == 'O' \
                          or inp[r][c] == '7' and c < len(inp) - 1 and d in 'RU' and inp[r][c + 1] == 'O' \
                          or inp[r][c] == '7' and r > 0 and d in 'RU' and inp[r - 1][c] == 'O' \
                          or inp[r][c] == 'F' and c > 0 and d in 'LU' and inp[r][c - 1] == 'O' \
                          or inp[r][c] == 'F' and r > 0 and d in 'LU' and inp[r - 1][c] == 'O'
                if outside:
                    break

                if explored[r][c]:
                    n, w, s, e = pipeMap.get(inp[r][c])
                    if n:
                        checkNorth2(r, c, d, seen)
                    if w:
                        checkWest2(r, c, d, seen)
                    if s:
                        checkSouth2(r, c, d, seen)
                    if e:
                        checkEast2(r, c, d, seen)
                else:
                    if (r + 1, c) not in seen and (r + 1, c) not in loopSet:
                        seen.add((r + 1, c))
                        q.append((r + 1, c, 'U'))
                    if (r - 1, c) not in seen and (r - 1, c) not in loopSet:
                        seen.add((r - 1, c))
                        q.append((r - 1, c, 'D'))
                    if (r, c - 1) not in seen and (r, c - 1) not in loopSet:
                        seen.add((r, c - 1))
                        q.append((r, c - 1, 'R'))
                    if (r, c + 1) not in seen and (r, c + 1) not in loopSet:
                        seen.add((r, c - 1))
                        q.append((r, c - 1, 'L'))

        mark = 'O' if outside else 'I'
        for r, c in loopSet:
            inp[r][c] = mark

total = 0
for l in inp:
    # print("".join(l)) # print the grid
    total += sum(1 for x in l if x == 'I')
print(f"Part 2: {total}")
