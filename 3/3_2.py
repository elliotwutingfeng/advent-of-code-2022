with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

total = 0
for i in range(0, len(lines), 3):
    items = lines[i : i + 3]
    common = tuple(set.intersection(*[set(x) for x in items]))[0]
    if ord("A") <= ord(common) <= ord("Z"):
        total += ord(common) - 38
    else:
        total += ord(common) - 96
print(total)
