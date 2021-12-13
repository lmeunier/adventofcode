with open("input", "r") as f:
    lines = f.readlines()


dots = []
folds = []
dots_list_finished = False
for line in lines:
    line = line.strip()
    if not line:
        # empty line between list of dots and fold instructions
        dots_list_finished = True
        continue

    if not dots_list_finished:
        x, y = line.split(",")
        dots.append((int(x), int(y)))
    else:
        direction, line_number = line.strip("fold along ").split("=")
        folds.append((direction, int(line_number)))


def fold_paper(dots, horizontal, line_number):
    new_dots = []
    if horizontal:
        # fold along y
        for x, y in dots:
            if y > line_number:
                y = line_number - (y - line_number)
            new_dots.append((x, y))
    else:
        # fold along x
        for x, y in dots:
            if x > line_number:
                x = line_number - (x - line_number)
            new_dots.append((x, y))

    return set(new_dots)


def print_dots(dots):
    max_x = max([x for x, y in dots])
    max_y = max([y for x, y in dots])

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in dots:
                print("#", end="")
            else:
                print(" ", end="")
        print("")


for fold in folds:
    dots = fold_paper(dots, fold[0] == "y", fold[1])

print_dots(dots)
