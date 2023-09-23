with open("input/day07.txt") as file:
    input = file.read().splitlines()


def has_abba(sequences):
    for seq in sequences:
        for i in range(1, len(seq) - 2):
            if (
                seq[i] == seq[i + 1]
                and seq[i - 1] == seq[i + 2]
                and seq[i - 1] != seq[i]
            ):
                return True
    return False


def has_ssl(supernets, hypernets):
    for supernet in supernets:
        for i in range(1, len(supernet) - 1):
            if supernet[i] != supernet[i + 1] and supernet[i - 1] == supernet[i + 1]:
                bab = supernet[i] + supernet[i - 1] + supernet[i]
                for hypernet in hypernets:
                    if bab in hypernet:
                        return True
    return False


def exec():
    part1 = 0
    part2 = 0

    for line in input:
        supernets = []
        hypernets = []

        while "[" in line:
            supernets.append(line[: line.index("[")])
            hypernets.append(line[line.index("[") + 1 : line.index("]")])
            line = line[line.index("]") + 1 :]

        supernets.append(line)

        if has_abba(supernets) and not has_abba(hypernets):
            part1 += 1

        if has_ssl(supernets, hypernets):
            part2 += 1

    return str(part1) + " - " + str(part2)


print(exec())
