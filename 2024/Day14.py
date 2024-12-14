# worst part 2 of all time just why. no information given at all
# absolutely just guessed what to do and happened to get the correct answer - make sure the bots are in unique locations
# also this code assumes part 2 is after part 1
# meh today 331/417

# stuff already written before today
import re
from itertools import count
from math import prod

def extract_integers(input_string, allow_negative=True):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]
    return integers

def replace_character_at_index(input_string, index, new_char):
    string_list = list(input_string)
    string_list[index] = new_char
    return ''.join(string_list)

# new code i wrote today
with open("input.txt", "r") as f:
    bots = [tuple(extract_integers(line.strip())) for line in f.readlines()]

W, H = 101, 103
for i in count(1):
    nbots = []
    for (px, py, vx, vy) in bots:
        nbots.append(((px + vx) % W, (py + vy) % H, vx, vy))

    if i == 100: # originally i had just (px + vx * 100) % W, (py + vy * 100) % H, but part 2 requires iterative sol
        quadrants = [0, 0, 0, 0]
        for (x, y, _, _) in nbots:
            quadrants[(x < W // 2) + 2 * (y < H // 2)] += x != W // 2 and y != H // 2
        print(f"Part 1: {prod(quadrants)}")

    if len(set([(x, y) for (x, y, _, _) in nbots])) == len(nbots):
        print(f"Part 2: {i}")

        # print the tree!
        grid = ["." * W for _ in range(H)]
        for (x, y, _, _) in nbots:
            grid[y] = replace_character_at_index(grid[y], x, "#")
        for row in grid:
            print(row)
        quit()

    bots = nbots