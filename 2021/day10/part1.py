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
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def score_for_line(line):
    stack = []
    for c in line:
        if c in open_chars:
            stack.append(c)
        elif c in close_chars:
            last_c = stack.pop()
            if open_to_close[last_c] != c:
                return points_by_char[c]
    return 0


score = 0
for line in lines:
    score += score_for_line(line.strip())

print(score)
