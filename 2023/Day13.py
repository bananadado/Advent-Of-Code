# ngl i just got a bit confused
# and also my pc decided to kill itself ~15 minutes in and I was out of action for a while..
with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

nInp = [[]]
for l in inp:
    if l == '':
        nInp.append([])
    else:
        nInp[-1].append(l)


def findReflection(block, pack):
    # find vertical:
    for c in range(len(block[0]) - 1):
        curr = True
        left = [''.join([block[i][j] for i in range(len(block))]) for j in range(c + 1)][::-1]
        right = [''.join([block[i][len(block[0]) - j - 1] for i in range(len(block))]) for j in range(len(block[0]) - c - 1)][::-1]
        for i in range(min(c + 1, len(block[0]) - c - 1)):
            if left[i] != right[i]:
                curr = False
                break
        if curr and (c + 1, 'v') != pack:
            return c + 1, 'v'

    for c in range(len(block) - 1):
        curr = True
        top = block[:c + 1][::-1]
        bottom = block[c + 1:]
        for i in range(min(c + 1, len(block) - c - 1)):
            if top[i] != bottom[i]:
                curr = False
                break
        if curr and ((c + 1) * 100, 'r') != pack:
            return (c + 1) * 100, 'r'
    return 0, 0


reverse = {'.': '#', '#': '.'}
part1 = 0
part2 = 0
for block in nInp:
    ori = findReflection(block, (0, 0))
    part1 += ori[0]
    for i in range(len(block)):
        leave = False
        NB = [x for x in block]
        row = [x for x in block[i]]
        for j in range(len(block[0])):
            row[j] = reverse[NB[i][j]]
            NB[i] = ''.join(row)
            toAdd, d = findReflection(NB, ori)
            if toAdd != 0:
                part2 += toAdd
                leave = True
                break
            row[j] = reverse[NB[i][j]]
        if leave:
            break
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
