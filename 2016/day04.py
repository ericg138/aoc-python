import collections

with open("input/day04.txt") as file:
    input = file.read().splitlines()


def part1():
    result = 0

    for line in input:

        # Build map of occurences per letter ordered alphabetically
        ordered_name = sorted(line[:-10].replace("-", ""))
        ordered_map = collections.OrderedDict()
        for letter in ordered_name:
            ordered_map[letter] = ordered_map.get(letter, 0) + 1

        # List of keys from the map ordered by value desc
        ordered_keys = sorted(ordered_map, key=ordered_map.get, reverse=True)

        expectedChecksum = line[-6:-1]
        if "".join(ordered_keys[:5]) == expectedChecksum:
            id = int(line[-10:-7])
            result += id

    return result


def part2():

    for line in input:
        decrypted_name = ""
        id = int(line[-10:-7])

        for letter in line[:-10].replace("-", ""):
            letter_index = ord(letter) - 97
            new_letter_index = (letter_index + id) % 26
            decrypted_name += chr(new_letter_index + 97)

        if decrypted_name == "northpoleobjectstorage":
            return id


print(part1())
print(part2())
