# i noticed at the end i assumed ranges don't overlap
# idk i couldnt think of anything better than 3 for loops
# i also broke part 1 when i was refactoring and so the refactor isnt even that good :older_man:
with open("input.txt") as f:
    inp = sorted([tuple(map(int, part.split("-"))) for part in f.read().strip().split(',')])

# binary search over ranges
def in_ranges(x):
    lo, hi = 0, len(inp) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        a, b = inp[mid]
        if a <= x <= b:
            return True
        if x < a:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


end = inp[-1][1]
max_digits = len(str(end))

p1, p2 = 0, 0
seen1, seen2 = set(), set()
for total_len in range(2, max_digits + 1):
    for base_len in range(1, max_digits // 2 + 1):
        if total_len % base_len != 0:
            continue

        start = 10 ** (base_len - 1)
        max_repeats = max_digits // base_len

        for base_num in range(start, 10 * start):
            s = str(base_num)
            for r in range(2, max_repeats + 1):
                val = int(s * r)
                if val > end:
                    break

                # yh idk combining the part 1 code into part 2 was for some reason more difficult
                # than literally the entire problem itself
                if r == 2:
                    if val in seen1:
                        continue
                    seen1.add(val)
                    if in_ranges(val):
                        p1 += val
                        p2 += val if val not in seen2 else 0
                else:
                    if val in seen2:
                        continue
                    if in_ranges(val):
                        p2 += val
                seen2.add(val)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")