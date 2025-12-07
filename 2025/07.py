# actually threw today i was so slow on part 2 and implemented a slow idea which took me too long to think of
# took recursive idea from zadukk. original approach was backtracking with a defaultdict
# i then merged part 1 which was just a dfs into the recursion
from functools import cache
with open("input.txt","r") as f:
   inp = [line.strip() for line in f.readlines()]

H = len(inp)
W = len(inp[0])

for r in range(H):
    for c in range(W):
        if inp[r][c] == 'S':
            start = (r, c)
            break

splits = set()

@cache
def ways(r, c):
    while True:
        r += 1
        if r >= H: # end
            return 1

        if inp[r][c] == '.':
            continue
        else: # splitter
            splits.add((r, c))
            way = 0
            for nc in (c - 1, c + 1):
                if 0 <= nc < W:
                    way += ways(r, nc)
            return way

    raise ValueError

p2 = ways(*start)

print(f"Part 1: {len(splits)}")
print(f"Part 2: {p2}")