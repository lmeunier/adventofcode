from collections import deque

with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


class Node:
    def __init__(self, coordinates, risk_level):
        self.coordinates = coordinates
        self.risk_level = risk_level


cave = {}

# create initial cave
for y, line in enumerate(lines):
    for x, risk_level in enumerate(line):
        cave[(x, y)] = Node((x, y), int(risk_level))

max_x = max([x for (x, y) in cave.keys()])
max_y = max([y for (x, y) in cave.keys()])

# extend the cave five times
for shift_y in range(0, 5):
    for shift_x in range(0, 5):
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                node = cave[(x, y)]
                new_risk_level = node.risk_level + shift_y + shift_x
                new_node = Node(
                    (shift_x * (max_x + 1) + x, shift_y * (max_y + 1) + y),
                    9 if new_risk_level % 9 == 0 else new_risk_level % 9,
                )
                cave[new_node.coordinates] = new_node


start = cave[(0, 0)]
destination = cave[(max([x for (x, y) in cave.keys()]),
                    max([y for (x, y) in cave.keys()]))]


def dijkstra(start_node):
    queue = deque([start_node])
    distances = {start_node: 0}

    while queue:
        current_node = queue.popleft()

        neighbors = [node for node in [
            cave.get((current_node.coordinates[0] + 1, current_node.coordinates[1])),
            cave.get((current_node.coordinates[0] - 1, current_node.coordinates[1])),
            cave.get((current_node.coordinates[0], current_node.coordinates[1] + 1)),
            cave.get((current_node.coordinates[0], current_node.coordinates[1] - 1)),
        ] if node]

        for neighbor in neighbors:
            tentative_distance = distances[current_node] + neighbor.risk_level

            if neighbor not in distances or tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                queue.append(neighbor)
    return distances


print(dijkstra(start)[destination])
