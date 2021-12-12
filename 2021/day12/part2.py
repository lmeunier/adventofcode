from collections import Counter

with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


class Node:
    def __init__(self, name):
        self.name = name
        self.is_visited_count = 0
        self.connected_nodes = set()

    def is_visitable(self, path):
        if self.name == "start":
            return False

        if self.name.isupper():
            return True

        if self.is_visited_count == 0:
            return True

        small_cave_already_visited_twice = 2 in [
            v for n, v in Counter(path).items() if n.name.islower()
        ]
        return not small_cave_already_visited_twice


nodes = {}
for f, t in [line.split("-") for line in lines]:
    node_from = nodes.get(f, Node(f))
    node_to = nodes.get(t, Node(t))

    nodes[f] = node_from
    nodes[t] = node_to

    node_from.connected_nodes.add(node_to)
    node_to.connected_nodes.add(node_from)


def visite_node(node, path):
    path.append(node)
    node.is_visited_count += 1

    if node.name == "end":
        paths.append(path.copy())
        return

    for connected_node in node.connected_nodes:
        if connected_node.is_visitable(path):
            visite_node(connected_node, path)
            connected_node.is_visited_count -= 1
            path.pop()


paths = []
visite_node(nodes.get("start"), [])

print(len(paths))
