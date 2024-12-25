# christmas!!! - 225/182
# i win @Imperial College London leaderboard!!!
with open("input.txt", "r") as f:
    inp = [line.split() for line in f.read().split("\n\n")]

keys = []
locks = []
for lk in inp:
    if lk[0][0] == "#":
        locks.append(lk)
    else:
        keys.append(lk)

R, C = 7, 5
t = 0
for key in keys:
    for lock in locks:
        fits = True
        for r in range(R):
            for c in range(C):
                if lock[r][c] == "#" and key[r][c] == "#":
                    fits = False
                    break
        t += fits

print(t)