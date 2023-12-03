import sys
import string
from typing import Dict
from math import prod

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(f'{part_one(aoc_input.copy())} - not correct: (519861)')
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    engine = Engine(aoc_input)
    return engine.part_sum


def part_two(aoc_input) -> int:
    engine = Engine(aoc_input)
    return engine.ratio_sum


class Engine:
    def __init__(self, schematic):
        self.symbol_coords = []
        self.part_sum = 0
        self.ratio_sum = 0
        self.schematic = schematic
        self.y_max = len(schematic) - 1
        self.x_max = len(schematic[0]) - 1
        self.gears: Dict[tuple, list] = {}
        self._get_symbol_coords()
        self._calculate_results()

    def _get_symbol_coords(self):
        for y, line in enumerate(self.schematic):
            for x, character in enumerate(line):
                if character in string.punctuation and character != '.':
                    self.symbol_coords.append((y, x))

    def _calculate_results(self):
        for y, line in enumerate(self.schematic):
            number_found = False
            num_start = -1
            for x, character in enumerate(line):
                if not number_found and character in string.digits:
                    # find start index of number in row
                    number_found = True
                    num_start = (y, x)

                if number_found and not self._is_next_char_digit((y, x)):
                    # find end index of number in row
                    number_found = False
                    num_end = (y, x)
                    number = int(line[num_start[1]:num_end[1] + 1])
                    symbol_coordinate = self._has_adjecent_symbol((num_start, num_end))
                    if symbol_coordinate is not None:
                        self.part_sum += number
                        if symbol_coordinate in self.gears.keys():
                            self.gears[symbol_coordinate].append(number)
                        else:
                            self.gears[symbol_coordinate] = [number]
                    else:
                        a = None

        self._calculate_gear_ratio()

    def _calculate_gear_ratio(self):
        for key, item in self.gears.items():
            if len(item) == 2:
                self.ratio_sum += prod(item)

    def _has_adjecent_symbol(self, num_coords: ((int, int), (int, int))) -> None | tuple:
        y_start = 0 if num_coords[0][0] == 0 else num_coords[0][0] - 1
        y_end = self.y_max if num_coords[1][0] == self.y_max else num_coords[1][0] + 1
        x_start = 0 if num_coords[0][1] == 0 else num_coords[0][1] - 1
        x_end = self.y_max if num_coords[1][1] == self.x_max else num_coords[1][1] + 1

        if y_start < 0 or x_start < 0:
            raise ValueError('Index value below min')

        if y_end > self.y_max or x_end > self.x_max:
            raise ValueError('Index value above max')

        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                if (y, x) in self.symbol_coords:
                    return y, x

        return None

    def _is_next_char_digit(self, coords: (int, int)) -> bool:
        y, x = coords

        if x == self.x_max:
            return False
        elif self.schematic[y][x + 1] in string.digits:
            return True

        return False


if __name__ == '__main__':
    main()
