with open("input", "r") as f:
    lines = f.readlines()

increased = 0
previous = None
for i in range(len(lines) - 2):
    value = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if not previous:
        previous = value
    if previous < value:
        increased += 1
    previous = value

print(increased)
