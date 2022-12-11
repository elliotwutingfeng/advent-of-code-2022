with open("input.txt", "r") as f:
    lines = [line for line in f.read().split("\n") if line != ""]


class Monkey:
    def __init__(self, ID, starting_items, operand, modifier, divisor, true_ID, false_ID):
        self.ID = ID
        self.starting_items = starting_items
        self.operand = operand
        self.modifier = modifier
        self.divisor = divisor
        self.true_ID = true_ID
        self.false_ID = false_ID

        self.inspect_count = 0


monkeys: dict[int, Monkey] = dict()

idx = 0
while idx in range(len(lines)):
    if lines[idx].startswith("Monkey "):
        ID = int(lines[idx].split(" ")[1].strip(":"))
        starting_items = [int(x) for x in lines[idx + 1].split(": ")[1].split(", ")]
        operand = lines[idx + 2][23]
        modifier: int | str = 0
        if lines[idx + 2][25:] == "old":
            modifier = "old"
        else:
            modifier = int(lines[idx + 2][25:])
        divisor = int(lines[idx + 3][21:])
        true_ID = int(lines[idx + 4][29:])
        false_ID = int(lines[idx + 5][29:])
        monkeys[ID] = Monkey(ID, starting_items, operand, modifier, divisor, true_ID, false_ID)
        idx += 6
import math

rounds_completed = 0
current_monkey_id = 0
product_of_all_divisors = math.prod(monkey.divisor for monkey in monkeys.values())
while rounds_completed < 10_000:
    monkey = monkeys[current_monkey_id]
    while monkey.starting_items:
        worry_level = monkey.starting_items[0]
        if monkey.modifier == "old":
            worry_level = worry_level * worry_level
        else:
            if monkey.operand == "+":
                worry_level += monkey.modifier
            if monkey.operand == "*":
                worry_level *= monkey.modifier
        worry_level %= product_of_all_divisors
        target_id = monkey.true_ID if worry_level % monkey.divisor == 0 else monkey.false_ID
        monkey.starting_items.pop(0)
        monkey.inspect_count += 1
        monkeys[target_id].starting_items.append(worry_level)
    current_monkey_id += 1
    if current_monkey_id == len(monkeys):
        current_monkey_id = 0
        rounds_completed += 1


top_2 = sorted([monkey.inspect_count for monkey in monkeys.values()])[-2:]
print(top_2[0] * top_2[1])
