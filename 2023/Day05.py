# I had a solution extremely similar to this one to begin with (using nested lists rather than tuples)
# But somehow when I was neatening it up I broke it 👴
# My original solution was with the nested lists but instead of doing the sort for part 2, it just compared the values
with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()] + ['']

# Part 1
seeds = [int(x) for x in inp[0].split(':')[1].split()]
tamper = [False]*len(seeds)

# Part 2
# Find the ranges [lb, ub]
ranges = [(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1] - 1) for i in range(0, len(seeds) // 2)]
currentMappedRanges = []

for i in inp:
    # Reset some stuff before going onto the next mapping
    if len(i) == 0 or not i[0].isdigit():
        # Part 1
        tamper = [False] * len(seeds)

        # Part 2
        ranges += currentMappedRanges
        currentMappedRanges = []
        continue

    # Part 1
    nums = [int(x) for x in i.split()]
    for j, x in enumerate(seeds):
        if not tamper[j] and x in range(nums[1], nums[1]+nums[2]):
            tamper[j] = True
            seeds[j] = nums[0]+x-nums[1]

    # Part 2
    nums = [int(x) for x in i.split()]
    add = nums[0] - nums[1]
    sourceStart = nums[1]
    sourceEnd = nums[1] + nums[2] - 1

    currentRanges = []
    for x, y in ranges:
        sort = sorted([x, y, sourceStart, sourceEnd])
        bounds = [(sort[0], sort[1]), (sort[1], sort[2]), (sort[2], sort[3])]

        for lb, ub in bounds:
            # The bounds are not in the range we are looking at so they can be ignored
            if x > lb or y < ub:
                continue

            # The source range totally covers the whole range
            if sourceStart <= lb and sourceEnd >= ub:
                currentMappedRanges.append((lb + add, ub + add))
            else:
                currentRanges.append((lb, ub))
    ranges = currentRanges

print(f"Part 1: {min(seeds)}")
print(f"Part 2: {min([x for x, y in ranges])}")
