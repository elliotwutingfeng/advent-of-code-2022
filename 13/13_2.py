import functools
import json

with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

signals = []
for line in lines:
    signals.append(json.loads(line))


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


signals += [[[2]], [[6]]]
signals = sorted(signals, key=functools.cmp_to_key(compare), reverse=True)


indices = []
for (idx, signal) in enumerate(signals):
    if signal == [[2]] or signal == [[6]]:
        indices.append(idx + 1)
print(indices[0] * indices[1])
