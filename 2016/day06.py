with open("input/day06.txt") as file:
    input = file.read().splitlines()


def exec():
    part1 = ""
    part2 = ""

    for i in range(8):
        map = {}

        for line in input:
            letter = line[i]
            map[letter] = map.get(letter, 0) + 1

        part1 += max(map, key=map.get)
        part2 += min(map, key=map.get)

    return part1 + " - " + part2


print(exec())
