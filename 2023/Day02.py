with open("input.txt", "r") as f:
    inp = [line.strip().split(':') for line in f.readlines()]
    inp = [[line.split(',') for line in l[1].split(';')] for l in inp]

count = 1
part1 = 0
part2 = 0
for line in inp:
    reject = False
    bMax = 0; rMax = 0; gMax = 0
    for i in range(len(line)):
        blue = 0; red = 0; green = 0
        for j in line[i]:
            if j.split()[1] == "blue":
                blue += int(j.split()[0])
            if j.split()[1] == "red":
                red += int(j.split()[0])
            if j.split()[1] == "green":
                green += int(j.split()[0])

        if red > 12 or green > 13 or blue > 14:
            reject = True
        if i == len(line) - 1 and not reject and red <= 12 and green <= 13 and blue <= 14:
            part1 += count

        bMax = max(blue, bMax); rMax = max(red, rMax); gMax = max(green, gMax)
    part2 += bMax * rMax * gMax
    count += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
