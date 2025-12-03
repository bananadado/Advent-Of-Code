# actually keep throwing part 2 what am i doing could've easily been 1 minute delta
# why was this easier than day 2???
with open("input.txt") as f:
    inp = [[int(c) for c in l.strip()] for l in f.readlines()]

# for each row find the max digit in r[:-k]
# greedy approach is fine since 9.... > 8.... always
def max_subseq(arr, k):
    n = len(arr)
    start = 0
    res = []
    for pos in range(k):
        # find first max digit in subarray [start:end+1]
        end = n - (k - pos)
        md, mi = -1, -1
        for i in range(start, end + 1):
            d = arr[i]
            if d > md:
                md, mi = d, i
                if d == 9:
                    break
        res.append(md)
        start = mi + 1
    return to_base10(res)

def to_base10(arr):
    return int(''.join(map(str, arr)))

p1, p2 = 0, 0
for bank in inp:
    p1 += max_subseq(bank, 2)
    p2 += max_subseq(bank, 12)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
