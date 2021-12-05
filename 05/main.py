SIZE = 1000


def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end="")
        print()


with open("input.txt") as f:
    lines = []

    for line in f.read().strip().split("\n"):
        line = line.replace(" -> ", ",")
        s = tuple([int(x) for x in line.split(",")])
        lines.append(s)

grid = []
for _ in range(SIZE):
    grid.append([0] * SIZE)

for l in lines:
    print(l)
    if l[0] != l[2] and l[1] == l[3]:
        step = 1 if l[2] > l[0] else -1
        for i in range(l[0], l[2]+step, step):
            grid[l[1]][i] += 1

    elif l[1] != l[3] and l[0] == l[2]:
        step = 1 if l[3] > l[1] else -1
        for i in range(l[1], l[3]+step, step):
            grid[i][l[0]] += 1

    else:
        stepx = 1 if l[3] > l[1] else -1
        stepy = 1 if l[2] > l[0] else -1

        x = l[1]
        y = l[0]
        while True:
            if x == l[3] and y == l[2]:
                grid[x][y] += 1
                break
            grid[x][y] += 1
            x += stepx
            y += stepy

    # print_grid(grid)
    # print()

out = 0
for row in grid:
    for cell in row:
        if cell >= 2:
            out += 1

print(out)
