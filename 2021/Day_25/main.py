import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    seafloor = []

    for line in content:
        seafloor.append(list(line))

    return 0


def part_two(content) -> int:

    return 0


def step(seafloor):
    for row in seafloor:
        pass

    return seafloor


if __name__ == '__main__':
    main()
