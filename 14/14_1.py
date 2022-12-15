with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

coords = []
instructions = []
for line in lines:
    line_coords = [(int(a.split(",")[0]), int(a.split(",")[1])) for a in line.split(" -> ")]
    coords += line_coords
    instructions.append(line_coords)
min_col, min_row = min(x[0] for x in coords), 0
max_col, max_row = max(x[0] for x in coords), max(x[1] for x in coords)
grid = [[0 for _ in range(max_col + 2)] for _ in range(max_row + 2)]
for instruction in instructions:
    i = instruction.copy()
    current = i.pop(0)
    next = i.pop(0)
    while True:
        if current[0] == next[0]:  # Same column
            col = current[0]
            start = current[1] if current[1] < next[1] else next[1]
            end = current[1] + 1 if current[1] >= next[1] else next[1] + 1
            for row in range(start, end):
                grid[row][col] = 1
        elif current[1] == next[1]:  # Same row
            row = current[1]
            start = current[0] if current[0] < next[0] else next[0]
            end = current[0] + 1 if current[0] >= next[0] else next[0] + 1
            for col in range(start, end):
                grid[row][col] = 1
        current = next
        if not i:
            break
        next = i.pop(0)

# for row in range(min_row, max_row + 1):
#     for col in range(min_col, max_col + 1):
#         print(grid[row][col], end="")
#     print()

# print(len(grid), len(grid[0]))

sand_count = 0
overflow = False
while not overflow:
    pos = 500, 0
    while True:
        down_coords = (pos[0], pos[1] + 1)
        down_left_coords = (pos[0] - 1, pos[1] + 1)
        down_right_coords = (pos[0] + 1, pos[1] + 1)
        # print(down_coords, down_left_coords, down_right_coords)
        # Attempt down
        if grid[down_coords[1]][down_coords[0]] == 0:
            pos = down_coords
        # Attempt down-left
        elif grid[down_left_coords[1]][down_left_coords[0]] == 0:
            pos = down_left_coords
        # Attempt down-right
        elif grid[down_right_coords[1]][down_right_coords[0]] == 0:
            pos = down_right_coords
        # Nowhere else to go
        else:
            grid[pos[1]][pos[0]] = 1
            break
        if not ((min_col <= pos[0] <= max_col) and (min_row <= pos[1] <= max_row)):
            overflow = True
            break
    if not overflow:
        sand_count += 1

print(sand_count)
