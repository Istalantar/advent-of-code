import sys
from itertools import cycle

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(f'{part_one(aoc_input.copy())} (wrong: -1424)')
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    numbers = [int(i) for i in aoc_input]
    nums_amount = {int(i): 0 for i in aoc_input}
    for number in aoc_input:
        nums_amount[int(number)] += 1
    [nums_amount.pop(key) for key, val in nums_amount.copy().items() if val == 1]

    dont_move = dict[int: list]
    for number in numbers.copy():
        # find index to move: number only once in list
        old_index = numbers.index(number)

        # find index to move: number in list several times
        if number in nums_amount.keys():
            pass
            # number overtakes same value number

        new_index = None
        if 0 < old_index + number <= len(numbers):
            new_index = old_index + number
        elif old_index + number < 0:
            new_index = len(numbers) + 1 + number - old_index
        elif old_index + number > len(numbers):
            new_index = len(numbers) + 1 - old_index
        elif old_index + number == 0:
            new_index = len(numbers)

        numbers.pop(old_index)
        numbers.insert(new_index, number)

    return sum([numbers[i % len(numbers) - numbers.index(0) + 1] for i in range(1000, 3001, 1000)])


def part_two(aoc_input) -> int:
    return -1


if __name__ == '__main__':
    main()
