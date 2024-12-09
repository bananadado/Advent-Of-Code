# fastest time yet today - 450/306 (10:18/23:11) :))
with open("input.txt") as f:
    inp = f.read().strip()

# refactoring is hard :( - certain other people/solutions helped me with this (trust me you do not want to see the original)
def solve(pt2):
    files = [] # (pos, size, ID)
    frees = [] # (pos, size)
    disk_layout = []

    file_id = 0
    index = 0
    for i, l in enumerate(inp):
        length = int(l)
        if i % 2 == 0:
            if pt2: # group
                files.append((index, length, file_id))
            else: # individual
                files.extend([(index + i, 1, file_id) for i in range(length)])
            disk_layout.extend([file_id] * length)
            file_id += 1
        else:
            frees.append((index, length))
            disk_layout.extend([-1] * length)
        index += length

    # defragment
    for pos, size, file_id in reversed(files):
        for s_i, (s_pos, s_size) in enumerate(frees):
            if s_pos < pos and size <= s_size:
                for i in range(size):
                    disk_layout[pos + i] = -1  # clear old pos
                    disk_layout[s_pos + i] = file_id  # move to new pos
                frees[s_i] = (s_pos + size, s_size - size)
                break

    # checksum
    return sum(pos * block_id for pos, block_id in enumerate(disk_layout) if block_id != -1)


print(f"Part 1: {solve(False)}")
print(f"Part 2: {solve(True)}")
