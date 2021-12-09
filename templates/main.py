import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:

    return 0


def part_two(content) -> int:

    return 0


if __name__ == '__main__':
    main()
