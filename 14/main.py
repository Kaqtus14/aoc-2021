from collections import Counter


def add(template, key, amount):
    if key not in template:
        template[key] = 0
    template[key] += amount
    return template


def flatten_template(template):
    flat = {}
    for k, v in template.items():
        flat = add(flat, k[0], v)
    return flat


def step(template, pairs):
    new = {}

    for k, v in template.items():
        if tuple(k) in pairs:
            n = pairs[tuple(k)]
            new = add(new, k[0]+n, v)
            new = add(new, n+k[1], v)
        else:
            new = add(new, k, v)

    return new


with open("input.txt") as f:
    parts = f.read().split("\n\n")

    template = {}
    temp = parts[0]
    for i in range(len(temp)-1):
        l = temp[i]+temp[i+1]
        template = add(template, l, 1)

    pairs = {}
    for line in parts[1].split("\n"):
        s = line.split(" -> ")
        pairs[tuple(s[0])] = s[1]


for _ in range(40):
    template = step(template, pairs)

template = flatten_template(template)
d = sorted(dict(Counter(template)).values())
res = d[-1]-d[0]-2
print(res)
