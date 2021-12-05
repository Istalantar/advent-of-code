import sys

sys.path.append('../..')
from myFunctions import my_input  # noqa E402


def main():
    content = my_input("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    res = 0
    return res


def part_two(content) -> int:
    res = 0
    return res


if __name__ == '__main__':
    main()
