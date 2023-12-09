with open("input.txt", "r") as f:
    inp = [line.strip().split() for line in f.readlines()]

def nextTerms(sequence):
    differences = []
    for i in range(len(sequence) - 1):
        differences.append(sequence[i + 1] - sequence[i])

    if all([x == 0 for x in differences]):
        return differences

    nextDiff = nextTerms(differences)
    return [differences[0] - nextDiff[0]] + differences + [differences[-1] + nextDiff[-1]]


p1 = 0
p2 = 0
for l in inp:
    next = nextTerms([int(x) for x in l])
    p1 += int(l[-1]) + next[-1]
    p2 += int(l[0]) - next[0]

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
