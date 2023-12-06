import sys
from math import prod

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    times = list(map(int, (aoc_input[0].split(':')[1].split())))
    distances = list(map(int, (aoc_input[1].split(':')[1].split())))
    # d = v * t
    win_count = []
    for t_max, d_record in zip(times, distances):
        # find record with least acceleration time
        v = 0
        t_win_min = t_win_max = 0
        for t in range(1, t_max):
            v += 1
            d = v * (t_max - t)
            if d > d_record:
                t_win_min = t
                break

        # find record with most acceleration time
        v = t_max
        for t in range(t_max - 1, 0, -1):
            v -= 1
            d = v * (t_max - t)
            if d > d_record:
                t_win_max = t
                break

        # find number of possible wins
        win_count.append(t_win_max - t_win_min + 1)

    return prod(win_count)


def part_two(aoc_input) -> int:
    return -1


if __name__ == '__main__':
    main()
