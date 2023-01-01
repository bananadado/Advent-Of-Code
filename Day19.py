from collections import deque
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def part1(time, oreBC, clayBC, obsOreBC, obsClayBC, geodeOreBC, geodeObsBC):    #where BC = Bot Cost and Obs = Obsidian
    highest = 0
    q = deque()
    q.append((time, 0, 1, 0, 0, 0, 0, 0, 0))
    #time, ore, oreBots, clay, clayBots, obsidian, obsidianBots, geodes, geodeBots
    seen = set()
    while len(q) > 0:
        current = q.popleft()
        t, ore, oreBots, clay, clayBots, obsidian, obsidianBots, geodes, geodeBots = current

        if t == 0:
            highest = max(geodes, highest)
            continue

        #optimise the amount of bots being used as you don't need more than you need (wise words of wisdom)
        maxOreCost = max(oreBC, obsOreBC, geodeOreBC, clayBC)
        if oreBots > maxOreCost:
            oreBots = maxOreCost
        if clayBots > obsClayBC:
            clayBots = obsClayBC
        if obsidianBots > geodeObsBC:
            obsidianBots = geodeObsBC

        #I did not make the following optimisation but my friend told me about it afterwards as not to make the code take a year to run
        #Originally I was on a different computer which doesn't die when I run it without the following code for some reason even though it is less powerful???
        #optimise ore quantities so that cannot exceed the maximum you can spend
        if ore > (maxOreCost*t) - ((t-1)*oreBots):
            #have to reset them to this and not continue as there are varying degrees of overshooting
            ore = (maxOreCost*t) - ((t-1)*oreBots)
        if clay > (obsClayBC*t) - ((t-1)*clayBots):
            clay = (obsClayBC*t) - ((t-1)*clayBots)
        if obsidian > (geodeObsBC*t) - ((t-1)*obsidianBots):
            obsidian = (geodeObsBC*t) - ((t-1)*obsidianBots)

        newcurrent = (ore, oreBots, clay, clayBots, obsidian, obsidianBots, geodes, geodeBots) #time is not included as anything after this would have a worse time anyway
        if newcurrent in seen:
            continue
        seen.add(newcurrent)

        if ore >= oreBC:
            q.append((t - 1, ore + oreBots - oreBC, oreBots + 1, clay + clayBots, clayBots, obsidian + obsidianBots, obsidianBots, geodes + geodeBots, geodeBots))
        if ore >= clayBC:
            q.append((t - 1, ore + oreBots - clayBC, oreBots , clay + clayBots, clayBots + 1, obsidian + obsidianBots, obsidianBots, geodes + geodeBots, geodeBots))
        if ore >= obsOreBC and clay >= obsClayBC:
            q.append((t - 1, ore + oreBots - obsOreBC, oreBots , clay + clayBots - obsClayBC, clayBots, obsidian + obsidianBots, obsidianBots + 1, geodes + geodeBots, geodeBots))
        if ore >= geodeOreBC and obsidian >= geodeObsBC:
            q.append((t - 1, ore + oreBots - geodeOreBC, oreBots , clay + clayBots, clayBots, obsidian + obsidianBots - geodeObsBC, obsidianBots , geodes + geodeBots, geodeBots + 1))
        q.append((t - 1, ore + oreBots, oreBots, clay + clayBots, clayBots, obsidian + obsidianBots, obsidianBots, geodes + geodeBots, geodeBots))

    print(highest)
    return highest


totalp1 = 0
for i in range(len(lines)):
    words = lines[i].split()
    totalp1 += (i+1) * (part1(24, int(words[6]), int(words[12]), int(words[18]), int(words[21]), int(words[27]), int(words[30])))
    #time, ore bot cost, clay bot cost, obsidian ore bot cost, obsidian clay bot cost, geode ore bot cost, geode obsidian bot cost
print("Part 1:" , totalp1)

totalp2 = 1
for i in range(3):
    words = lines[i].split()
    totalp2 *= part1(32, int(words[6]), int(words[12]), int(words[18]), int(words[21]), int(words[27]), int(words[30]))
print("Part 2:",totalp2)