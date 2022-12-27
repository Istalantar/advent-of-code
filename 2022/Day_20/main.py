import sys
from itertools import cycle

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(f'{part_one(aoc_input.copy())} (wrong: -1424, 11254, -1093, 1093)')
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    numbers = [int(i) for i in aoc_input]
    nums_index = {int(i): [] for i in aoc_input}
    for i, number in enumerate(aoc_input):
        nums_index[int(number)].append(i)
    [nums_index.pop(key) for key, val in nums_index.copy().items() if len(val) == 1]

    for number in numbers.copy():
        # find index to move: number only once in list
        old_index = numbers.index(number)

        # find index to move: number in list several times
        if number in nums_index.keys():
            old_index = nums_index[number].pop(0)

        try:
            assert numbers[old_index] == number
        except AssertionError as e:
            raise e

        new_index = None
        num = number if abs(number) < len(numbers) else number % (len(numbers) - 1)
        # number moved left or right without overflow
        if 0 < old_index + num <= len(numbers):
            new_index = old_index + num
        # number moved left with overflow
        elif old_index + num < 0:
            new_index = len(numbers) - 1 + num
        # number moved right with overflow
        elif old_index + num > len(numbers):
            new_index = len(numbers) + 1 - old_index
        # number between first and last number is at the end of the list
        elif old_index + num == 0:
            new_index = len(numbers)

        try:
            assert new_index > 0
            assert numbers.pop(old_index) == number
        except AssertionError as e:
            raise e
        numbers.insert(new_index, number)

        # adjust saved indices
        for indices in nums_index.values():
            for i, index in enumerate(indices):
                if index not in range(old_index + 1, new_index + 1):
                    continue
                # index increases if number moved to the left, without overflow
                if number < 0 and old_index > new_index:
                    indices[i] += 1
                # index decreases if number moved to the right, without overflow
                elif number > 0 and old_index < new_index:
                    indices[i] -= 1
                # index decreases if number moved to the left, with overflow
                elif number < 0 and old_index + number < 0:
                    indices[i] -= 1
                # index increases if number moved to the right, with overflow
                elif number > 0 and old_index + number > len(numbers):
                    indices[i] += 1
                else:
                    raise Exception('Unexpected increase/decrease')

    return sum([numbers[i % len(numbers) - numbers.index(0) + 1] for i in range(1000, 3001, 1000)])


def part_two(aoc_input) -> int:
    return -1


if __name__ == '__main__':
    main()
