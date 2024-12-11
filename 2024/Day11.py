# mega fast today 383/204 - global leaderboard took longer thank i expected to fill up today
# it feels like ive finally started to lock in (e.g. day 2, 3, 6, 7, 8 - horrible)
# i suspected part 2 would be what it was but i wanted a fast part 1 so 4:13 delta
# (I didnt instantly think of the optimisation)
from collections import Counter
with open("input.txt", "r") as f:
    inp = f.read().split()


def solve(blinks):
    # Like memoization but for iteration
    stones = Counter(inp)

    for _ in range(blinks):
        new_stones = Counter()

        for stone, count in stones.items():
            if stone == "0":
                new_stones["1"] += count
            elif len(stone) % 2 == 0:
                l, r = stone[:len(stone) // 2], str(int(stone[len(stone) // 2:])) # remove leading 0s
                new_stones[l] += count
                new_stones[r] += count
            else:
                new_stones[str(int(stone) * 2024)] += count

        stones = new_stones

    return sum(stones.values())

print(f"Part 1: {solve(25)}")
print(f"Part 2: {solve(75)}")