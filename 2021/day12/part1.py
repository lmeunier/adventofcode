with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


class Node:
    def __init__(self, name):
        self.name = name
        self.is_visited = False
        self.connected_nodes = set()

    def is_visitable(self):
        return self.name.isupper() or not self.is_visited


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
    node.is_visited = True

    if node.name == "end":
        paths.append(path.copy())
        return

    for connected_node in node.connected_nodes:
        if connected_node.is_visitable():
            visite_node(connected_node, path)
            connected_node.is_visited = False
            path.pop()


paths = []
visite_node(nodes.get("start"), [])

print(len(paths))
