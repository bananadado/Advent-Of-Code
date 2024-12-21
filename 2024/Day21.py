# 485/516
# originally for part 1 i just had 5*bfs but obviously had to completely recode for part 2
# this implementation stores locations of each key and then does permutations instead of doing a bfs from one key to another
# it took me a while to think of this solution for the refactor but it now runs in 0.002166600010241382s on my machine (perf_counter)
from functools import lru_cache # this is so lazy
from itertools import permutations

with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

# no longer needed for the refactor
# numpad = [["7", "8", "9"],
#           ["4", "5", "6"],
#           ["1", "2", "3"],
#           [None, "0", "A"]]
# dpad = [[None, "^", "A"],
#         ["<", "v", ">"]]

# using dictionaries here is easier and has faster lookup
# None is just where the gap is (no paths can go over it)
numpad = { '7': (0, 0), '8': (0, 1), '9': (0, 2),
           '4': (1, 0), '5': (1, 1), '6': (1, 2),
           '1': (2, 0), '2': (2, 1), '3': (2, 2),
          None: (3, 0), '0': (3, 1), 'A': (3, 2)}

dpad = {None: (0, 0), "^": (0, 1), "A": (0, 2),
         "<": (1, 0), "v": (1, 1), ">": (1, 2)}


dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
rdirs = {v: k for k, v in dirs.items()}


def paths(s, e, empty):
    if s == e:
        return ['A']

    dr, dc = e[0] - s[0], e[1] - s[1]
    moves = ""
    if dr != 0:
        moves += rdirs[(dr / abs(dr), 0)] * abs(dr)
    if dc != 0:
        moves += rdirs[(0, dc / abs(dc))] * abs(dc)

    # no paths can go over the empty space
    valid = []
    for p in permutations(moves):
        cr, cc = s
        ok = True
        for move in p:
            ddr, ddc = dirs[move]
            cr, cc = cr + ddr, cc + ddc
            if (cr, cc) == empty:
                ok = False
                break
        if ok:
            valid.append("".join(p) + "A")

    return valid


@lru_cache
def optimal_path(seq, bots, first=False):
    locs = numpad if first else dpad # first iteration is on numpad

    t = 0
    cpos = locs["A"] # start at A
    for key in seq:
        npos = locs[key]
        all_paths = paths(cpos, npos, locs[None])

        if bots == 0: # base case last robot
            t += min(len(path) for path in all_paths)
        else:
            t += min(optimal_path(path, bots - 1) for path in all_paths)
        cpos = npos

    return t


def solve(ndpads):
    return sum([optimal_path(code, ndpads, True) * int(code[:-1]) for code in inp])


print(f"Part 1: {solve(2)}")
print(f"Part 2: {solve(25)}")