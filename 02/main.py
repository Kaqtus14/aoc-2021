with open("input.txt") as f:
    data = []
    for x in f.read().strip().split("\n"):
        x = x.split(" ")
        data.append((x[0], int(x[1])))

position = 0
depth = 0
aim = 0

for c in data:
    if c[0] == "forward":
        position += c[1]
        depth += c[1] * aim
    elif c[0] == "down":
        aim += c[1]
    elif c[0] == "up":
        aim -= c[1]
    else:
        assert False, "unreachable"

print(position * depth)
