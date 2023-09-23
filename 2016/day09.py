import re

with open("input/day09.txt") as file:
    input = file.read()

marker_pattern = re.compile(r"(\d+)x(\d+)")


def part1():
    decompressed_line = ""

    i = 0
    while i < len(input):
        char = input[i]

        if char == "(":
            marker_end = input.index(")", i)
            m = marker_pattern.match(input[i + 1 : marker_end])
            compressed_data_length = int(m.group(1))
            repeat_count = int(m.group(2))

            i = marker_end + 1 + compressed_data_length
            compressed_data = input[marker_end + 1 : i]

            for _ in range(0, repeat_count):
                decompressed_line += compressed_data
        else:
            decompressed_line += char
            i += 1

    return len(decompressed_line)


def get_length(string):
    length = 0

    i = 0
    while i < len(string):
        char = string[i]

        if char == "(":
            marker_end = string.index(")", i)
            m = marker_pattern.match(string[i + 1 : marker_end])
            compressed_data_length = int(m.group(1))
            repeat_count = int(m.group(2))

            i = marker_end + 1 + compressed_data_length
            compressed_data = string[marker_end + 1 : i]
            length += repeat_count * get_length(compressed_data)
        else:
            length += 1
            i += 1

    return length


def part2():
    return get_length(input)


print(part1())
print(part2())
