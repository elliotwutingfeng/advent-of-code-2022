with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]


def back_move_where(front, back):
    front_x, front_y = front
    back_x, back_y = back

    if back_x + 2 == front_x:
        back_x += 1
        if front_y > back_y:
            back_y += 1
        elif front_y < back_y:
            back_y -= 1

    elif back_y + 2 == front_y:
        back_y += 1
        if front_x > back_x:
            back_x += 1
        elif front_x < back_x:
            back_x -= 1

    elif back_x - 2 == front_x:
        back_x -= 1
        if front_y > back_y:
            back_y += 1
        elif front_y < back_y:
            back_y -= 1

    elif back_y - 2 == front_y:
        back_y -= 1
        if front_x > back_x:
            back_x += 1
        elif front_x < back_x:
            back_x -= 1

    return back_x, back_y


coords: set[tuple[int, int]] = set([(0, 0)])


current_coords = [(0, 0) for _ in range(10)]
for line in lines:
    direction = line.split(" ")[0]
    step_size = int(line.split(" ")[1])
    step_unit = -1 if direction in ("D", "L") else 1
    for _ in range(step_size):
        current_coords[0] = (
            current_coords[0][0] + (0 if direction in ("U", "D") else step_unit),
            current_coords[0][1] + (0 if direction in ("L", "R") else step_unit),
        )
        for i in range(9):
            current_coords[i + 1] = back_move_where(current_coords[i], current_coords[i + 1])
            if i == 8:
                coords.add(current_coords[i + 1])

print(len(coords))
