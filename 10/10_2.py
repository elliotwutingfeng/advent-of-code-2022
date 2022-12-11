with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]

signals = []
X = 1
cycle = 0
for line in lines:
    cycle += 1
    signals.append(X)
    if line != "noop":
        cycle += 1
        signals.append(X)
        val = int(line.split(" ")[1])
        X += val

output = ""
for idx, signal in enumerate(signals):
    col = idx % 40
    if col in range(signal - 1, signal + 2):
        output += "#"
    else:
        output += " "
    if (idx + 1) % 40 == 0:
        output += "\n"
print(output)

# Answer for this input: PBZGRAZA
