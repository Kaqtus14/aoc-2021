with open("input.txt") as f:
    data = [int(x) for x in f.read().strip().split("\n")]

larger = 0
for i in range(1, len(data)-1):
    if data[i-2] + data[i-1] + data[i] < data[i-1] + data[i] + data[i+1]:
        larger += 1

print(larger)
