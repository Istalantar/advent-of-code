import sys
import string

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:  # noqa
    res = 0
    for rucksack in aoc_input:
        comp_1 = rucksack[:len(rucksack)//2]
        comp_2 = rucksack[len(rucksack)//2:]
        item = set(comp_1).intersection(comp_2).pop()
        if item.isupper():
            res += string.ascii_uppercase.index(item) + 27
        else:
            res += string.ascii_lowercase.index(item) + 1
    return res


def part_two(aoc_input) -> int:  # noqa
    res = 0
    groups = list(zip(*(iter(aoc_input), ) * 3))
    for group in groups:
        inter_1 = set(group[0]).intersection(group[1])
        item = inter_1.intersection(group[2]).pop()
        if item.isupper():
            res += string.ascii_uppercase.index(item) + 27
        else:
            res += string.ascii_lowercase.index(item) + 1
    return res


if __name__ == '__main__':
    main()
