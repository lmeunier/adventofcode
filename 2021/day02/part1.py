with open("input", "r") as f:
    lines = f.readlines()

hpos = 0
depth = 0

for line in lines:
    line = line.strip()
    if not line:
        continue

    command, value = line.split(" ")
    value = int(value)
    if command == "forward":
        hpos += value
    elif command == "up":
        depth -= value
    elif command == "down":
        depth += value

print(hpos * depth)
