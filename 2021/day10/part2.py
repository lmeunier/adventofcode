with open("input", "r") as f:
    lines = f.readlines()

open_chars = "([{<"
close_chars = ")]}>"
open_to_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
points_by_char = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def is_corrupted(line):
    stack = []
    for c in line:
        if c in open_chars:
            stack.append(c)
        elif c in close_chars:
            last_c = stack.pop()
            if open_to_close[last_c] != c:
                return True
    return False


def get_missing_chars(line):
    stack = []
    for c in line:
        if c in open_chars:
            stack.append(c)
        elif c in close_chars:
            last_c = stack.pop()
    return reversed([open_to_close[c] for c in stack])


scores = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    if is_corrupted(line):
        continue

    score = 0
    missing_chars = get_missing_chars(line)
    for c in missing_chars:
        score *= 5
        score += points_by_char[c]
    scores.append(score)

print(sorted(scores)[int(len(scores) / 2)])
