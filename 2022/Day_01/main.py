import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    print(part_one(aoc_input))
    print(part_two(aoc_input))


def part_one(aoc_input) -> int:  # noqa
    elves = []
    for elf in aoc_input.strip().split('\n\n'):
        calories = 0
        for val in elf.strip().split('\n'):
            calories += int(val)
        elves.append(calories)

    return max(elves)


def part_two(aoc_input) -> int:  # noqa
    elves = []
    for elf in aoc_input.strip().split('\n\n'):
        calories = 0
        for val in elf.strip().split('\n'):
            calories += int(val)

        elves.append(calories)
    elves.sort()
    return sum(elves[-3:])


if __name__ == '__main__':
    main()
