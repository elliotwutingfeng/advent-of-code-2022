import typing

with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

tree: dict[str, typing.Any] = {"/": {}}
dir_to_contents: dict[str, list[typing.Any]] = {"/": []}

current = tree
current_path = "/"


def get_path_above(current_path):
    if current_path == "/":
        return "/"
    new_path = "/" + "/".join(current_path.strip("/").split("/")[:-1]) + "/"
    if new_path == "//":
        return "/"
    return new_path


assert get_path_above("/") == "/"
assert get_path_above("/a/") == "/"
assert get_path_above("/a/b/") == "/a/"
assert get_path_above("/a/b/c/") == "/a/b/"


def get_path_into(current_path, directory_to_move_into):
    if directory_to_move_into == "/":
        return "/"
    new_path = current_path + directory_to_move_into + "/"
    return new_path


assert get_path_into("/", "/") == "/"
assert get_path_into("/", "a") == "/a/"
assert get_path_into("/a/", "b") == "/a/b/"
assert get_path_into("/a/b/", "c") == "/a/b/c/"


def move_into_path(current_path):
    current = tree
    if current_path == "/":
        return current["/"]
    for node in current_path.strip("/").split("/"):
        if node not in current:
            current[node] = {}
        current = current[node]
    return current


row_idx = 0
while row_idx < len(lines):
    line = lines[row_idx]
    if line.startswith("$ cd .."):
        current_path = get_path_above(current_path)
        current = move_into_path(current_path)
        row_idx += 1
    elif line.startswith("$ cd "):
        directory_to_move_into = line.removeprefix("$ cd ")
        current_path = get_path_into(current_path, directory_to_move_into)
        current = move_into_path(current_path)
        if current_path not in dir_to_contents:
            dir_to_contents[current_path] = []
        row_idx += 1
    elif line.startswith("$ ls"):
        while True:
            row_idx += 1
            if row_idx == len(lines):
                break
            line = lines[row_idx]
            if line.startswith("$ "):
                break
            dir_to_contents[current_path].append(tuple(line.split(" ")))


def get_dir_size(path_to_dir):
    inner_dir_paths = [
        path_to_dir + x[1] + "/" for x in dir_to_contents[path_to_dir] if x[0] == "dir"
    ]
    return sum([int(x[0]) for x in dir_to_contents[path_to_dir] if x[0] != "dir"]) + sum(
        get_dir_size(p) for p in inner_dir_paths
    )


total = 0
for path in dir_to_contents:
    dir_size = get_dir_size(path)
    if dir_size <= 100_000:
        total += dir_size
print(total)
