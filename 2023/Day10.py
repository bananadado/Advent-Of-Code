# awful, awful day. Bad code too
# Part 2 essentially just searches outwards as in Day 18 of 2022
# A more optimal solution would be to consider a line (e.g. ..|...|..|.|..),
# where it is evident that the 2nd and 4th gaps would be inside the loop.
# I'm still in the process of neatening this code up so gimme a minute lol

from collections import deque

with open("input.txt", "r") as f:
    inp = [[x for x in line.strip()] for line in f.readlines()]

explored = [[False] * len(inp[0]) for _ in range(len(inp))]
inLoop = [[0] * len(inp[0]) for _ in range(len(inp))]
q = deque()

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
    if row > 0 and not explored[row - 1][col]:
        if inp[row - 1][col] in '7F|':
            explored[row - 1][col] = True
            q.append((row - 1, col, dist + 1))


def checkSouth1(row, col):
    if row < len(inp) - 1 and not explored[row + 1][col]:
        if inp[row + 1][col] in 'LJ|':
            explored[row + 1][col] = True
            q.append((row + 1, col, dist + 1))


def checkWest1(row, col):
    if col > 0 and not explored[row][col - 1]:
        if inp[row][col - 1] in 'LF-':
            explored[row][col - 1] = True
            q.append((row, col - 1, dist + 1))


def checkEast1(row, col):
    if col < len(inp[0]) - 1 and not explored[row][col + 1]:
        if inp[row][col + 1] in '7J-':
            explored[row][col + 1] = True
            q.append((row, col + 1, dist + 1))


pipeMap = {v: k for k, v in pipeMap.items()}
high = 0
while q:
    row, col, dist = q.popleft()
    high = max(dist, high)

    n, w, s, e = pipeMap[inp[row][col]]
    if n:
        checkNorth1(row, col)
    if w:
        checkWest1(row, col)
    if s:
        checkSouth1(row, col)
    if e:
        checkEast1(row, col)

print(f"Part 1: {high}")


# Part 2
def checkNorth2(row, col, dir, seen):
    if row > 0 and (row - 1, col) not in seen:
        if inp[row - 1][col] in ['7', 'F', '|']:
            seen.add((row - 1, col))
            if inp[row][col] == 'L' and dir == 'U':
                q.append((row - 1, col, 'R'))
            elif inp[row][col] == 'L' and dir == 'D':
                q.append((row - 1, col, 'L'))
            elif inp[row][col] == 'J' and dir == 'U':
                q.append((row - 1, col, 'L'))
            elif inp[row][col] == 'J' and dir == 'D':
                q.append((row - 1, col, 'R'))
            else:
                q.append((row - 1, col, dir))


def checkSouth2(row, col, dir, seen):
    if row < len(inp) - 1 and (row + 1, col) not in seen:
        if inp[row + 1][col] in ['L', 'J', '|']:
            seen.add((row + 1, col))
            if inp[row][col] == '7' and dir == 'U':
                q.append((row + 1, col, 'R'))
            elif inp[row][col] == '7' and dir == 'D':
                q.append((row + 1, col, 'L'))
            elif inp[row][col] == 'F' and dir == 'U':
                q.append((row + 1, col, 'L'))
            elif inp[row][col] == 'F' and dir == 'D':
                q.append((row + 1, col, 'R'))
            else:
                q.append((row + 1, col, dir))


def checkWest2(row, col, dir, seen):
    if col > 0 and (row, col - 1) not in seen:
        if inp[row][col - 1] in ['-', 'L', 'F']:
            seen.add((row, col - 1))
            if inp[row][col] == 'J' and dir == 'R':
                q.append((row, col - 1, 'D'))
            elif inp[row][col] == 'J' and dir == 'L':
                q.append((row, col - 1, 'U'))
            elif inp[row][col] == '7' and dir == 'R':
                q.append((row, col - 1, 'U'))
            elif inp[row][col] == '7' and dir == 'L':
                q.append((row, col - 1, 'D'))
            else:
                q.append((row, col - 1, dir))


def checkEast2(row, col, dir, seen):
    if col < len(inp[0]) - 1 and (row, col + 1) not in seen:
        if inp[row][col + 1] in ['-', 'J', '7']:
            seen.add((row, col + 1))
            if inp[row][col] == 'L' and dir == 'R':
                q.append((row, col + 1, 'U'))
            elif inp[row][col] == 'L' and dir == 'L':
                q.append((row, col + 1, 'D'))
            elif inp[row][col] == 'F' and dir == 'R':
                q.append((row, col + 1, 'D'))
            elif inp[row][col] == 'F' and dir == 'L':
                q.append((row, col + 1, 'U'))
            else:
                q.append((row, col + 1, dir))


for i in range(len(explored)):
    for j in range(len(explored[0])):
        if explored[i][j] or inp[i][j] in ['O', 'I']:
            continue
        loopSet = set()
        loopSet.add((i, j))
        q = deque()
        q.append((i, j))

        outside = False
        while q:
            row, col = q.popleft()
            if not outside:
                outside = row == 0 or row == len(inp) - 1 or col == 0 or col == len(inp[0]) - 1

            if row > 0 and (row - 1, col) not in loopSet and not explored[row - 1][col]:
                q.append((row - 1, col))
                loopSet.add((row - 1, col))
            if row < len(inp) - 1 and (row + 1, col) not in loopSet and not explored[row + 1][col]:
                q.append((row + 1, col))
                loopSet.add((row + 1, col))
            if col < len(inp[0]) - 1 and (row, col + 1) not in loopSet and not explored[row][col + 1]:
                q.append((row, col + 1))
                loopSet.add((row, col + 1))
            if col > 0 and (row, col - 1) not in loopSet and not explored[row][col - 1]:
                q.append((row, col - 1))
                loopSet.add((row, col - 1))

        # Try to find an escape
        if not outside:
            r, c = list(loopSet)[0]
            q.append((r, c, ''))
            seen = set()
            while q:
                row, col, dir = q.popleft()
                seen.add((row, col))

                if inp[row][col] == 'I':
                    break

                outside = not explored[row][col] and (row == 0 or row == len(inp) - 1 or col == 0 or col == len(inp[0]) - 1) \
                          or inp[row][col] == 'L' and col > 0 and dir in 'LD' and inp[row][col - 1] == 'O' \
                          or inp[row][col] == 'L' and row < len(inp) - 1 and dir in 'LD' and inp[row + 1][col] == 'O' \
                          or inp[row][col] == 'J' and col < len(inp) - 1 and dir in 'RD' and inp[row][col + 1] == 'O' \
                          or inp[row][col] == 'J' and row < len(inp) - 1 and dir in 'RD' and inp[row + 1][col] == 'O' \
                          or inp[row][col] == '7' and col < len(inp) - 1 and dir in 'RU' and inp[row][col + 1] == 'O' \
                          or inp[row][col] == '7' and row > 0 and dir in 'RU' and inp[row - 1][col] == 'O' \
                          or inp[row][col] == 'F' and col > 0 and dir in 'LU' and inp[row][col - 1] == 'O' \
                          or inp[row][col] == 'F' and row > 0 and dir in 'LU' and inp[row - 1][col] == 'O'
                if outside:
                    break

                if explored[row][col]:
                    n, w, s, e = pipeMap.get(inp[row][col])
                    if n:
                        checkNorth2(row, col, dir, seen)
                    if w:
                        checkWest2(row, col, dir, seen)
                    if s:
                        checkSouth2(row, col, dir, seen)
                    if e:
                        checkEast2(row, col, dir, seen)
                else:
                    if (row + 1, col) not in seen and (row + 1, col) not in loopSet:
                        seen.add((row + 1, col))
                        q.append((row + 1, col, 'U'))
                    if (row - 1, col) not in seen and (row - 1, col) not in loopSet:
                        seen.add((row - 1, col))
                        q.append((row - 1, col, 'D'))
                    if (row, col - 1) not in seen and (row, col - 1) not in loopSet:
                        seen.add((row, col - 1))
                        q.append((row, col - 1, 'R'))
                    if (row, col + 1) not in seen and (row, col + 1) not in loopSet:
                        seen.add((row, col - 1))
                        q.append((row, col - 1, 'L'))

        if outside:
            for row, col in loopSet:
                inp[row][col] = 'O'
        else:
            for row, col in loopSet:
                inp[row][col] = 'I'

total = 0
for l in inp:
    #print("".join(l)) # print the grid
    total += sum(1 for x in l if x == 'I')
print(f"Part 2: {total}")
