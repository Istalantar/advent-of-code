import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    print(part_one(list(map(str.strip, aoc_input.split(',')))))
    print(part_two(list(map(str.strip, aoc_input.split(',')))))


def part_one(aoc_input) -> int:
    directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    heading = 0
    position = (0, 0)  # (x, y)

    for instruction in aoc_input:
        # turn to correct direction
        if instruction[0] == 'R':
            heading = heading + 1 if heading < 3 else 0
        elif instruction[0] == 'L':
            heading = heading - 1 if heading > 0 else 3
        else:
            raise ValueError('Unexpected instruction')
        # walk the steps
        steps = tuple(map(lambda a: a * int(instruction[1:]), directions[list(directions.keys())[heading]]))
        position = tuple(map(lambda a, b: a + b, position, steps))
    return abs(position[0] + position[1])


def part_two(aoc_input) -> int:
    directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    heading = 0
    position = (0, 0)  # (x, y)
    coords = dict()

    for instruction in aoc_input:
        # turn to correct direction
        if instruction[0] == 'R':
            heading = heading + 1 if heading < 3 else 0
        elif instruction[0] == 'L':
            heading = heading - 1 if heading > 0 else 3
        else:
            raise ValueError('Unexpected instruction')
        # walk the steps
        found_intersection = False
        for steps in range(int(instruction[1:])):
            position = tuple(map(lambda a, b: a + b, position, directions[list(directions.keys())[heading]]))
            if position in coords.keys():
                found_intersection = True
                break
            else:
                coords[position] = True

        if found_intersection:
            break
    return abs(position[0] + position[1])


if __name__ == '__main__':
    main()
