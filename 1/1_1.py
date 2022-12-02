with open("input.txt", "r") as f:
    lines = f.read().split("\n")

x = 0
largest = 0
for d in lines:
    if d == "":
        largest = max(x, largest)
        x = 0
    else:
        x += int(d)
print(largest)
