with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

arr = [[int(x) for x in line] for line in lines]

total = 2 * len(arr) + 2 * len(arr[0]) - 4

counted: set[tuple[int, int]] = set()

for x in range(1, len(arr) - 1):
    record_holder = arr[x][0]
    for y in range(1, len(arr[0]) - 1):
        record_holder = max(record_holder, arr[x][y - 1])
        if record_holder < arr[x][y]:
            counted.add((x, y))
    record_holder = arr[x][len(arr[0]) - 1]
    for y in range(len(arr[0]) - 2, 0, -1):
        record_holder = max(record_holder, arr[x][y + 1])
        if record_holder < arr[x][y]:
            counted.add((x, y))

for y in range(1, len(arr[0]) - 1):
    record_holder = arr[0][y]
    for x in range(1, len(arr) - 1):
        record_holder = max(record_holder, arr[x - 1][y])
        if record_holder < arr[x][y]:
            counted.add((x, y))
    record_holder = arr[len(arr) - 1][y]
    for x in range(len(arr) - 2, 0, -1):
        record_holder = max(record_holder, arr[x + 1][y])
        if record_holder < arr[x][y]:
            counted.add((x, y))

print(total + len(counted))
