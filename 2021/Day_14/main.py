import sys
import collections

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class Element:
    def __init__(self, element, insert, occurence, el_idx):
        self.element = element
        self.insert = insert
        self.occurence = occurence
        self.index = el_idx


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    start = str(content[0])
    rules = content[2:]
    polymer = start

    # for _ in range(10):
    #     for rule in rules:
    #         element, insert = rule.split(' -> ')
    #         occ = start.count(element)
    #         search_index = 0
    #         for _ in range(occ):
    #             ind = start[search_index:].find(element)
    #             polymer = start[:ind] + \
    #                       start[ind:ind + 2].replace(element, element[0] + insert + element[1]) + \
    #                       start[ind + 2:]  # noqa
    #             search_index += 3
    #
    #     start = polymer

    for _ in range(1):
        elements = []
        for rule in rules:
            element, insert = rule.split(' -> ')
            
            # remember what needs to be replaced
            if element in start:
                el_idx = []
                el_cnt = start.count(element)
                temp_idx = 0
                for _ in range(el_cnt):
                    temp_idx = start[temp_idx:].find(element)
                    el_idx.append(temp_idx)
                elements.append(Element(element, insert, el_cnt, el_idx))
                
        # replace
        rep_cnt = 0  # replace count
        # ToDo: Rep count nur auf indizes anwenden, die groesser sind als der platz wo was eingefuegt wurde
        # Beispiel: wenn an Position 3 eingefuegt wurde muss beim einfuegen an Pos 1 keine Indexanpassung stattfinden
        for ele in elements:
            for i in range(ele.occurence):
                polymer = polymer[:ele.index[i] + rep_cnt] + \
                          polymer[ele.index[i] + rep_cnt:ele.index[i] + rep_cnt + 2].replace(ele.element,
                                                         ele.element[0] + ele.insert + ele.element[1]) + \
                          polymer[ele.index[i] + rep_cnt + 2:]  # noqa
                rep_cnt += 1

    polymer = list(polymer)
    letter_count = collections.Counter(polymer)
    common = letter_count.most_common()

    return common[0][1] - common[-1][1]


def part_two(content) -> int:
    return 0


if __name__ == '__main__':
    main()
