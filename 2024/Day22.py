# I GOT GLOBALLLL - 266/75
# how did the leaderboard fill up so slowly i swear it should've been full in like 5 mins such an easy problem
# also the last weekend problem? sooooo difficulty tends not to be that bad after this... (easiest year?!??!?)
from collections import Counter

with open("input.txt", "r") as f:
    inp = [int(line.strip()) for line in f.readlines()]


def evolve(s):
    prices = [s % 10]
    for _ in range(2000):
        s = (s ^ (s * 64)) % 16777216
        s = (s ^ (s // 32)) % 16777216
        s = (s ^ (s * 2048)) % 16777216
        prices.append(s % 10)
    return prices, s

def diffs(prices):
    return [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

t = 0
seq_sum = Counter()
for secret in inp:
    prices, sn = evolve(secret)
    changes = diffs(prices)
    t += sn

    seen = set()
    for i in range(len(changes) - 3):
        seq = tuple(changes[i: i + 4])
        if seq not in seen:
            seq_sum[seq] += prices[i + 4]
            seen.add(seq)

print(f"Part 1: {t}")
print(f"Part 2: {max(seq_sum.values())}")