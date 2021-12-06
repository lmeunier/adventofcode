with open("input", "r") as f:
    lines = f.readlines()

fishes = list(map(int, lines[0].strip().split(",")))

for d in range(80):
    for i, fish in list(enumerate(fishes)):
        if fish == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1

print(len(fishes))
