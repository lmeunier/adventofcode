with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]

ones_count = [0] * len(lines[0])

for line in lines:
    for i, bit in enumerate(line):
        if bit == "1":
            ones_count[i] += 1

gamma = 0b0
for i, count in enumerate(reversed(ones_count)):
    if count > len(lines) / 2:
        gamma = gamma | (1<<i)

epsilon = gamma ^ (2 ** len(ones_count) - 1)

print(gamma * epsilon)
