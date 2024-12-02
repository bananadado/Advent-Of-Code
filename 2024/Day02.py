with open("input.txt", "r") as f:
    inp = [[int(x) for x in line.strip().split()] for line in f.readlines()]

def safe(xs):
    if not (xs == sorted(xs) or xs == sorted(xs)[::-1]):
        return False

    for i in range(len(xs) - 1):
        if not 1 <= abs(xs[i] - xs[i+1]) <= 3:
            return False
    return True

p1 = 0
p2 = 0
for line in inp:
    if safe(line):
        p1 += 1

    for i in range(len(line)):
        if safe(line[:i] + line[i+1:]):
            p2 += 1
            break

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")