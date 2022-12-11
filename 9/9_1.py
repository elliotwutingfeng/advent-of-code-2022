with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]


def tail_still_with_head(head, tail):
    return abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1


coords: set[tuple[int, int]] = set([(0, 0)])


previous_coord = (0, 0)
tail = (0, 0)
current_coord = (0, 0)
for line in lines:
    direction = line.split(" ")[0]
    step_size = int(line.split(" ")[1])
    step_unit = -1 if direction in ("D", "L") else 1
    for _ in range(step_size):
        current_coord = (
            current_coord[0] + (0 if direction in ("U", "D") else step_unit),
            current_coord[1] + (0 if direction in ("L", "R") else step_unit),
        )
        if not tail_still_with_head(current_coord, tail):
            coords.add(previous_coord)
            tail = previous_coord
        previous_coord = current_coord

print(len(coords))
