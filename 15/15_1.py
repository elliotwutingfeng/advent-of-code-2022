from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

grid: defaultdict[int, list[tuple[int, int]]] = defaultdict(lambda: [])  # intervals for each row
beacons_per_row: dict[int, int] = defaultdict(lambda: 0)
beacons: set[tuple[int, int]] = set()


def merge_intervals(arr):
    arr = sorted(arr, key=lambda x: (x[0], x[1]))
    new_arr = []
    for curr in arr:
        if not new_arr:
            new_arr.append(curr)
            continue
        prev = new_arr[-1]
        if prev[1] < curr[0] - 1:
            # no overlap
            new_arr.append(curr)
        else:
            # overlap
            new_arr[-1] = prev[0], max(prev[1], curr[1])
    return new_arr


assert merge_intervals([(1, 2), (3, 4)]) == [(1, 4)]
assert merge_intervals([(1, 2), (2, 4)]) == [(1, 4)]
assert merge_intervals([(1, 6), (2, 4)]) == [(1, 6)]

for line in lines:
    (x1, y1, x2, y2) = (
        int(k)
        for k in line.replace("Sensor at x=", "")
        .replace(" y=", " ")
        .replace(": closest beacon is at x=", ", ")
        .split(", ")
    )

    sensor = x1, y1
    beacon = x2, y2
    beacons.add((x2, y2))

    manhattan_distance = abs(x2 - x1) + abs(y2 - y1)

    magic_row = 2000000
    if not (y1 - manhattan_distance <= magic_row <= y1 + manhattan_distance):
        continue
    elif magic_row <= y1:
        row_flank = max(0, abs(y1 - magic_row - manhattan_distance))
    else:
        row_flank = max(0, abs(magic_row - y1 - manhattan_distance))
    grid[magic_row].append((x1 - row_flank, x1 + row_flank))

intervals = merge_intervals(grid[magic_row])
for _, y in beacons:
    beacons_per_row[y] += 1

print(sum(i[1] - i[0] + 1 for i in intervals) - beacons_per_row[magic_row])
