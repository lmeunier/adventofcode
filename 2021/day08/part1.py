with open("input", "r") as f:
    lines = f.readlines()

count = 0
for line in lines:
    digits = line.split("|")[1].strip().split(" ")
    for digit in digits:
        if len(digit) in [2, 4, 3, 7]:
            count += 1

print(count)
