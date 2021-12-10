import statistics


BRACKETS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def process_line(line):
    opened = []

    for c in line:
        if c in BRACKETS:
            opened.append(BRACKETS[c])
        else:
            if opened.pop() != c:
                return None
    return opened


with open("input.txt") as f:
    lines = f.read().split("\n")

scores = []
for line in lines:
    res = process_line(line)
    if not res:
        continue

    temp = 0
    for b in res[::-1]:
        temp *= 5
        temp += SCORES[b]
    scores.append(temp)

print(statistics.median(scores))
