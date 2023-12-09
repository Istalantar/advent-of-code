import sys
import itertools
from math import lcm
import logging

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    logging.basicConfig(level=logging.INFO, style='{', format='{message}')
    aoc_input = my_input_list("input.txt")

    logging.info(part_one(aoc_input.copy()))
    logging.info(part_two(aoc_input.copy()))


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
    nodes = {}
    starting_nodes = set()
    ending_nodes = set()
    for line in aoc_input[2:]:
        node_name, next_nodes = line.split(' = ')
        next_nodes = (next_nodes[1:4], next_nodes[6:9])
        nodes[node_name] = next_nodes
        if node_name[2] == 'A':
            starting_nodes.add(node_name)
        elif node_name[2] == 'Z':
            ending_nodes.add(node_name)

    steps_to_end = {node: 0 for node in starting_nodes}
    for node in starting_nodes:
        logging.debug(f'Tracing {node=}')
        not_finished = True
        i = 0
        instructions = itertools.cycle(aoc_input[0])
        current_node = node
        while not_finished:
            i += 1
            instruction = next(instructions)
            next_node = nodes[current_node][0] if instruction == 'L' else nodes[current_node][1]
            if next_node in ending_nodes:
                not_finished = False
            else:
                current_node = next_node
        steps_to_end[node] = i
        logging.debug(f'Steps for {node} = {i}')

    # after finding the first ending for each starting node,
    # use 'least common multiple' to find the step where they all meet
    # Example, to get the idea:
    # person A can go around a track in 3 minutes and person B runs around the same track in 5 minutes.
    # If they start at the same time, how long does it take for them to meet at the start again?
    # lcm(3, 5) -> 15 Minutes
    return lcm(*steps_to_end.values())


if __name__ == '__main__':
    main()
