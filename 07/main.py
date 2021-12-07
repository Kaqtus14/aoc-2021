def get_spent_fuel(i, data):
    fuel = 0

    for d in data:
        if d < i:
            for j in range(1, i - d + 1):
                fuel += j
        elif d > i:
            for j in range(1, d - i + 1):
                fuel += j
    return fuel


with open("input.txt") as f:
    data = [int(x) for x in f.read().split(",")]

i = int(sum(data) / len(data))
fuel = get_spent_fuel(i, data)
print(fuel)
