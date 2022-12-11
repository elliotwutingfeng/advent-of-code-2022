with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

signals = []
X = 1
cycle = 1
for line in lines:
    cycle += 1
    if (cycle - 20) % 40 == 0:
        signals.append(cycle * X)
    if line != "noop":
        val = int(line.split(" ")[1])
        # print(val)
        X += val
        cycle += 1
        if (cycle - 20) % 40 == 0:
            signals.append(cycle * X)
print(sum(signals[:6]))
