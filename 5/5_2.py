with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

for idx, line in enumerate(lines):
    if "move" in line:
        number_of_columns = int(lines[idx - 1].strip().split("   ")[-1])
        instruction_start_row_idx = idx
        break

# Load up initial grid
grid: list[list] = [list() for _ in range(number_of_columns)]
for line in lines[: instruction_start_row_idx - 1]:
    elems = [line[x] for x in range(1, len(line), 4)]
    for idx, elem in enumerate(elems):
        if elem != " ":
            grid[idx].insert(0, elem)

# for col in grid:
#     print(col)
# print("")
for line in lines[instruction_start_row_idx:]:
    qty, source, destination = tuple(
        int(x) for x in line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
    )
    grid[destination - 1] += grid[source - 1][-qty:]  # not reversed for anti stack-like behavior
    grid[source - 1] = grid[source - 1][:-qty]
    # for col in grid:
    #     print(col)
    # print("")

print("".join(col[-1] for col in grid if col))
