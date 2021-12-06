with open("input", "r") as f:
    lines = f.readlines()

fishes = {n: 0 for n in range(9)}

for n in map(int, lines[0].strip().split(",")):
    fishes[n] += 1

for d in range(256):
    prev = dict(fishes)
    for i in range(9):
        if i == 8:
            fishes[6] += prev[0]
            fishes[8] = prev[0]
        else:
            fishes[i] = prev[i+1]

print(sum(fishes.values()))
