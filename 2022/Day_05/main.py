import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    print(part_one(aoc_input))
    print(part_two(aoc_input))


class Storage:
    def __init__(self, start_position):
        self.stacks = []
        self._set_up_initial_stacks(start_position)

    def _set_up_initial_stacks(self, start_layout: str):
        """Sets up the initial stacks"""
        rows = start_layout.split('\n')
        max_stacks = len(rows[-1].split())
        [self.stacks.append([]) for _ in range(max_stacks)]
        # format of information in one line is: 3 string digits seperated by one whitespace
        # if there is no box in a position then there are 3 whitespaces instead of string digits
        for line in rows[::-1][1:]:  # columns without column numbers
            for i, box in enumerate(line[1::4]):
                if box.isalpha():
                    self.stacks[i].append(box)

    def move(self, num: int, src: int, dst: int):
        """Moves one box at a time from src to dst stack"""
        for i in range(num):
            self.stacks[dst - 1].append(self.stacks[src - 1].pop())

    def move_9001(self, num: int, src: int, dst: int):
        """Moves num boxes at a time from src to dst stack"""
        self.stacks[dst - 1] += self.stacks[src - 1][-num:]  # get stacks to dst

        for i in range(num):
            self.stacks[src - 1].pop()  # remove stacks from src

    def get_top_boxes(self) -> str:
        """Returns the name of all the boxes in the top row"""
        top_boxes = ''
        for stack in self.stacks:
            top_boxes += stack[-1]
        return top_boxes


def part_one(aoc_input) -> str:
    start_position, moves = aoc_input.split('\n\n')
    stacks = Storage(start_position)
    for move in moves.strip().split('\n'):
        _, num, _, src, _, dst = move.split()
        stacks.move(int(num), int(src), int(dst))
    return stacks.get_top_boxes()


def part_two(aoc_input) -> str:
    start_position, moves = aoc_input.split('\n\n')
    stacks = Storage(start_position)
    for move in moves.strip().split('\n'):
        _, num, _, src, _, dst = move.split()
        stacks.move_9001(int(num), int(src), int(dst))
    return stacks.get_top_boxes()


if __name__ == '__main__':
    main()
