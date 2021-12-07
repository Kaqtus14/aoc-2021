def get_spent_fuel(i, data):
    fuel = 0

    for d in data:
        if d < i:
            fuel += i - d
        elif d > i:
            fuel += d - i
    return fuel


with open("input.txt") as f:
    data = [int(x) for x in f.read().split(",")]

lowest = (-1, 999999)
for i in range(2000):
    fuel = get_spent_fuel(i, data)
    if fuel < lowest[1]:
        lowest = (i, fuel)

print(lowest)
