with open("input", "r") as f:
    lines = f.readlines()

hm = {}
max_x = len(lines)
max_y = len(lines[0].strip())

for x, line in enumerate(lines):
    for y, height in enumerate(line.strip()):
        hm[(x, y)] = int(height)

risk_level = 0
for x in range(max_x):
    for y in range(max_y):
        h = hm.get((x, y))

        if h < hm.get((x-1, y), 10) and h < hm.get((x+1, y), 10) and h < hm.get((x, y-1), 10) and h < hm.get((x, y+1), 10):
            risk_level += h + 1

print(risk_level)
