import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:  # noqa
    circuit_vectors = []

    """Get vectors for each point of both wires.
    Same vectors for both wires are intersections."""
    for wire_no, wire in enumerate(aoc_input):
        position = (0, 0)
        wire_vectors = []

        for way in wire.split(','):
            for _ in range(1, int(way[1:])+1):
                if 'U' in way:
                    position = (position[0], position[1] + 1)
                    wire_vectors.append(position)
                elif 'R' in way:
                    position = (position[0] + 1, position[1])
                    wire_vectors.append(position)
                elif 'D' in way:
                    position = (position[0], position[1] - 1)
                    wire_vectors.append(position)
                elif 'L' in way:
                    position = (position[0] - 1, position[1])
                    wire_vectors.append(position)
                else:
                    raise Exception('Invalid direction')
        circuit_vectors.append(wire_vectors)

    intersections = list(set(circuit_vectors[0]).intersection(circuit_vectors[1]))
    distance = []
    for vector in intersections:
        distance.append(abs(vector[0]) + abs(vector[1]))

    return min(map(abs, distance))


def part_two(aoc_input) -> int:  # noqa
    return 0


if __name__ == '__main__':
    main()
