with open("input/day02.txt") as file:
    input = file.read().splitlines()


def part1():
    position = 5
    result = ""

    for line in input:
        for instruction in line:

            if instruction == "U" and position > 3:
                position -= 3
            elif instruction == "D" and position < 7:
                position += 3
            elif instruction == "R" and position % 3 != 0:
                position += 1
            elif instruction == "L" and position % 3 != 1:
                position -= 1

        result += str(position)

    return result


def part2():
    position = 5
    result = ""

    for line in input:
        for instruction in line:

            if instruction == "U" and position not in [5, 2, 1, 4, 9]:
                if position == 3 or position == 13:
                    position -= 2
                else:
                    position -= 4
            elif instruction == "D" and position not in [5, 10, 13, 12, 9]:
                if position == 11 or position == 1:
                    position += 2
                else:
                    position += 4
            elif instruction == "R" and position not in [1, 4, 9, 12, 13]:
                position += 1
            elif instruction == "L" and position not in [1, 2, 5, 10, 13]:
                position -= 1

        result += hex(position)[2:3].upper()

    return result


print(part1())
print(part2())
