# This took me so long because I accidentally had "if inp[i][j] == '#'" in the nested loop check
# Didn't spot it, cost me ~25 minutes or 3 places on the lb
with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]


rows = []
for i, l in enumerate(inp):
    if '#' not in l:
        rows.append(i)
cols = []
for i in range(len(inp[0])):
    empty = True
    for j in range(len(inp)):
        empty = inp[j][i] != '#'
        if not empty:
            break
    if empty:
        cols.append(i)

part1 = 0
part2 = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == '#':
            for k in range(len(inp)):
                for l in range(len(inp[0])):
                    if inp[k][l] == '#':
                        part1 += abs((k - i)) + abs((l - j)) + sum(1 for x in cols if l < x < j or j < x < l) + sum(1 for x in rows if k < x < i or i < x < k)
                        part2 += abs((k - i)) + abs((l - j)) + sum(999999 for x in cols if l < x < j or j < x < l) + sum(999999 for x in rows if k < x < i or i < x < k)
print(f"Part 1: {part1//2}")
print(f"Part 2: {part2//2}")
