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
    sides = 0
    for cube in cubes:
        for x, y, z in neighbours(*cube):
            if (x, y, z) in cubes:
                continue
            if not all([(dx, dy, dz) in cubes for dx, dy, dz in neighbours(x, y, z)]):
                sides += 1
            # ToDo: solve two air pieces next to each other
    return sides


def neighbours(x, y, z) -> list:
    return [(x - 1, y, z), (x + 1, y, z),
            (x, y - 1, z), (x, y + 1, z),
            (x, y, z - 1), (x, y, z + 1)]


if __name__ == '__main__':
    main()
