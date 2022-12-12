import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    # start with number of all outer trees
    max_y = len(aoc_input)
    max_x = len(aoc_input[0])
    coords = set()

    for y, row in enumerate(aoc_input):
        max_nr = -1
        for x in range(max_x):
            # left to right
            if int(aoc_input[y][x]) > max_nr:
                coords.add((x, y))
                max_nr = int(aoc_input[y][x])
            elif int(aoc_input[y][x]) == 9:
                break

    for y, row in enumerate(aoc_input):
        max_nr = -1
        for x in range(max_x)[::-1]:
            # right to left
            if int(aoc_input[y][x]) > max_nr:
                coords.add((x, y))
                max_nr = int(aoc_input[y][x])
            elif int(aoc_input[y][x]) == 9:
                break

    for x in range(max_x):
        max_nr = -1
        for y in range(max_y):
            # top to bottom
            if int(aoc_input[y][x]) > max_nr:
                coords.add((x, y))
                max_nr = int(aoc_input[y][x])
            elif int(aoc_input[y][x]) == 9:
                break

    for x in range(max_x):
        max_nr = -1
        for y in range(max_y)[::-1]:
            # bottom to top
            if int(aoc_input[y][x]) > max_nr:
                coords.add((x, y))
                max_nr = int(aoc_input[y][x])
            elif int(aoc_input[y][x]) == 9:
                break

    return len(coords)


def part_two(aoc_input) -> int:
    # start with number of all outer trees
    max_y = len(aoc_input)
    max_x = len(aoc_input[0])
    scenic_score = []

    for y in range(max_y):
        for x in range(max_x):
            score = 1
            if 0 < x < max_x and 0 < y < max_y:
                tree_height = int(aoc_input[y][x])
                # look top
                distance = 0
                for i in range(1, y + 1):
                    distance += 1
                    if int(aoc_input[y - i][x]) < tree_height:
                        continue
                    else:
                        break
                score *= distance
                # look right
                distance = 0
                for i in range(1, max_x - x):
                    distance += 1
                    if int(aoc_input[y][x + i]) < tree_height:
                        continue
                    else:
                        break
                score *= distance
                # look bottom
                distance = 0
                for i in range(1, max_y - y):
                    distance += 1
                    if int(aoc_input[y + i][x]) < tree_height:
                        continue
                    else:
                        break
                score *= distance
                # look left
                distance = 0
                for i in range(1, x + 1):
                    distance += 1
                    if int(aoc_input[y][x - i]) < tree_height:
                        continue
                    else:
                        break
                score *= distance
                scenic_score.append(score)

    return max(scenic_score)


if __name__ == '__main__':
    main()
