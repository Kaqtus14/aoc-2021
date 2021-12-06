def day(fish):
    new = {i: 0 for i in range(9)}

    for k in fish:
        if k == 0:
            new[6] += fish[k]
            new[8] += fish[k]
        else:
            new[k - 1] += fish[k]
    return new


with open("input.txt") as f:
    data = [int(x) for x in f.read().split(",")]
    fish = {i: 0 for i in range(9)}
    for f in data:
        fish[f] += 1

for i in range(256):
    fish = day(fish)
print(i, sum(fish.values()))
