import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    grid = []
    max_x = max_y = 0
    low_points = []

    for row in content:
        line = []
        for num in row:
            line.append(int(num))
        grid.append(line)

    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            is_lowpoint = True
            try:
                # upper
                if (y - 1) >= 0:
                    if value >= grid[y - 1][x]:
                        is_lowpoint = False
                # left
                if (x - 1) >= 0:
                    if value >= grid[y][x - 1]:
                        is_lowpoint = False
                # right
                if (x + 1) <= max_x:
                    if value >= grid[y][x + 1]:
                        is_lowpoint = False
                # lower
                if (y + 1) <= max_y:
                    if value >= grid[y + 1][x]:
                        is_lowpoint = False
            except IndexError:
                print("Index Error")

            if is_lowpoint:
                low_points.append(int(value))

    return sum([val + 1 for val in low_points])


def part_two(content) -> int:
    grid = []
    max_x = max_y = 0
    basin_size = []

    for row in content:
        line = []
        for num in row:
            line.append(int(num))
        grid.append(line)

    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            is_lowpoint = True
            try:
                # upper
                if (y - 1) >= 0:
                    if value >= grid[y - 1][x]:
                        is_lowpoint = False
                # left
                if (x - 1) >= 0:
                    if value >= grid[y][x - 1]:
                        is_lowpoint = False
                # right
                if (x + 1) <= max_x:
                    if value >= grid[y][x + 1]:
                        is_lowpoint = False
                # lower
                if (y + 1) <= max_y:
                    if value >= grid[y + 1][x]:
                        is_lowpoint = False
            except IndexError:
                print("Index Error")

            if is_lowpoint:
                count_higher_adjacent(grid, x, y)

    return 0


def count_higher_adjacent(grid, x, y) -> int:
    my_count = 0

    try:
        if grid[y][x] > grid[y - 1][x]:
            my_count += 1 + count_higher_adjacent(grid, x, y - 1)
        if grid[y][x] > grid[y][x - 1]:
            my_count += 1 + count_higher_adjacent(grid, x - 1, y)
        if grid[y][x] > grid[y][x + 1]:
            my_count += 1 + count_higher_adjacent(grid, x + 1, y)
        if grid[y][x] > grid[y + 1][x]:
            my_count += 1 + count_higher_adjacent(grid, x, y + 1)
    except IndexError:
        print("Index error")

    return my_count


if __name__ == '__main__':
    main()
