LENGTH = 12

with open("input.txt") as f:
    data = f.read().strip().split("\n")

gamma = ""
epsilon = ""
for i in range(LENGTH):
    zeros = 0
    ones = 0
    for l in data:
        if l[i] == "1":
            ones += 1
        else:
            zeros += 1

    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))
