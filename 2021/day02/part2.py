with open("input", "r") as f:
    lines = f.readlines()

hpos = 0
depth = 0
aim = 0

for line in lines:
    line = line.strip()
    if not line:
        continue

    command, value = line.split(" ")
    value = int(value)
    if command == "forward":
        hpos += value
        depth += aim * value
    elif command == "up":
        aim -= value
    elif command == "down":
        aim += value

print(hpos * depth)
