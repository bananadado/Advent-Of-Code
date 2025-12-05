# uh where is the difficulty
with open("input.txt","r") as f:
   inp = f.read().split("\n\n")
   ranges = [tuple(map(int, l.strip().split("-"))) for l in inp[0].split("\n")]
   ingredients = [int(l.strip()) for l in inp[1].split("\n")]

# merge ranges
ranges.sort()
merged = []

for a, b in ranges:
    if not merged or a > merged[-1][1] + 1:
        merged.append([a, b])
    else:
        merged[-1][1] = max(merged[-1][1], b)

t = 0
for x in ingredients:
    for a, b in merged:
        if a <= x <= b:
            t += 1
            break

print(f"Part 1: {t}")
print(f"Part 2: {sum(b - a + 1 for a, b in merged)}")