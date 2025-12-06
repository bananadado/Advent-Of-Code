# advent of reading comprehension i have never comprehended an easy problem this slowly
# might revisit this there might be an easier way to parse part 2
from math import prod
with open("input.txt","r") as f:
   inp = [line.strip("\n") for line in f.readlines()]
   data = inp[:-1]
   nums = list(zip(*[list(map(int, l.strip().split())) for l in data])) # rotation trick from many moons ago
   ops = inp[-1].split()

# form part 2 data
def get_part2_from_range(s, e):
    problem = []
    for j in range(s, e):
        n = ""
        for k in range(len(data)):
            if data[k][j] == ' ':
                continue
            n += data[k][j]
        problem.append(int(n))
    return problem

nums2 = []
prev = 0
for i in range(len(data[0])):
    space = True
    for j in range(len(data)):
        if data[j][i] != ' ':
            space = False
            break
    if not space: # not a new set of numbers
        continue

    nums2.append(get_part2_from_range(prev, i))
    prev = i + 1

nums2.append(get_part2_from_range(prev, len(data[0]) - 1))

p1, p2 = 0, 0
for i in range(len(ops)):
    p1 += prod(nums[i]) if ops[i] == "*" else sum(nums[i])
    p2 += prod(nums2[i]) if ops[i] == "*" else sum(nums2[i])

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
