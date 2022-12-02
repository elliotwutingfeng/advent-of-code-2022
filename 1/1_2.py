with open("input.txt", "r") as f:
    lines = f.read().split("\n")

numbers = []
x = 0
for d in lines:
    if d == "":
        numbers.append(x)
        x = 0
    else:
        x += int(d)
top_3 = sum(sorted(numbers)[-3:])
print(top_3)
