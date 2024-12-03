import re
with open("input.txt", "r") as f:
    inp = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', "".join([l.strip() for l in f.readlines()]))

p1 = 0
p2 = 0
do = True
for x in inp:
    if x == "don't()":
        do = False
        continue
    if x == "do()":
        do = True
        continue

    if do:
        p2 += int(x.split(",")[0][4:]) * int(x.split(",")[1][:-1])
    p1 += int(x.split(",")[0][4:]) * int(x.split(",")[1][:-1])

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
