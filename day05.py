import re

with open("input/day05.txt") as file:
    input = file.read()

instruction_pattern = re.compile(r"(\d)(\d)(\d)(\d{2})")

opcode_map = {
    1: "add",
    2: "multiply",
    3: "input",
    4: "output",
    5: "jump-if-true",
    6: "jump-if-false",
    7: "less than",
    8: "equals",
    99: "exit",
}


def run(input_value):
    memory = [int(x) for x in input.split(",")]

    pointer = 0
    while True:
        instruction = str(memory[pointer]).rjust(5, "0")
        m = instruction_pattern.match(instruction)
        opcode = m.group(4)
        mode_param1 = m.group(3)
        mode_param2 = m.group(2)
        function = opcode_map.get(int(opcode))

        if function == "exit":
            break

        # Param definition
        param1 = memory[pointer + 1]
        pointer += 2

        if function not in ("input", "output"):
            param2 = memory[pointer]
            pointer += 1

            param1_value = param1 if mode_param1 == "1" else memory[param1]
            param2_value = param2 if mode_param2 == "1" else memory[param2]

            if function not in ("jump-if-true", "jump-if-false"):
                param3 = memory[pointer]
                pointer += 1

        # Function processing
        if function == "add":
            memory[param3] = param1_value + param2_value

        elif function == "multiply":
            memory[param3] = param1_value * param2_value

        elif function == "less than":
            memory[param3] = 1 if param1_value < param2_value else 0

        elif function == "equals":
            memory[param3] = 1 if param1_value == param2_value else 0

        elif function == "jump-if-true":
            if param1_value != 0:
                pointer = param2_value

        elif function == "jump-if-false":
            if param1_value == 0:
                pointer = param2_value

        elif function == "input":
            memory[param1] = input_value

        elif function == "output":
            print(memory[param1])

    return memory[0]


def part1():
    return run(1)


def part2():
    return run(5)


part1()
part2()
