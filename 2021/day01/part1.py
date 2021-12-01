with open("input", "r") as f:
    lines = f.readlines()

increased = 0
previous = None
for line in lines:
    line = line.strip()
    if not line:
        continue
    value = int(line)
    if not previous:
        previous = value
        continue
    if previous < value:
        increased += 1
    previous = value

print(increased)
