# This one went somewhat well. Nice and easy (definitely should have been swapped with day 1). 😎 #emojiCoding
with open("input.txt", "r") as f:
    inp = [[part.split() for part in line.strip().split(':')[1].split('|')] for line in f.readlines()]

total = 0
instances = [1]*len(inp)
for i, x in enumerate(inp):
    current = 0
    for y in x[0]:
        if y in x[1]:
            current += 1
    total += int(2**(current - 1))

    for j in range(i + 1, current + i + 1):
        instances[j] += (instances[i])

print(f"Part 1: {total}")
print(f"Part 2: {sum(instances)}")