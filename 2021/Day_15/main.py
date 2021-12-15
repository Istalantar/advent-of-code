import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    cavern = []

    for line in content:
        cav_row = []
        for col in list(line):
            cav_row.append(int(col))

        cav_row.sort()
        cavern.append(cav_row)

    for row in cavern:
        str_row = list(map(lambda x: format(x, '2d'), row))
        print(str_row, sum(row))

    col_sum = []
    for col in zip(*cavern):
        col_sum.append(sum(col))

    print(list(map(lambda x: format(x, '02d'), col_sum)))

    return 0


def part_two(content) -> int:

    return 0


if __name__ == '__main__':
    main()
