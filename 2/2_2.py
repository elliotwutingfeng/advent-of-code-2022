with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

lose = {"A": 3, "B": 1, "C": 2}
tie = {"A": 1, "B": 2, "C": 3}
win = {"A": 2, "B": 3, "C": 1}

score = 0
for line in lines:
    other, goal = line.split(" ")
    if goal == "X":
        d = lose
    if goal == "Y":
        score += 3
        d = tie
    if goal == "Z":
        score += 6
        d = win
    score += d[other]
print(score)
