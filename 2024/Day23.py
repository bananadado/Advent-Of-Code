# very easy graph theory problem - 374/314
from collections import defaultdict
from itertools import combinations

# networkx solution for part 2. i realised after the fact i could've just used this and done the problem in <1 min instead of 6
# import networkx as nx
# G = nx.Graph()
# with open("input.txt", "r") as f:
#     G.add_edges_from([tuple(line.strip().split("-")) for line in f.readlines()])
# print(",".join(sorted(max(list(nx.find_cliques(G)), key=len))))


# my solution
with open("input.txt", "r") as f:
    inp = [line.strip().split("-") for line in f.readlines()]
    G = defaultdict(set) # adjacency list
    for a, b in inp:
        G[a].add(b)
        G[b].add(a)

triangles = set()
for node in G:
    for a, b in combinations(G[node], 2):
        if a in G[b]:
            triangles.add(tuple(sorted((node, a, b))))
print(f"Part 1: {len([t for t in triangles if any(node.startswith("t") for node in t)])}")


# used bron-kerbosch algorithm to find the largest clique (https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm#Without_pivoting)
# apparently Flameded used a bfs and he had a 2 min delta so I should've probably just done that as I had forgotten the bk algo
def bron_kerbosch(R, P, X):
    if not P and not X:
        return [sorted(R)]

    cliques = []
    for v in list(P):
        cliques.extend(bron_kerbosch(R | {v}, P & G[v], X & G[v])) # i didnt know you can use | and & on sets (pycharm randomly suggested it) all my older solutions are long now :(
        P.remove(v)
        X.add(v)
    return cliques

print("Part 2: " + ",".join(sorted(max(bron_kerbosch(set(), set(G.keys()), set()), key=len))))