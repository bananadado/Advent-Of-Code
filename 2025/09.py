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
from shapely.prepared import prep # improves execution time from 6 -> 3s on my machine

with open("input.txt","r") as f:
   inp = [eval(line) for line in f.readlines()]

p = prep(Polygon(inp))

p1, p2 = 0, 0
for x1, y1 in inp:
    for x2, y2 in inp:
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        p1 = max(p1, area)

        if area <= p2:
            continue

        rect = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if p.covers(rect):
            p2 = max(p2, area)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")