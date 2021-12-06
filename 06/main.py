def day(fish):
    new = []

    for f in fish:
        if f == 0:
            new.append(6)
            new.append(8)
        else:
            new.append(f - 1)
    return new


with open("input.txt") as f:
    fish = [int(x) for x in f.read().split(",")]

for i in range(256):
    fish = day(fish)
    print(i, len(fish))
