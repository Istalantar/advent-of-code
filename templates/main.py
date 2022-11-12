import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:  # noqa
    return 0


def part_two(aoc_input) -> int:  # noqa
    return 0


if __name__ == '__main__':
    main()
