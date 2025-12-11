# i thought this was going to be the hardest day this year but it was insanely easy
from functools import cache
with open("input.txt","r") as f:
   inp = [line.strip().split() for line in f]
   inp = {l[0][:-1] : l[1:] for l in inp}


@cache
def dfs(node, fft=False, dac=False, part1=True):
    if node == "out":
        return part1 or (fft and dac)

    fft |= (node == "fft")
    dac |= (node == "dac")

    return sum(dfs(n, fft, dac, part1) for n in inp[node])


print(f"Part 1: {dfs("you")}")
print(f"Part 2: {dfs("svr", part1=False)}")