from collections import Counter


def step(template, pairs):
    new = []

    for i in range(len(template)-1):
        t = (template[i], template[i+1])

        new.append(template[i])
        if t in pairs:
            new.append(pairs[t])

    new.append(template[i+1])
    return new


with open("input.txt") as f:
    parts = f.read().split("\n\n")

    template = parts[0]

    pairs = {}
    for line in parts[1].split("\n"):
        s = line.split(" -> ")
        pairs[tuple(s[0])] = s[1]


for _ in range(10):
    template = step(template, pairs)

d = sorted(dict(Counter(template)).values())
print(d[-1]-d[0])
