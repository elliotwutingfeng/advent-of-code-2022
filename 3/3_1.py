with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

total = 0
for line in lines:
    first_half = line[: len(line) // 2]
    second_half = line[len(line) // 2 :]
    common = tuple(set(first_half).intersection(second_half))[0]
    if ord("A") <= ord(common) <= ord("Z"):
        total += ord(common) - 38
    else:
        total += ord(common) - 96
print(total)
