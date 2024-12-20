# 938/984
# what even is networkx
import networkx as nx
with open("input.txt", "r") as f:
    G =  [list(line.strip()) for line in f]

R, C = len(G), len(G[0])
maze = nx.grid_2d_graph(R, C) # didnt know this was a thing until the refactor...
S = E = None
for r, row in enumerate(G):
    for c, cell in enumerate(row):
        if cell == 'S':
            S = (r, c)
        elif cell == 'E':
            E = (r, c)
        elif cell == "#":
            maze.remove_node((r, c))


target = nx.shortest_path_length(maze, S, E) - 100
start_distance = nx.single_source_shortest_path_length(maze, S)
end_distance = nx.single_source_shortest_path_length(maze, E)
wallless = nx.grid_2d_graph(R, C)


def find_cheats(max_steps):
    paths = 0
    for r, c in start_distance.keys():
            cheats = nx.single_source_shortest_path_length(wallless, (r, c), cutoff=max_steps) # returns every loc in 20 step radius

            for cheat_end, steps in cheats.items():
                if cheat_end not in end_distance:
                    continue
                paths += start_distance[(r, c)] + end_distance[cheat_end] + steps <= target

    return paths


print(f"Part 1: {find_cheats(2)}")
print(f"Part 2: {find_cheats(20)}")