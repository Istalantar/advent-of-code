import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    cnt = 0
    for pair in aoc_input:
        elf_1, elf_2 = pair.split(',')
        elf_1_start, elf_1_end = map(int, elf_1.split('-'))
        elf_2_start, elf_2_end = map(int, elf_2.split('-'))
        elf_1_sections = set(range(elf_1_start, elf_1_end + 1))
        elf_2_sections = set(range(elf_2_start, elf_2_end + 1))
        elf_1_section_length = len(elf_1_sections)
        elf_2_section_length = len(elf_2_sections)
        overlap = elf_1_sections.intersection(elf_2_sections)
        if min(elf_1_section_length, elf_2_section_length) == len(overlap):
            cnt += 1
    return cnt


def part_two(aoc_input) -> int:
    cnt = 0
    for pair in aoc_input:
        elf_1, elf_2 = pair.split(',')
        elf_1_start, elf_1_end = map(int, elf_1.split('-'))
        elf_2_start, elf_2_end = map(int, elf_2.split('-'))
        elf_1_sections = set(range(elf_1_start, elf_1_end + 1))
        elf_2_sections = set(range(elf_2_start, elf_2_end + 1))
        overlap = elf_1_sections.intersection(elf_2_sections)
        if len(overlap) != 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    main()
