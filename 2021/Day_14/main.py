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
    print('The result of Part 2 is one too low, because one letter is counted too less')  # see code comment


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
        rep_cnt = 0
        for ele in elements:  # ele = [element, insert, index]
            polymer = polymer[:ele[2] + rep_cnt] + \
                      polymer[ele[2] + rep_cnt:ele[2] + 2 + rep_cnt].replace(ele[0],
                                                                             ele[0][0] + ele[1] + ele[0][1]) + \
                      polymer[ele[2] + 2 + rep_cnt:]
            rep_cnt += 1

    polymer = list(polymer)
    letter_count = collections.Counter(polymer)
    common = letter_count.most_common()

    return common[0][1] - common[-1][1]


def part_two(content) -> int:
    start = str(content[0])
    rules = []
    polymer = start
    elements = {}
    letters = {}
    steps = 40

    for rule in content[2:]:
        element, insert = rule.split(' -> ')
        rules.append((element, insert))
        for letter in element:
            letters[letter] = 0
        elements[element] = 0

    for key, val in elements.items():
        elements[key] = len(re.findall(key, polymer, overlapped=True))

    for _ in range(steps):
        cp_eles = elements.copy()

        for ele, ins in rules:
            if cp_eles[ele] > 0:
                elements[ele] -= cp_eles[ele]
                elements[ele[0] + ins] += cp_eles[ele]
                elements[ins + ele[1]] += cp_eles[ele]

    # count letters
    # of each pair only the first letter will be counted
    # this means, that one letter will not be counted (the last letter of the last pair in the polynom)
    # since I only keep track of the pairs an not the polynom itself, I don't know which would be the last letter
    for ele_key, ele_val in elements.items():
        for let_key, let_val in letters.items():
            if ele_key[0] == let_key:
                letters[let_key] += ele_val

    letters = list(i for i in letters.items())
    letters.sort(key=lambda x: x[1], reverse=True)

    return letters[0][1] - letters[-1][1]


if __name__ == '__main__':
    main()
