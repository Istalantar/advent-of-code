import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    values = []

    for history in aoc_input:
        is_all_zero = False
        depth = 0
        sequences = {depth: list(map(int, history.split()))}
        while not is_all_zero:
            depth += 1
            previous_sequence = sequences[depth - 1]
            next_sequence = []
            for i in range(len(sequences[depth - 1]) - 1):
                value = previous_sequence[i + 1] - previous_sequence[i]
                next_sequence.append(value)

            sequences[depth] = next_sequence
            if not any([val for val in next_sequence]):
                is_all_zero = True

        # add next value from bottom up
        for depth in range(len(sequences.keys()) - 2, -1, -1):
            top_sequence = sequences[depth + 1]
            bottom_sequence = sequences[depth]
            sequences[depth].append(top_sequence[-1] + bottom_sequence[-1])
        values.append(sequences[0][-1])

    return sum(values)


def part_two(aoc_input) -> int:
    return -1


if __name__ == '__main__':
    main()
