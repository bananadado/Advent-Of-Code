# I slept through all my alarms 😭
# I didn't even hear them go off
# Woke up at 6:45 and started coding at 7 ;-;
from itertools import count
with open("input.txt", "r") as f:
    inp = [[x for x in line.strip()] for line in f.readlines()]

def moveUp(grid: list):
    new = [[x for x in y] for y in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 'O':
                continue
            c = i
            while True:
                if c == 0 or new[c - 1][j] != '.':
                    break
                new[c][j] = '.'
                c -= 1
                new[c][j] = 'O'
    return new

def score(grid):
    t = 0
    for i, x in enumerate(grid[::-1]):
        t += (i + 1) * x.count('O')
    return t

seen = {}
for i in count():
    for j in range(4):
        inp = moveUp(inp)
        if i == 0 and j == 0:
            print(f"Part 1: {score(inp)}")
        inp = list(zip(*inp[::-1]))
    arr = tuple(tuple(x) for x in inp)
    if arr in seen:
        dex = seen[arr]
        print(f"Part 2: {score([k for k, v in seen.items()][(10**9 - dex - 1)%(i - dex) + dex])}")
        quit()
    seen[arr] = i
