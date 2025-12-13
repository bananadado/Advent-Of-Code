# I know today's problem was supposed to be implemented via Knuth's Algorithm X (probably)
# However, at 5am I really didn't want to have to learn it unless I really had to
# So I just implemented a very simple recursive backtracking
# - finding each shape's possible states and then just trying to place them
# (refactored to use pieces index, size heuristic, and a symmetry optimisation
#   - i didn't change any fundamental logic though, still checking pieces instead of trying to fill area e.g.)
# This is an extremely slow approach O(8^n * w * h) or so (i think - could actually be wrong)
# It takes for some reason an extremely variable amount of time to run on the sample input (but not less than 2 minutes)
# on a whim this morning i decided to run it on the actual input
# (maybe hoping for a 40 minute runtime - if it was a more interesting input i think it would've been a few hours actually :older_man:)
# and, lo and behold,
# it takes pretty much no time to run on the puzzle input
# Because not only are the grids that are not obviously too small all solvable,
# but each of them is solvable by just having 3x3 adjacent grids throughout
# so my dfs will be able to solve it in 1 pass :skull:
# So, we don't even need to run a search for the real input:
# you can just check if it's obviously not solvable (sum total shape areas and compare to grid size),
# and then do a quick check (which is ALWAYS true FOR SOME REASON) to check if the grid of 3x3 grids is a correct packing
# it would've been nice to have learnt the algorithm above (but also i would've probably done quite badly in terms of time)
# speaking of which - I WON THE INTER UNI LONDON WIDE AoC LEADERBOARD :D (but not the docsoc one somehow lmao)

# i may come back to this problem if i decide i wish to learn Algorithm X;
# however, i should probably redo the end of 2023 first

import re

origin = (0, 0)

# from template
def extract_integers(input_string, allow_negative=False):
    return list(map(int, re.findall(r'-?\d+' if allow_negative else r'\d+', input_string)))


# find all rotations/reflections of a shape
def variations(shape):
    # you remember the two point trick right? ;)
    def rotate(coords):
        return set((c, -r) for r, c in coords)

    def flip(coords):
        return set((r, -c) for r, c in coords)

    # place top-left-most '#' at origin
    def normalise(coords):
        min_r, min_c = min(list(coords))
        return tuple((r - min_r, c - min_c) for r, c in coords)

    # convert grid to coords
    current = {
        (r, c)
        for r, row in enumerate(shape)
        for c, ch in enumerate(row)
        if ch == '#'
    }

    # dihedral group of order 8 via 2 generators
    states = set()
    for _ in range(4):
        states.add(normalise(current))
        states.add(normalise(flip(current)))
        current = rotate(current)

    return list(states)


# recursive backtracking - O(8^n * w * h) where n is the number of pieces :D
def dfs(grid, w, h, pieces, states, sr, sc, pidx):
    if pidx < 0:
        return True

    piece = pieces[pidx]

    for r in range(sr, h):
        for c in range(sc if r == sr else 0, w):
            if grid[r][c]:
                continue

            # try to fit the shape anchored at r, c
            # i think precomputing available slots is more efficient here,
            # but I'd probably want to use a 1 dimensional approach which I don't want to implement
            for state in states[piece]:
                cells = []
                for dr, dc in state:
                    nr, nc = r + dr, c + dc

                    # coord is occupied or out of bounds
                    if not (0 <= nr < h and 0 <= nc < w) or grid[nr][nc]:
                        break

                    cells.append((nr, nc))
                else: # ooh for-else wackiness
                    for pr, pc in cells:
                        grid[pr][pc] = True

                    nx = (r, c) if (pidx > 0 and pieces[pidx - 1] == piece) else origin # symmetry optimisation
                    if dfs(grid, w, h, pieces, states, *nx, pidx - 1):
                        return True

                    # unplace
                    for pr, pc in cells:
                        grid[pr][pc] = False

    return False


with open("input.txt", "r") as f:
    inp = f.read().split("\n\n")

shapes = [variations(l.split("\n")[1:]) for l in inp if '#' in l]
areas = [len(s[0]) for s in shapes]
grids = [extract_integers(l) for l in inp[-1].split("\n")] # w, h, *qts

t = 0
for g in grids:
    w, h, *qts = g

    # obviously too many items
    if sum(a * qt for a, qt in zip(areas, qts)) > w * h:
        continue

    # adjacent packing of 3x3 grids :skull:
    # works on all puzzle inputs for some reason >:(
    if sum(qts) <= (w // 3) * (h // 3):
        t += 1
        continue

    # else actually run the dfs
    # make an occupancy grid
    grid = [[False] * w for _ in range(h)]

    # queue of pieces to place in grid
    # sorted by size (heuristic) ascending
    # traverse via pointer pidx
    pieces = sorted([i for i, qt in enumerate(qts) for _ in range(qt)], key=lambda x: (areas[x], x))

    if dfs(grid, w, h, pieces, shapes, *origin, len(pieces) - 1):
        t += 1

print(f"Part 1: {t}")