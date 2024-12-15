# I GOT GLOBALLL 89/248   !!!!!!!!!
# kinda threw part 2 tho
# in this refactor i solve part 1 in the same fashion as part 2 (essentially move_boxes()),
# however i originally went for just a for loop for part 1 instead of the bfs which is easier to think about => leaderboard
# also this took me a while to upload and refactor because i was sleeping and then forgot to upload
from collections import deque
from copy import deepcopy

dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

with open("input.txt", "r") as f:
    grid, instructions = f.read().split("\n\n")
    grid = [list(line.strip()) for line in grid.split("\n")]
    instructions = "".join(instructions.split("\n"))


def start_pos(G):
    for r in range(len(G)):
        for c in range(len(G[0])):
            if G[r][c] == '@':
                G[r][c] = '.'
                return r, c


def move_boxes(G, r, c, dr, dc):
    q = deque([(r, c)])
    seen = set()
    move = True

    while q:
        cr, cc = q.popleft()
        if (cr, cc) in seen:
            continue
        seen.add((cr, cc))
        nr, nc = cr + dr, cc + dc

        if G[nr][nc] == '#':
            move = False
            break

        if G[nr][nc] in "O[]":
            q.append((nr, nc))
        if G[nr][nc] == '[':
            q.append((nr, nc + 1))
        if G[nr][nc] == ']':
            q.append((nr, nc - 1))

    if not move:
        return False

    # move the boxes, making sure not to move the boxes over one another
    to_move = deque(seen)
    while to_move:
        xr, xc = to_move.popleft()
        mr, mc = xr + dr, xc + dc
        if (mr, mc) not in to_move: # nothing blocking
            G[mr][mc] = G[xr][xc]
            G[xr][xc] = '.'
        else:
            to_move.append((xr, xc))
    return True


def score(G):
    t = 0
    for r in range(len(G)):
        for c in range(len(G[0])):
            if G[r][c] in "[O":
                t += 100 * r + c
    return t


def solve(G):
    r, c = start_pos(G)
    for dir in instructions:
        dr, dc = dirs[dir]
        rr, cc = r + dr, c + dc

        if G[rr][cc] == '#':
            continue

        # move if you can
        if G[rr][cc] == '.' or move_boxes(G, r, c, dr, dc):
            r, c = rr, cc

    return score(G)


def expand_grid(G):
    expanded_grid = []
    for r in range(len(G)):
        row = ""
        for c in range(len(G[0])):
            if G[r][c] == 'O':
                row += "[]"
            elif G[r][c] == '@':
                row += "@."
            else:
                row += 2 * G[r][c]

        expanded_grid.append(list(row))
    return expanded_grid


print(f"Part 1: {solve(deepcopy(grid))}") # deepcopy is required to do part 2 after part 1 as the grid is modified by reference throughout
print(f"Part 2: {solve(expand_grid(grid))}")