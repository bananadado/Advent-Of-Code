# took me a bit too long to write up union find
# also i didn't realise part 2 is an mst until after the problem i was just doing part 1 over and over and increasing K in part 1 (woops)
# also also i should've just pulled a zadukk and used networkx (massive blunder from me)
import heapq
from math import prod
from itertools import count

with open("input.txt","r") as f:
   inp = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

n = len(inp)

# theres "only" 1 million edges so can actually just store them all (yippee)
edges = []
for i in range(n):
    x1, y1, z1 = inp[i]
    for j in range(i+1, n):
        x2, y2, z2 = inp[j]
        dx = x1 - x2; dy = y1 - y2; dz = z1 - z2
        d2 = dx*dx + dy*dy + dz*dz
        edges.append((d2, i, j))
heapq.heapify(edges)

# union find
parent = list(range(n))
size = [1]*n

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: # in the same union already
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True


num_components = n
for i in count(1):
    _, a, b = heapq.heappop(edges)

    if union(a, b):
        num_components -= 1

    if i == 1000: # part 1
        # check all the root nodes (gives unique cliques)
        print(f"Part 1: {prod(sorted([size[k] for k in range(n) if parent[k] == k], reverse=True)[:3])}")

    if num_components == 1: # part 2
        print(f"Part 2: {inp[a][0] * inp[b][0]}")
        quit()
