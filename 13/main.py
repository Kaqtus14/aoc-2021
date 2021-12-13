def parse_input():
    with open("input.txt") as f:
        data = f.read().split("\n\n")

    dots = set([tuple([int(x) for x in line.split(",")])
                for line in data[0].split("\n")])

    folds = []
    for line in data[1].split("\n"):
        line = line.split(" ")[-1].split("=")
        folds.append((line[0], int(line[1])))

    return dots, folds


def fold(dots, fold):
    new_dots = set()
    if fold[0] == "x":
        for dot in dots:
            x = min(dot[0], 2*fold[1]-dot[0])
            new_dots.add((x, dot[1]))
    elif fold[0] == "y":
        for dot in dots:
            y = min(dot[1], 2*fold[1]-dot[1])
            new_dots.add((dot[0], y))
    else:
        assert False
    return new_dots


dots, folds = parse_input()
dots = fold(dots, folds[0])
print(len(dots))
