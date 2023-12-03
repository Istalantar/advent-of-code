import sys
import string

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(f'{part_one(aoc_input.copy())} - not correct: (519861)')
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    engine = Engine(aoc_input)
    return engine.get_part_sum()


def part_two(aoc_input) -> int:
    return -1


class Engine:
    def __init__(self, schematic):
        self.symbol_coords = []
        self.part_sum = 0
        self.schematic = schematic
        self.y_max = len(schematic) - 1
        self.x_max = len(schematic[0]) - 1
        self._get_symbol_coords()
        self._calculate_part_sum()

    def _get_symbol_coords(self):
        for y, line in enumerate(self.schematic):
            for x, character in enumerate(line):
                if character in string.punctuation and character != '.':
                    self.symbol_coords.append((y, x))

    def _calculate_part_sum(self):
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
                    if self._has_adjecent_symbol((num_start, num_end)):
                        self.part_sum += number
                    else:
                        a = None

    def _has_adjecent_symbol(self, num_coords: ((int, int), (int, int))) -> bool:
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
                    return True

        return False

    def _is_next_char_digit(self, coords: (int, int)) -> bool:
        y, x = coords

        if x == self.x_max:
            return False
        elif self.schematic[y][x+1] in string.digits:
            return True

        return False

    def get_part_sum(self) -> int:
        return self.part_sum


if __name__ == '__main__':
    main()
