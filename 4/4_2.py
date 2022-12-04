with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

count = 0
for line in lines:
    pair1, pair2 = tuple(line.split(","))
    p1_min, p1_max = tuple(int(i) for i in pair1.split("-"))
    p2_min, p2_max = tuple(int(i) for i in pair2.split("-"))
    if (p2_min <= p1_min <= p2_max) or (p1_min <= p2_min <= p1_max):
        count += 1
print(count)
