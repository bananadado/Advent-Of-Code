with open("input.txt", "r") as f:
    inp = [[int(x) for x in line.strip().split()] for line in f.readlines()]


print(inp)