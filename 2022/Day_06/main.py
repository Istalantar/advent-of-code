import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt").strip()

    print(part_one(aoc_input))
    print(part_two(aoc_input))


def part_one(aoc_input) -> int:
    for i in range(len(aoc_input)):
        has_twice = False
        for char in aoc_input[i:i+4]:
            if aoc_input[i:i+4].count(char) > 1:
                has_twice = True
                break
        if not has_twice:
            return aoc_input.index(aoc_input[i:i+4]) + 4
    return -1


def part_two(aoc_input) -> int:
    for i in range(len(aoc_input)):
        has_twice = False
        for char in aoc_input[i:i+14]:
            if aoc_input[i:i+14].count(char) > 1:
                has_twice = True
                break
        if not has_twice:
            return aoc_input.index(aoc_input[i:i+14]) + 14
    return -1


if __name__ == '__main__':
    main()
