import json

with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

pairs = []
pair = []
for line in lines:
    pair.append(json.loads(line))
    if len(pair) == 2:
        pairs.append(pair)
        pair = []


def compare(left_arr, right_arr):
    if type(left_arr) is int and type(right_arr) is list:
        left_arr = [left_arr]
    if type(right_arr) is int and type(left_arr) is list:
        right_arr = [right_arr]
    if type(left_arr) is int and type(right_arr) is int:
        if left_arr == right_arr:
            return 0
        return 1 if left_arr < right_arr else -1

    x = 0
    while x < len(left_arr) and x < len(right_arr):
        res = compare(left_arr[x], right_arr[x])
        if res == 1:
            return 1
        if res == -1:
            return -1
        x += 1
    if x == len(left_arr):
        if x == len(right_arr):
            return 0
        return 1
    if x == len(right_arr):
        return -1


assert compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == 1
assert compare([[1], [2, 3, 4]], [[1], 4]) == 1
assert compare([9], [[8, 7, 6]]) == -1
assert compare([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) == 1
assert compare([7, 7, 7, 7], [7, 7, 7]) == -1
assert compare([], [3]) == 1
assert compare([[[]]], [[]]) == -1
assert compare([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) == -1

s = 0
for (idx, (left, right)) in enumerate(pairs):
    if compare(left, right) == 1:
        s += idx + 1
print(s)
