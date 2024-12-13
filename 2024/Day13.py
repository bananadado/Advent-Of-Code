# Actually so close to global leaderboard today - 744/130 insane
# I got the correct approach first try thank you Ben Briggs (lin alg prof)
# I think I could've actually gotten it today if I locked in for part 1 better
import re

with open("input.txt", "r") as f:
    inp = f.read().strip().split("\n\n")


# matrix:
# (ax ay) (x) = (px)
# (bx by) (y)   (py)
def find_sol(ax, ay, bx, by, px, py):
    det = ax * by - ay * bx
    if det == 0:
        return 0

    # integer solutions
    if (py * ax - px * ay) % det != 0 or (px * by - py * bx) % det != 0:
        return 0

    na = (px * by - py * bx) // det
    nb = (py * ax - px * ay) // det

    # positive solutions only
    if na < 0 or nb < 0:
        return 0

    return na * 3 + nb


p1, p2 = 0, 0
for system in inp:
    lines = system.split("\n")
    ax, ay = map(int, re.search(r"X\+(-?\d+), Y\+(-?\d+)", lines[0]).groups())
    bx, by = map(int, re.search(r"X\+(-?\d+), Y\+(-?\d+)", lines[1]).groups())
    px, py = map(int, re.search(r"X=(-?\d+), Y=(-?\d+)", lines[2]).groups())

    p1 += find_sol(ax, ay, bx, by, px, py)
    p2 += find_sol(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")