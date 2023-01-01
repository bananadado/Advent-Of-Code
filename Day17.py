with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

#Jonathan Paulson's sets because they look cool (rest is my own code)
def getPieces(num, ypos):
    if num == 0:
        return {(2, ypos), (3, ypos), (4, ypos), (5, ypos)}  # -
    if num == 1:
        return {(3, ypos + 2), (2, ypos + 1), (3, ypos + 1), (4, ypos + 1), (3, ypos)}  # +
    if num == 2:
        return {(2, ypos), (3, ypos), (4, ypos), (4, ypos + 1), (4, ypos + 2)}  # _|
    if num == 3:
        return {(2, ypos), (2, ypos + 1), (2, ypos + 2), (2, ypos + 3)}  # |
    if num == 4:
        return {(2, ypos + 1), (2, ypos), (3, ypos + 1), (3, ypos)}  # ■

def moveleft(piece):
    for (x,y) in piece:
        if x == 0 or (x-1,y) in verticalChamber:
            return piece
    return set([(x - 1, y) for (x, y) in piece])

def moveright(piece):
    for (x,y) in piece:
        if x == 6 or (x+1,y) in verticalChamber:
            return piece
    return set([(x + 1, y) for (x, y) in piece])

def movedown(piece):
    return set([(x, y - 1) for (x, y) in piece])

def movebackup(piece):
    return set([(x, y + 1) for (x, y) in piece])


verticalChamber = set()
count = 0
countDirect = 0
height = 0
true0 = True
while true0:
    piece = getPieces(count % 5, height+4)
    true1 = True
    while true1:
        direction = inp[0][countDirect%len(inp[0])]
        if direction == '<':
            piece = moveleft(piece)
        else:
            piece = moveright(piece)

        countDirect += 1

        piece = movedown(piece)

        for (x, y) in piece:
            if (x,y) in verticalChamber or y == 0:
                piece = movebackup(piece)
                true1 = False
                break
    for (x, y) in piece:
        verticalChamber.add((x,y))

    for (x, y) in verticalChamber:
        if y > height:
            height = y
    count += 1
    if count == 2022:
        print("Part 1:",height)
        true0 = False


h = []
for i in range(height):
    row = []
    for j in range(7):
        row.append(".")
    h.append(row)
for (x,y) in verticalChamber:
    #print(x,y)
    h[y-1][x] = '#'
# h.reverse()
with open("vertical chamber.txt", "w") as f:
    for line in h:
        f.write("".join(line))
        f.write("\n")
#Then Ctrl+F + calculator for part 2