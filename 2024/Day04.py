with open("input.txt", "r") as f:
    G = [line.strip() for line in f.readlines()]

# not a good solution but it was decently fast
R = len(G)
C = len(G[0])
p1, p2 = 0, 0
for r in range(R):
    p1 += G[r].count("XMAS")
    p1 += G[r].count("SAMX")
    for c in range(C):
        if r <= R - 4:
            if G[r][c] + G[r+1][c] + G[r+2][c] + G[r+3][c] in {"XMAS", "SAMX"}:
                p1 += 1
            if c <= C - 4 and G[r][c] + G[r+1][c+1] + G[r+2][c+2] + G[r+3][c+3] in {"XMAS", "SAMX"}:
                p1 += 1
            if c >= 3 and G[r][c] + G[r+1][c-1] + G[r+2][c-2] + G[r+3][c-3] in {"XMAS", "SAMX"}:
                p1 += 1

        if  (0 < r < R - 1 and 0 < c < C - 1
                and G[r][c] == "A"
                and len({G[r-1][c-1] + G[r+1][c+1], G[r+1][c-1] + G[r-1][c+1]}.union({"MS", "SM"})) == 2):
            p2 += 1

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
