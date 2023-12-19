# ngl this is bad code
# not sure I want to neaten this mess haha
# finally got 1st this year tho :D
import re
from collections import deque
with open("input.txt", "r") as f:
    workflows = {}
    ratings = []
    r = False
    for l in f.readlines():
        l = l.strip()
        if not r:
            if len(l) == 0:
                r = True
                continue
            l = l.split('{')
            workflows[l[0]] = l[1].strip('}').split(',')
        else:
            ratings.append(l)

def evalPart(part):
    x, m, a, s = [int(x.split('=')[1].strip('}')) for x in part.split(',')]
    totals = {'x': x, 'm': m, 'a': a, 's': s}

    current = 'in'
    while True:
        if current in 'AR':
            break
        for i in workflows[current]:
            if ':' not in i:
                current = i
                break

            c, move = i.split(':')
            if '>' in c and totals[c[0]] > int(c.split('>')[1]) or '<' in c and totals[c[0]] < int(c.split('<')[1]):
                current = move
                break
    return sum(totals.values()) if current == 'A' else 0

print(f"Part 1: {sum(evalPart(x) for x in ratings)}")

# x, m, a, s; all in form [lb, ub]
q = deque()
q.append(('in', {"xl": 1, "xu": 4000, "ml": 1, "mu": 4000, "al": 1, "au": 4000, "sl": 1, "su": 4000}))
t = 0
while q:
    current, bounds = q.popleft()
    if current == 'R':
        continue
    if current == 'A':
        t += (bounds["xu"] - bounds["xl"] + 1) * (bounds["mu"] - bounds["ml"] + 1) * (bounds["au"] - bounds["al"] + 1) * (bounds["su"] - bounds["sl"] + 1)
        continue
    for x in workflows[current]:
        if ':' not in x:
            q.append((x, bounds))
            break

        cv, n, move = re.split('[<>:]', x)
        n = int(n)
        cu, cl = f"{cv}u", f"{cv}l"
        clone = dict(bounds)

        if '>' in x and n < clone[cu]:
            bounds[cu] = n
            clone[cl] = n + 1
            q.append((move, clone))
        elif '<' in x and n > clone[cl]:
            bounds[cl] = n
            clone[cu] = n - 1
            q.append((move, clone))

print(f"Part 2: {t}")
