import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def tuple_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def tuple_sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def part_one(aoc_input) -> int:
    head = (0, 0)
    tail = (0, 0)
    tail_path = {tail}
    directions = {'R': (1, 0), 'D': (0, -1), 'L': (-1, 0), 'U': (0, 1)}
    # tail can move in 8 different directions, depending on position of head
    tail_step = {(2, 0): (1, 0), (0, -2): (0, -1), (-2, 0): (-1, 0), (0, 2): (0, 1),
                 (1, 2): (1, 1), (1, -2): (1, -1), (-1, 2): (-1, 1), (-1, -2): (-1, -1),
                 (2, 1): (1, 1), (2, -1): (1, -1), (-2, 1): (-1, 1), (-2, -1): (-1, -1)}
    for direction, steps in map(str.split, aoc_input):
        for i in range(int(steps)):
            head = tuple_add(head, directions[direction])
            diff = tuple_sub(head, tail)
            if diff in tail_step:
                tail = tuple_add(tail, tail_step[diff])
                tail_path.add(tail)
    return len(tail_path)


def part_two(aoc_input) -> int:
    head = (0, 0)
    tails = [(0, 0) for _ in range(9)]
    tail_path = [{tails[0]} for _ in range(9)]
    directions = {'R': (1, 0), 'D': (0, -1), 'L': (-1, 0), 'U': (0, 1)}
    # tail can move in 8 different directions, depending on position of head
    tail_step = {(2, 0): (1, 0), (0, -2): (0, -1), (-2, 0): (-1, 0), (0, 2): (0, 1),
                 (1, 2): (1, 1), (1, -2): (1, -1), (-1, 2): (-1, 1), (-1, -2): (-1, -1),
                 (2, 1): (1, 1), (2, -1): (1, -1), (-2, 1): (-1, 1), (-2, -1): (-1, -1),
                 (2, 2): (1, 1), (2, -2): (1, -1), (-2, 2): (-1, 1), (-2, -2): (-1, -1)}
    for direction, steps in map(str.split, aoc_input):
        for i in range(int(steps)):
            head = tuple_add(head, directions[direction])
            diff = tuple_sub(head, tails[0])
            for j in range(len(tails)):
                if diff in tail_step:
                    tails[j] = tuple_add(tails[j], tail_step[diff])
                    tail_path[j].add(tails[j])
                    if j < len(tails) - 1:
                        diff = tuple_sub(tails[j], tails[j + 1])

    return len(tail_path[8])


if __name__ == '__main__':
    main()
