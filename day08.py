with open("input/day08.txt") as file:
    input = file.read()

input_list = list(input)
layers = []

while input_list:
    layer = []
    for _ in range(6):
        row = []
        for __ in range(25):
            row.append(input_list.pop(0))
        layer.append(row)
    layers.append(layer)


def part1():
    min_0 = None
    min_layer = None

    for layer in layers:
        layer_count = 0
        for row in layer:
            layer_count += row.count("0")
        if min_0 is None or layer_count < min_0:
            min_0 = layer_count
            min_layer = layer

    digits_1 = 0
    digits_2 = 0
    for row in min_layer:
        digits_1 += row.count("1")
        digits_2 += row.count("2")

    print(digits_1 * digits_2)


def part2():
    image = []

    for y in range(6):
        image_row = []
        for x in range(25):
            for layer in layers:
                if layer[y][x] != "2":
                    image_row.append(layer[y][x])
                    break
        image.append(image_row)

    for row in image:
        print("".join(row).replace("1", "#").replace("0", "."))


part1()
part2()
