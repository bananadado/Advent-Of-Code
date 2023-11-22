#DISCLAIMER
#I did manage to get part 1 on the day in the most ridiculous fashion possible which I should put here:
#So I had made a program for part 1 of day 16 which is completely wrong: gave an output of 600.
#Because I was frustrated with the wrong answer I decided to use the output for my friend's input as a sort of ratio with his actual output - 1820/525. 
#I then multiplied my answer by this, and lo and behold: a correct answer! (600*(1820/525) = 2080)

#I didn't manage to do this one on the day and ended up doing it on the 24th. I needed a bit of help :(

from collections import deque, defaultdict

def parseInput():
    inputs = dict()
    with open("input.txt") as f:
        for line in f.readlines():
            line = line.rstrip()

            node = line.split(' ')[1]
            flow = int(line.split(' ')[4].split('=')[1][:-1])  # flow rate
            nextElements = line.split('valve')[1].replace('s ', '').replace(' ', '').split(',') 

            inputs[node] = [flow, tuple(nextElements)]
    return inputs


def bfs(start, end, graph):  # bfs from node to node (start to end)
    q = deque([(start, 0)])
    distances = defaultdict(lambda: float('inf'))
    while len(q) > 0:
        position, steps = q.popleft()

        if position == end:  # reached goal
            break

        for neighbour in graph[position][1]:
            nsteps = steps + 1
            if nsteps < distances[neighbour]:
                distances[neighbour] = nsteps
                q.append((neighbour, nsteps))

    return distances[end]


def weightedValves(inputs: dict):  # important nodes lol
    nonZero = {name for name, value in inputs.items() if value[0] > 0}
    nonZero.add('AA')
    return nonZero


def shortestPaths(worthy_valves: set, graph: dict):
    # get the shortest path
    shortestPath = defaultdict(dict)

    nonZero_list = list(worthy_valves)
    for idx, start in enumerate(nonZero_list):
        for end in nonZero_list[idx + 1:]:
            path_cost = bfs(start, end, graph)  # shortest path

            # Put this information into th edictionary, both directions
            shortestPath[start][end] = path_cost
            shortestPath[end][start] = path_cost

    return shortestPath


def everyMove(shortestPath, graph, time):
    pathes = defaultdict(lambda: -1)

    q = deque([('AA', 0, time, set())])
    while len(q) > 0:
        position, currentFlow, time, visited = q.popleft()

        # get neighbours that are in reach
        neighbours = (neighbour for neighbour in shortestPath[position] if
                      neighbour not in visited and shortestPath[position][neighbour] < time)

        # update the maximum
        if pathes[frozenset(visited)] < currentFlow:
            pathes[frozenset(visited)] = currentFlow

        # append the neighbours
        for neighbour in neighbours:
            newFlow = (time - shortestPath[position][neighbour] - 1) * graph[neighbour][0]

            new_set = visited | {neighbour}
            q.append((neighbour, currentFlow + newFlow, time - shortestPath[position][neighbour] - 1, new_set))
    return pathes


def part1():
    inputs = parseInput()  # get inputs
    nonZero = weightedValves(inputs)

    shortestPath = shortestPaths(nonZero, inputs)

    pathes = everyMove(shortestPath, inputs, 30)

    print(f'Part 1: {max(pathes.values())}')


def part2():
    inputs = parseInput()
    nonZero = weightedValves(inputs)  # get the inputs that work again
    shortestPath = shortestPaths(nonZero, inputs)

    # get all possible paths and their maximum flow. totally doesn't take forever ~ 400000 combinations???
    allPaths = everyMove(shortestPath, inputs, 26)

    result = max(flow1 + flow2 for path1, flow1 in allPaths.items() for path2, flow2 in allPaths.items() if not path1 & path2)
    print(f'Part 2: {result}')


part1()
part2()
