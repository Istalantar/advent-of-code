import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:  # noqa
    points_1 = 0
    points_2 = 0
    for t_round in aoc_input:
        if 'X' in t_round:  # Rock
            points_2 += 1
        if 'Y' in t_round:  # Paper
            points_2 += 2
        if 'Z' in t_round:  # Scissors
            points_2 += 3

        players = t_round.strip().split(' ')
        if 'A' in t_round and 'X' in t_round \
                or 'B' in t_round and 'Y' in t_round \
                or 'C' in t_round and 'Z' in t_round:
            points_1 += 3
            points_2 += 3
        elif 'A' in t_round and 'Y' in t_round \
                or 'B' in t_round and 'Z' in t_round \
                or 'C' in t_round and 'X' in t_round:
            points_2 += 6
        else:
            points_1 += 6

    return points_2


def part_two(aoc_input) -> int:  # noqa
    points = 0
    for t_round in aoc_input:
        if 'X' in t_round:  # Lose
            if 'A' in t_round:
                points += 3
            elif 'B' in t_round:
                points += 1
            elif 'C' in t_round:
                points += 2
        elif 'Z' in t_round:  # Win
            points += 6
            if 'A' in t_round:
                points += 2
            elif 'B' in t_round:
                points += 3
            elif 'C' in t_round:
                points += 1
        elif 'Y' in t_round:  # Draw
            points += 3
            if 'A' in t_round:
                points += 1
            elif 'B' in t_round:
                points += 2
            elif 'C' in t_round:
                points += 3

    return points


if __name__ == '__main__':
    main()
