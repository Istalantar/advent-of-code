import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402

DIGITS_SPELLED = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                  'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    res = 0
    for line in aoc_input:
        numbers = []
        for character in line:
            if character.isdigit():
                numbers.append(character)
        res += int(f'{numbers[0]}{numbers[-1]}')

    return res


def part_two(aoc_input) -> int:
    res = 0
    line: str
    for line in aoc_input:
        first_number: str = ''
        second_number: str = ''

        # find first word
        word_index = float('inf')
        for number in DIGITS_SPELLED:
            line_index = line.find(number)
            if -1 < line_index < word_index:
                word_index = line_index
                first_number = DIGITS_SPELLED[number]

        # find first digit
        for i, character in enumerate(line):
            if character.isdigit():
                digit_index = i
                # overwrite first_number if the index is smaller
                first_number = character if digit_index < word_index else first_number
                break

        # find last word
        word_index = -1
        for number in DIGITS_SPELLED:
            if line.rfind(number) > word_index:
                word_index = line.rfind(number)
                second_number = DIGITS_SPELLED[number]

        # find last digit
        for i, character in enumerate(line):
            if character.isdigit():
                digit_index = i
                # overwrite second_number if index is higher
                second_number = character if digit_index > word_index else second_number

        res += int(f'{first_number}{second_number}')

    return res


if __name__ == '__main__':
    main()
