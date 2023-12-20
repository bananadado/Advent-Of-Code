# Hardest day yet!
# I have a few dictionaries...
from collections import deque, defaultdict
from itertools import count
from math import prod, lcm
with open("input.txt", "r") as f:
    connections = {}
    ts = defaultdict(lambda: '')  # type: '& or %'
    for l in f.readlines():
        s, d = [x.strip() for x in l.split('->')]
        d = d.split(', ')
        connections[s] = d
        if s != "broadcaster":
            ts[s[1:]] = s[0]

reverseConnections = defaultdict(list)
conjConnections = defaultdict(dict)  # connections to each conjunction. False is low, True is high
states = defaultdict(lambda: False)  # flip-flop states, False is off, True is on
for k, v in connections.items():
    connections[k] = [ts[x] + x for x in connections[k]]
    for i in connections[k]:
        reverseConnections[i].append(k)
        if i[0] == '&':
            conjConnections[i][k] = False

# Looking at the input there is only 1 connection to rx and it is a conjunction
feed = {x: 0 for x in reverseConnections[reverseConnections["rx"][0]]}

scores = {"hi": 0, "lo": 0}
q = deque()
for i in count(1):
    q.append(("broadcaster", "", "lo"))

    while q:
        x, p, t = q.popleft()  # x = current node, p = previous node, t = type of signal
        scores[t] += 1

        if t == "lo" and x in feed and feed[x] == 0:
            feed[x] = i
            if all(j != 0 for j in feed.values()):
                print(f"Part 2: {lcm(*feed.values())}")
                quit()

        if x not in connections:
            continue

        # flip-flop
        # This reminds me: "Talk about Finite State Automatons and edge-triggered D-type flip-flops to make friends at a party" - my cs teacher.
        if x[0] == '%':
            if t == 'hi':
                continue
            t = "lo" if states[x] else "hi"
            states[x] = not states[x]

        # conjunction
        elif x[0] == '&':
            conjConnections[x][p] = t == "hi"
            t = "lo" if all(conjConnections[x].values()) else "hi"

        for y in connections[x]:
            q.append((y, x, t))

    if i == 1000:
        print(f"Part 1: {prod(scores.values())}")
