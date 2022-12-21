import sys
from itertools import zip_longest

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    print(part_one(aoc_input))
    print(part_two(aoc_input))


def part_one(aoc_input) -> int:
    pairs = map(str.strip, aoc_input.split('\n\n'))
    pair_objs = dict()
    for index, input_pair in enumerate(pairs):
        pair = Pair(*map(eval, input_pair.split('\n')))
        pair_objs[index + 1] = pair
    return sum([i if v.is_right_order else 0 for i, v in pair_objs.items()])


def part_two(aoc_input) -> int:
    packets = aoc_input.replace('\n\n', '\n').strip().split('\n')
    packets = [eval(packet.strip()) for packet in packets]
    packets.append([[2]])
    packets.append([[6]])

    bubble_sort = True
    while bubble_sort:
        bubble_sort = False
        for i in range(len(packets) - 1):
            if not Pair(packets[i], packets[i + 1]).is_right_order:
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                bubble_sort = True

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.depth = 0
        self.is_right_order = False
        self.decision = ''
        self._evaluate_lists(self.left, self.right)

    def _evaluate_lists(self, left, right) -> bool:
        """Decides whether left and right element are in the right order

        :param left: first element
        :param right: second element
        :return: True if decision was made, False if no decision was made
        """
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                self.is_right_order = True
                self.decision = 'Left int is smaller'
                return True
            elif right < left:
                self.is_right_order = False
                self.decision = 'Right int is smaller'
                return True
            else:
                return False
        elif isinstance(left, list) and isinstance(right, list):
            for links, rechts in zip_longest(left, right, fillvalue=None):
                if self._evaluate_lists(links, rechts):
                    return True
            return False
        elif isinstance(left, int) and isinstance(right, list):
            return self._evaluate_lists([left], right)
        elif isinstance(left, list) and isinstance(right, int):
            return self._evaluate_lists(left, [right])
        elif left is None and right is not None:
            self.is_right_order = True
            self.decision = 'Left ran out of items'
            return True
        elif left is not None and right is None:
            self.is_right_order = False
            self.decision = 'Right ran out of items'
            return True
        else:
            raise Exception('Unexpected list element')


if __name__ == '__main__':
    main()
