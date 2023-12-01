with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

numDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

part1 = 0
part2 = 0
for line in inp:
    digits = [c for c in line if c.isdigit()]
    part1 += int(digits[0] + digits[-1])
    for key in numDict.keys():
        line = line.replace(key, f"{key}{numDict[key]}{key}")
    digits = [c for c in line if c.isdigit()]
    part2 += int(digits[0] + digits[-1])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")