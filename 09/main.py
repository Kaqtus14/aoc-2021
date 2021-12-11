def check(data, x, y):
    if x > 0 and data[x-1][y] <= data[x][y]:
        return None
    if x < len(data)-1 and data[x+1][y] <= data[x][y]:
        return None
    if y > 0 and data[x][y-1] <= data[x][y]:
        return None
    if y < len(data[0])-1 and data[x][y+1] <= data[x][y]:
        return None
    return data[x][y] + 1


with open("input.txt") as f:
    data = [[int(c) for c in line]
            for line in f.read().split("\n")]


out = 0
for x in range(len(data)):
    for y in range(len(data[0])):
        c = check(data, x, y)
        if c is not None:
            out += c

print(out)
