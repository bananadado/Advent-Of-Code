with open("input.txt", "r") as f:
    G = [line.strip() for line in f.readlines()]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left

R, C = len(G), len(G[0])
sr, sc = 0, 0
for i in range(R):
    for j in range(C):
        if G[i][j] == "^":
            sr, sc = i, j


# global variables something or other (G, R, C, sr, sc, dirs)
def iterate(obstacle = (-1, -1)):
    r, c = sr, sc
    d = 0
    visited = set()
    uniq_visited = set()

    while True:
        if (r, c, d) in visited:
            return 1 # part 2

        visited.add((r, c, d))
        uniq_visited.add((r, c))

        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc

        # leave the grid
        if not (0 <= nr < R and 0 <= nc < C):
            return uniq_visited if (obstacle == (-1, -1)) else 0 # part 1, else part 2

        # change direction
        if G[nr][nc] == "#" or (nr, nc) == obstacle:
            d = (d + 1) % 4
        else:
            r, c = nr, nc


path = iterate()
print(f"Part 1: {len(path)}")
print(f"Part 2: {sum(iterate(xy) for xy in path)}") # obstacles can only affect on path