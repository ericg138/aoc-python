import hashlib

input = "wtnhxymk"


def exec():
    part1 = ""
    part2 = [None] * 8
    index = 0

    while None in part2:
        hash = hashlib.md5((input + str(index)).encode("utf-8")).hexdigest()
        if hash.startswith("00000"):
            if len(part1) < 8:
                part1 += hash[5:6]

            position = int(hash[5:6], 16)
            if position < 8 and part2[position] == None:
                part2[position] = hash[6:7]

        index += 1

    return part1 + " - " + "".join(part2)


print(exec())
