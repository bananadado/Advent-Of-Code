def ways(inp):
    prod = 1
    for i in range(len(inp[0])):
        total = 0
        for j in range(inp[0][i]):
            if j * (inp[0][i] - j) > inp[1][i]:
                total += 1
        prod *= total
    return prod


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(f"Part 1: {ways([[int(x) for x in line.strip().split(':')[1].split()] for line in lines])}")
    print(f"Part 2: {ways([[int(''.join(line.strip().split(':')[1].split()))] for line in lines])}")
