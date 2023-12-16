from collections import defaultdict
import re
with open("input.txt", "r") as f:
    inp = f.readline().split(',')

def score(word):
    t = 0
    for c in word:
        t += ord(c)
        t *= 17
        t %= 256
    return t

print(f"Part 1: {sum([score(x) for x in inp])}")

boxes = defaultdict(lambda: [])
focal = defaultdict(lambda: 0)

for i in inp:
    j = re.split('[-=]', i)

    if j[0] not in boxes[score(j[0])]:
        if '-' in i:
            continue
        boxes[score(j[0])].append(j[0])
        focal[j[0]] = int(j[1])
    else:
        if '-' in i:
            boxes[score(j[0])].remove(j[0])
        else:
            focal[j[0]] = int(j[1])

t = 0
for k, v in boxes.items():
    for i in range(len(v)):
        t += (k + 1) * (i + 1) * focal[v[i]]
print(f"Part 2: {t}")
