BRACKETS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "": 0,
}


def process_line(line: str) -> str:
    opened = []

    for c in line:
        if c in BRACKETS:
            opened.append(BRACKETS[c])
        else:
            if opened.pop() != c:
                return c
    return ""


with open("input.txt") as f:
    data = f.read().split("\n")

score = 0
for line in data:
    score += SCORES[process_line(line)]
print(score)
