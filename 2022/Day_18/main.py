import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(f'{part_two(aoc_input.copy())} (wrong: 3462)')


def part_one(aoc_input) -> int:
    cubes = list(map(lambda l: tuple(map(int, l.strip().split(','))), aoc_input))
    sides = len(cubes) * 6
    for x, y, z in cubes:
        for neighbour in neighbours(x, y, z):
            if neighbour in cubes:
                sides -= 1
    return sides


def part_two(aoc_input) -> int:
    cubes = list(map(lambda l: tuple(map(int, l.strip().split(','))), aoc_input))
    sides = len(cubes) * 6
    for x, y, z in cubes:
        for neighbour in neighbours(x, y, z):
            if neighbour in cubes:
                sides -= 1
    all_x = [x for x, _, _ in cubes]
    all_y = [y for _, y, _ in cubes]
    all_z = [z for _, _, z in cubes]
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    min_z, max_z = min(all_z), max(all_z)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) in cubes:
                    continue
                else:
                    pass
                if all([(dx, dy, dz) in cubes for dx, dy, dz in neighbours(x, y, z)]):
                    sides -= 6
    return sides


def neighbours(x, y, z) -> list:
    return [(x - 1, y, z), (x + 1, y, z),
            (x, y - 1, z), (x, y + 1, z),
            (x, y, z - 1), (x, y, z + 1)]


if __name__ == '__main__':
    main()
