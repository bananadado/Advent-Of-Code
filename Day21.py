monkeys = []
monkeyOp = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        monkeys.append(line.split()[0].strip(':'))
        temp = []
        for i in range(1, len(line.split())):
            temp.append(line.split()[i])
        monkeyOp.append(temp)

def monkeyThrower(monkeyIndex):
    if len(monkeyOp[monkeyIndex]) == 1:
        return int(monkeyOp[monkeyIndex][0])
    operation = monkeyOp[monkeyIndex][1]
    if operation == "*":
        return monkeyThrower(monkeys.index(monkeyOp[monkeyIndex][0])) * monkeyThrower(monkeys.index(monkeyOp[monkeyIndex][2]))
    if operation == "+":
        return monkeyThrower(monkeys.index(monkeyOp[monkeyIndex][0])) + monkeyThrower(monkeys.index(monkeyOp[monkeyIndex][2]))
    if operation == "-":
        return monkeyThrower(monkeys.index(monkeyOp[monkeyIndex][0])) - monkeyThrower(monkeys.index(monkeyOp[monkeyIndex][2]))
    if operation == "/":
        return monkeyThrower(monkeys.index(monkeyOp[monkeyIndex][0])) / monkeyThrower(monkeys.index(monkeyOp[monkeyIndex][2]))


print(f"Part 1: {int(monkeyThrower(monkeys.index('root')))}")


#I actually ended up losing my python code for day 21 so I had to rewrite it :(   (I don't remember it exactly so it might be slightly influenced)
#make it so that it find which value is affected by humn
monkeyOp[monkeys.index('humn')] = [0]
check1 = monkeyThrower(monkeys.index(monkeyOp[monkeys.index('root')][0]))
monkeyOp[monkeys.index('humn')] = [1]
check2 = monkeyThrower(monkeys.index(monkeyOp[monkeys.index('root')][0]))
if check1 == check2:
    monkeyOp[monkeys.index('root')][0], monkeyOp[monkeys.index('root')][2] = monkeyOp[monkeys.index('root')][2], monkeyOp[monkeys.index('root')][0]

#This doesn't work for the test input as it is a binary search and the plot of points available are on a curve so I seem to have gotten kind of lucky with my input
target = monkeyThrower(monkeys.index(monkeyOp[monkeys.index('root')][2]))
low = 0
high = 999999999999999999999

while True:
    midpoint = (low + high)//2
    monkeyOp[monkeys.index('humn')] = [midpoint]
    score = monkeyThrower(monkeys.index(monkeyOp[monkeys.index('root')][0])) - target
    if score > 0:
        low = midpoint
    elif score < 0:
        high = midpoint
    else:
        print(f"Part 2: {midpoint}")
        break
