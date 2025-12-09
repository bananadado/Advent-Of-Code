# part 2 took me way too long to figure out.
# i first did a blood fill type thing - too slow (~10 billion operations)
# i then did a ray casting type thing - I THOUGHT THIS WOULD BE FAST ENOUGH BUT APPARENTLY NOT WTF TOOK ME SO LONG TO IMPLEMENT
# i then finally did a ranges type thing based on the y like a dictionary
# - it still took 3 minutes to run
# - this approach isn't even correct
# - i just got lucky the puzzle input happens to be a "circle"
# speaking of which, this problem is actually doable extremely quickly in desmos due to this property
# below is an actually correct implementation using the module shapely
# i cannot actually think of a solution that runs fast enough without it - i might come back if i'm hit by some divine inspiration

from shapely.geometry import Polygon, box
from shapely.prepared import prep # improves execution time from 2.5 -> 1.3s on my machine
from itertools import combinations

with open("input.txt","r") as f:
   inp = [eval(line) for line in f.readlines()]

poly = prep(Polygon(inp))

# sort candidates first
area = lambda p, q: (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)
candidates = sorted(combinations(inp, 2), key=lambda x: area(*x), reverse=True)

print(f"Part 1: {area(*candidates[0])}")

for (x1, y1), (x2, y2) in candidates:
    rect = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    if poly.covers(rect):
        print(f"Part 2: {area((x1, y1), (x2, y2))}")
        quit()
