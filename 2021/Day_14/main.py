import sys
import collections
import regex as re

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class Element:
    def __init__(self, element, insert, occurence, el_idx):
        self.element = element
        self.insert = insert
        self.occurence = occurence
        self.index = el_idx

    def __repr__(self):
        return self.element


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    start = str(content[0])
    rules = content[2:]
    polymer = start
    steps = 10

    for _ in range(steps):
        elements = []
        for rule in rules:
            element, insert = rule.split(' -> ')

            # remember what needs to be replaced
            if element in polymer:
                occ_all = [occ.start() for occ in re.finditer(element, polymer, overlapped=True)]
                for i in range(len(occ_all)):
                    elements.append([element, insert, occ_all[i]])

        # sort to be replaced elements by index
        elements.sort(key=lambda x: x[2])

        # replace
        replace_cnt = 0
        for ele in elements:  # ele = [element, insert, index]
            polymer = polymer[:ele[2] + replace_cnt] + \
                      polymer[ele[2] + replace_cnt:ele[2] + 2 + replace_cnt].replace(ele[0],
                                                                                     ele[0][0] + ele[1] + ele[0][1]) + \
                      polymer[ele[2] + 2 + replace_cnt:]
            replace_cnt += 1

    polymer = list(polymer)
    letter_count = collections.Counter(polymer)
    common = letter_count.most_common()

    return common[0][1] - common[-1][1]


def part_two(content) -> int:
    return 0


if __name__ == '__main__':
    main()
