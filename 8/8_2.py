with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

arr = [[int(x) for x in line] for line in lines]

scores: dict[tuple[int, int], int] = dict()

for x in range(len(arr)):
    for y in range(len(arr[0])):
        top, bottom, left, right = 0, 0, 0, 0
        # top
        for i in range(x - 1, -1, -1):
            top += 1
            if arr[i][y] >= arr[x][y]:
                break
        # bottom
        for i in range(x + 1, len(arr)):
            bottom += 1
            if arr[i][y] >= arr[x][y]:
                break
        # left
        for i in range(y - 1, -1, -1):
            left += 1
            if arr[x][i] >= arr[x][y]:
                break
        # right
        for i in range(y + 1, len(arr[0])):
            right += 1
            if arr[x][i] >= arr[x][y]:
                break
        scores[(x, y)] = max(1, top) * max(1, left) * max(1, bottom) * max(1, right)

print(max(scores.values()))
