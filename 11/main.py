import sys
sys.setrecursionlimit(9999)


def remove_flashed(data):
    flashed = 0

    for x in range(len(data)):
        for y in range(len(data)):
            if data[x][y] > 9:
                data[x][y] = 0
                flashed += 1

    return flashed


def increase_all(data):
    for x in range(len(data)):
        for y in range(len(data)):
            data[x][y] += 1


def print_grid(data):
    for x in range(len(data)):
        for y in range(len(data)):
            sys.stdout.write(str(data[x][y]))
        print()
    print()


def increase_adjecent(data,  x, y):
    for sx in range(-1, 2):
        for sy in range(-1, 2):
            if x+sx < len(data) and \
               x+sx > -1 and \
               y+sy < len(data) and \
               y+sy > -1:
                data[x+sx][y+sy] += 1


def flash(data, total_flashes=0, flashed=None):
    if not flashed:
        flashed = []
    flashes = 0

    for x in range(len(data)):
        for y in range(len(data)):
            if data[x][y] > 9 and (x, y) not in flashed:
                increase_adjecent(data, x, y)
                flashes += 1
                flashed.append((x, y))

    if flashes > 0:
        return flash(data, total_flashes+flashes, flashed)

    return total_flashes+flashes


with open("input.txt") as f:
    data = [[int(c) for c in line]
            for line in f.read().split("\n")]

found = False
flashes = 0
for i in range(1000):
    increase_all(data)
    count = flash(data)
    flashes += count

    flashed = remove_flashed(data)
    if flashed == 100 and not found:
        print("part 2:", i+1)
        found = True

print("part 1:", flashes)
