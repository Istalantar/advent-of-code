import sys
import itertools

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    nodes = {}
    for line in aoc_input[2:]:
        node_name, next_nodes = line.split(' = ')
        next_nodes = (next_nodes[1:4], next_nodes[6:9])
        nodes[node_name] = next_nodes

    not_finished = True
    i = 0
    instructions = itertools.cycle(aoc_input[0])
    current_node = 'AAA'
    while not_finished:
        i += 1
        instruction = next(instructions)
        next_node = nodes[current_node][0] if instruction == 'L' else nodes[current_node][1]
        if next_node == 'ZZZ':
            not_finished = False
        else:
            current_node = next_node

    return i


def part_two(aoc_input) -> int:
    return -1


if __name__ == '__main__':
    main()
