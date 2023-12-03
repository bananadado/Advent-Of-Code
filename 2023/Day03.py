# Not my proudest work
# I had a sort of OBO error I didn't spot for wayyyy too long
# AoC is not looking good for me anymore ;-;

import re

with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]


def isSymbol(row, col):
    if row < 0 or row >= len(inp) or col < 0 or col >= len(inp[0]):
        return False
    if not inp[row][col].isdigit() and inp[row][col] != '.':
        return True
    return False


def isAddable(row, col):
    return any(isSymbol(row + i - 1, col + j - 1) for i in range(3) for j in range(3))


def extractInts(element):
    return [int(x) for x in re.findall(r'\d+', element)]


def findNum(row, col):
    for i in range(col, len(inp[0]) + 1):
        if i == len(inp[0]) or not inp[row][i].isdigit():
            return int(extractInts(inp[row][:i].split('.')[-1])[-1])


def ratio(row, col):
    nums = [inp[row - 1][col - 1:col + 2], inp[row][col - 1:col + 2], inp[row + 1][col - 1:col + 2]]
    nums = [[y.isdigit() for y in x] for x in nums]
    if nums[0][1]:
        nums[0] = [False, True, False]
    if nums[2][1]:
        nums[2] = [False, True, False]

    tot = sum(sum([1 if y else 0 for y in x]) for x in nums)

    if tot == 2:
        prod = 1
        for i in range(3):
            for j in range(3):
                if nums[i][j]:
                    prod *= findNum(row + i - 1, col + j - 1)
        return prod
    return 0


part1 = 0
part2 = 0

for i, line in enumerate(inp):
    # part 1
    spl = line.split('.')
    for j, element in enumerate(spl):
        if len(extractInts(element)) == 0:
            continue

        col = sum([len(x) + 1 for x in spl[:j]])
        for k in range(col, col + len(element)):
            if isAddable(i, k):
                part1 += sum(extractInts(element))
                break

    # part 2
    index = [j for j, x in enumerate(line) if x == "*"]
    part2 += sum(ratio(i, j) for j in index)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
