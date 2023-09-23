with open("input/day01.txt") as file:
    input = file.read()

directions = {0: "NORTH", 1: "EAST", 2: "SOUTH", 3: "WEST"}


def exec():
    x = 0
    y = 0
    direction = 0
    visited = [(0, 0)]
    part2 = None

    for instruction in input.replace(" ", "").split(","):

        if instruction[0] == "R":
            direction = (direction + 1) % 4
        elif instruction[0] == "L":
            direction = (direction - 1) % 4

        steps = int(instruction[1:])
        direction_str = directions.get(direction)

        for _ in range(0, steps):
            if direction_str == "NORTH":
                y += 1
            elif direction_str == "SOUTH":
                y -= 1
            elif direction_str == "EAST":
                x += 1
            elif direction_str == "WEST":
                x -= 1

            if part2 == None:
                if (x, y) in visited:
                    part2 = abs(x) + abs(y)
                else:
                    visited.append((x, y))

    part1 = abs(x) + abs(y)

    print(part1)
    print(part2)


exec()
