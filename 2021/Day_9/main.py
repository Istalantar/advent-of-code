import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content.copy()))
    print(part_two(content.copy()))


def part_one(content) -> int:
    grid = []
    low_points = []

    for row in content:
        line = []
        for num in row:
            line.append(int(num))
        grid.append(line)

    max_y = len(grid)
    max_x = len(grid[0])
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
                if (x + 1) < max_x:
                    if value >= grid[y][x + 1]:
                        is_lowpoint = False
                # lower
                if (y + 1) < max_y:
                    if value >= grid[y + 1][x]:
                        is_lowpoint = False
            except IndexError:
                print("Index Error")

            if is_lowpoint:
                low_points.append(int(value))

    return sum([val + 1 for val in low_points])


def part_two(content) -> int:
    grid = []
    basin_size = []

    for row in content:
        line = []
        for num in row:
            line.append(int(num))
        grid.append(line)

    max_y = len(grid)
    max_x = len(grid[0])
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
                if (x + 1) < max_x:
                    if value >= grid[y][x + 1]:
                        is_lowpoint = False
                # lower
                if (y + 1) < max_y:
                    if value >= grid[y + 1][x]:
                        is_lowpoint = False
            except IndexError:
                print("Index Error")

            if is_lowpoint:
                pos_counted = []  # list to remember which position was already counted
                for _ in range(max_y):
                    pos_counted.append([False for _ in range(max_x)])
                basin_size.append(count_higher_adjacent(grid, pos_counted, x, y))

    basin_size.sort()

    return basin_size[-1] * basin_size[-2] * basin_size[-3]


def count_higher_adjacent(grid, pos_counted, x, y) -> int:
    my_count = 1
    max_y = len(grid)
    max_x = len(grid[0])

    # upper
    if (y - 1) >= 0 and grid[y][x] < grid[y - 1][x] < 9 and not pos_counted[y - 1][x]:
        my_count += count_higher_adjacent(grid, pos_counted, x, y - 1)
    # left
    if (x - 1) >= 0 and grid[y][x] < grid[y][x - 1] < 9 and not pos_counted[y][x - 1]:
        my_count += count_higher_adjacent(grid, pos_counted, x - 1, y)
    # right
    if (x + 1) < max_x and grid[y][x] < grid[y][x + 1] < 9 and not pos_counted[y][x + 1]:
        my_count += count_higher_adjacent(grid, pos_counted, x + 1, y)
    # lower
    if (y + 1) < max_y and grid[y][x] < grid[y + 1][x] < 9 and not pos_counted[y + 1][x]:
        my_count += count_higher_adjacent(grid, pos_counted, x, y + 1)

    pos_counted[y][x] = True

    return my_count


if __name__ == '__main__':
    main()
