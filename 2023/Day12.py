# I overslept...
with open("input.txt", "r") as f:
    inp = [line.strip().split() for line in f.readlines()]

seen = {}
def perm(springs, groups, i, j, current):
    key = (i, j, current)
    if key in seen:
        return seen[key]
    if i == len(springs):
        if j == len(groups) and current == 0 or j == len(groups) - 1 and groups[j] == current:
            return 1
        return 0

    ans = 0
    # Continue along the line of .'s
    if (springs[i] == '.' or springs[i] == '?') and current == 0:
        ans += perm(springs, groups, i + 1, j, 0)
    # Continue along the line but start a new block of #'s
    elif (springs[i] == '.' or springs[i] == '?') and j < len(groups) and groups[j] == current:
        ans += perm(springs, groups, i + 1, j + 1, 0)
    # Continue the block of #'s
    if springs[i] == '#' or springs[i] == '?':
        ans += perm(springs, groups, i + 1, j, current + 1)

    seen[key] = ans
    return ans


part1 = 0
part2 = 0
for l in inp:
    part1 += perm(l[0], [int(x) for x in l[1].split(',')], 0, 0, 0)
    seen.clear()
    part2 += perm('?'.join([l[0]] * 5), [int(x) for x in ','.join([l[1]] * 5).split(',')], 0, 0, 0)
    seen.clear()

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
