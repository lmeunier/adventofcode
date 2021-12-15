import math

with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


class Node:
    def __init__(self, coordinates, risk_level, visited=False, tentative_distance=math.inf):
        self.coordinates = coordinates
        self.risk_level = risk_level
        self.visited = False
        self.tentative_distance = tentative_distance


cave = {}

# create initial cave
for y, line in enumerate(lines):
    for x, risk_level in enumerate(line):
        cave[(x, y)] = Node((x, y), int(risk_level))

start = cave[(0, 0)]
start.tentative_distance = 0
destination = cave[(max([x for (x, y) in cave.keys()]),
                    max([y for (x, y) in cave.keys()]))]


def dijkstra(start_node):
    unvisited_nodes = [node for node in cave.values()]
    current_node = start_node
    while True:
        unvisited_neighbors = [node for node in [
            cave.get((current_node.coordinates[0] + 1, current_node.coordinates[1])),
            cave.get((current_node.coordinates[0] - 1, current_node.coordinates[1])),
            cave.get((current_node.coordinates[0], current_node.coordinates[1] + 1)),
            cave.get((current_node.coordinates[0], current_node.coordinates[1] - 1)),
        ] if node and not node.visited]

        for node in unvisited_neighbors:
            tentative_distance = current_node.tentative_distance + node.risk_level
            node.tentative_distance = min(tentative_distance, node.tentative_distance)

        current_node.visited = True
        unvisited_nodes.remove(current_node)

        if len(unvisited_nodes) == 0:
            break

        current_node = min(unvisited_nodes, key=lambda x: x.tentative_distance)

dijkstra(start)
print(destination.tentative_distance)
