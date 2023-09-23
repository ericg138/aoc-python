import re

with open("input/day08.txt") as file:
    input = file.read().splitlines()


def rotate(string, size):
    for _ in range(size):
        last = string.pop()
        string.insert(0, last)


def print_grid(grid):
    for row in grid:
        print("".join(row))


def exec():
    grid = []
    grid_height = 6
    grid_width = 50
    rect_pattern = re.compile(r"rect (\d+)x(\d+)")
    rotate_pattern = re.compile(r"rotate .* [xy]=(\d+) by (\d+)")

    for _ in range(grid_height):
        row = ["."] * grid_width
        grid.append(row)

    for line in input:

        if line.startswith("rect"):
            m = rect_pattern.match(line)
            rect_width = int(m.group(1))
            rect_height = int(m.group(2))

            for i in range(rect_height):
                for j in range(rect_width):
                    grid[i][j] = "#"

        if line.startswith("rotate row"):
            m = rotate_pattern.match(line)
            y = int(m.group(1))
            size = int(m.group(2))

            row = grid[y]
            rotate(row, size)
            grid[y] = row

        if line.startswith("rotate column"):
            m = rotate_pattern.match(line)
            x = int(m.group(1))
            size = int(m.group(2))

            column = [None] * grid_height
            for i in range(grid_height):
                column[i] = grid[i][x]

            rotate(column, size)

            for i in range(grid_height):
                grid[i][x] = column[i]

    print_grid(grid)

    on = 0
    for row in grid:
        on += len("".join(row).replace(".", ""))
    return on


print(exec())
