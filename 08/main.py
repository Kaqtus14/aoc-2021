with open("input.txt") as f:
    data = [tuple([[y for y in x.split(" ") if y]
            for x in l.split("|")])
            for l in f.read().split("\n")]

out = 0
for l in data:
    for x in l[1]:
        if len(x) in [2, 3, 4, 7]:
            out += 1

print(out)
