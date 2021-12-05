import re

with open("input", "r") as f:
    lines = f.readlines()

line_regexp = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")
diagram = {}
for line in lines:
    matches = line_regexp.search(line)
    x1, y1, x2, y2 = map(int, matches.groups())

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            count = diagram.get((x1, y), 0)
            diagram[(x1, y)] = count + 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            count = diagram.get((x, y1), 0)
            diagram[(x, y1)] = count + 1
    else:
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        for i, x in enumerate(range(x1, x2 + x_step, x_step)):
            point = (x, y1 + y_step * i)
            count = diagram.get(point, 0)
            diagram[point] = count + 1

print(len([c for c in diagram.values() if c >= 2]))
