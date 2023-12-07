from functools import cmp_to_key
with open("input.txt", "r") as f:
    inp = [line.strip().split() for line in f.readlines()]

strength1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
strength2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def evalHand(hand):
    c = set(hand)
    if len(c) == 1:
        return 6
    if len(c) == 2:
        if any([hand.count(x) == 4 for x in c]):
            return 5
        return 4
    if len(c) == 3:
        if any([hand.count(x) == 3 for x in c]):
            return 3
        return 2
    if len(c) == 4:
        return 1
    return 0

def cmpIter(cards1, cards2, strength):
    for a, b in zip(cards1, cards2):
        if strength.index(a) < strength.index(b):
            return 1
        if strength.index(a) > strength.index(b):
            return -1

def cmpHand1(hand1, hand2):
    score1 = evalHand(hand1[0])
    score2 = evalHand(hand2[0])
    if score1 == score2:
        return cmpIter(hand1[0], hand2[0], strength1)
    return score1 - score2

def cmpHand2(hand1, hand2):
    score1 = max(evalHand(hand1[0].replace('J', x)) for x in strength1)
    score2 = max(evalHand(hand2[0].replace('J', x)) for x in strength1)
    if score1 == score2:
        return cmpIter(hand1[0], hand2[0], strength2)
    return score1 - score2

print(f"Part 1: {sum([int(x[1]) * (i+1) for i, x in enumerate(sorted(inp, key=cmp_to_key(cmpHand1)))])}")
print(f"Part 2: {sum([int(x[1]) * (i+1) for i, x in enumerate(sorted(inp, key=cmp_to_key(cmpHand2)))])}")
