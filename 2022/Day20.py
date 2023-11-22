from collections import deque
with open("input.txt", "r") as f:
    niput = []
    for i, line in enumerate(f.readlines()):
        if line.strip() == '0':
            tempindex = i
        niput.append((int(line.strip()), i)) #i is a unique identifier

def decryption(part):
    if part == 2:
        for i in range(len(niput)):
            num, index = niput[i]
            niput[i] = (num * 811589153, index)

    output = deque(niput)

    for i in range(part * 9 - 8): #want 1 time for part 1 and 10 for part 2
        for item in niput:
            while output[0] != item:
                output.append(output.popleft())
            toMove = output.popleft()
            movement, index = toMove
            temp = list(output)

            if movement < 0:
                movement += (abs(movement//len(temp)) + 1) * len(temp)
            if movement > len(temp):
                movement = movement % len(temp)
            temp.insert(movement, toMove)
            output = deque(temp)

    outputList = list(output)
    index0 = outputList.index((0, tempindex))
    num1, _ = outputList[(index0 + 1000)%len(outputList)]
    num2, _ = outputList[(index0 + 2000)%len(outputList)]
    num3, _ = outputList[(index0 + 3000)%len(outputList)]
    print(f"Part {part}: {(num1 + num2 + num3)}")

decryption(1)
decryption(2)