with open("input.txt", "r") as f:
    inp = [line.strip().split(':') for line in f.readlines()]
    inp = [[line.split(',') for line in l[1].split(';')] for l in inp]

count = 1
part1 = 0
part2 = 0
for line in inp:
    reject = False
    rMax, gMax, bMax = 0, 0, 0
    for i in range(len(line)):
        red, green, blue = 0, 0, 0
        for j in line[i]:
            if j.split()[1] == "blue":
                blue += int(j.split()[0])
            if j.split()[1] == "red":
                red += int(j.split()[0])
            if j.split()[1] == "green":
                green += int(j.split()[0])

        if red > 12 or green > 13 or blue > 14:
            reject = True

        bMax = max(blue, bMax); rMax = max(red, rMax); gMax = max(green, gMax)

    if not reject:
        part1 += count
    part2 += rMax * gMax * bMax
    count += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
