import re

with open("input/day10.txt") as file:
    input = file.read().splitlines()


def exec():
    value_pattern = re.compile(r"value (\d+) goes to bot (\d+)")
    give_pattern = re.compile(
        r"bot (\d+) gives low to (?:bot|output) (\d+) and high to (?:bot|output) (\d+)"
    )

    bot_map = {}
    output_map = {}

    instructions = []
    for line in input:
        if line.startswith("value"):
            m = value_pattern.match(line)
            bot = int(m.group(2))
            value = int(m.group(1))
            bot_map.setdefault(bot, []).append(value)
        else:
            instructions.append(line)

    while len(instructions) != 0:
        remaining_instructions = []

        for line in instructions:
            m = give_pattern.match(line)
            bot = int(m.group(1))
            low_to = int(m.group(2))
            high_to = int(m.group(3))

            if bot not in bot_map or len(bot_map[bot]) < 2:
                remaining_instructions.append(line)
                continue

            low = min(bot_map[bot])
            high = max(bot_map[bot])
            del bot_map[bot]
            if low == 17 and high == 61:
                part1 = bot

            if "low to output" in line:
                output_map.setdefault(low_to, []).append(low)
            if "high to output" in line:
                output_map.setdefault(high_to, []).append(high)
            if "low to bot" in line:
                bot_map.setdefault(low_to, []).append(low)
            if "high to bot" in line:
                bot_map.setdefault(high_to, []).append(high)

        instructions = remaining_instructions

    part2 = output_map[0][0] * output_map[1][0] * output_map[2][0]
    return str(part1) + " - " + str(part2)


print(exec())
