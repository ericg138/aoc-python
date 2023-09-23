import re

with open("input/day03.txt") as file:
    input = file.read().splitlines()


def part1():
    result = 0

    for line in input:
        sides = re.sub("\\s+", " ", line.strip()).split(" ")
        sides = list(map(int, sides))
        sides.sort()

        if sides[0] + sides[1] > sides[2]:
            result += 1

    return result


def part2():
    result = 0
    table = []

    for line in input:
        sides = re.sub("\\s+", " ", line.strip()).split(" ")
        sides = list(map(int, sides))
        table.append(sides)

    for column in range(3):
        for row in range(0, len(table), 3):
            sides = [table[row][column], table[row + 1][column], table[row + 2][column]]
            sides.sort()

            if sides[0] + sides[1] > sides[2]:
                result += 1

    return result


print(part1())
print(part2())
