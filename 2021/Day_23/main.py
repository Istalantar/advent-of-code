import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    hallway = ['.' for _ in range(content[1].count('.'))]
    side_a, side_b, side_c, side_d = map(list, zip(list(content[3].replace('#', '')),
                                                   list(content[2].replace('#', ''))))

    return 0


def part_two(content) -> int:

    return 0


if __name__ == '__main__':
    main()
