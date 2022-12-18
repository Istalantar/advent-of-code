import sys
import itertools

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    print(part_one(aoc_input))
    print(part_two(aoc_input))


def part_one(aoc_input) -> int:
    tetris = Tetris(aoc_input.strip())
    while tetris.fallen_rocks < 2022:
        tetris.move()
    return tetris.tower_height


def part_two(aoc_input) -> int:
    # ToDo: Improve runtime
    raise NotImplementedError
    # tetris = Tetris(aoc_input.strip())
    # while tetris.fallen_rocks < 1_000_000_000_000:
    #     tetris.move()
    # return tetris.tower_height


class Tetris:
    def __init__(self, jet: str):
        """Initializes the Pyroclastic Flow

        The floor is at y = 0, so that first rock lands on y = 1,
        this makes y the total height of the tower.
        The left wall is at -1, so that 0 can be occupied by a rock.
        The start position of the first rock is (x, y) = (1, 4)
        The bottom left point of a rock is (dx, dy) = (0, 0)
        """
        self.rocks = itertools.cycle([['####'],
                                      ['.#.',
                                       '###',
                                       '.#.'],
                                      ['..#',
                                       '..#',
                                       '###'],
                                      ['#',
                                       '#',
                                       '#',
                                       '#'],
                                      ['##',
                                       '##']])
        self.rock = next(self.rocks)
        self.jet = itertools.cycle(jet)
        self.cave_width = 7
        self.tower_height = 0
        self.tower = ['#' * 7]  # index 0 is floor
        self.rock_height = len(self.rock)
        self.rock_width = len(self.rock[0])
        self.rock_x = 2
        self.rock_y = 4
        self.is_rock_falling = True
        self.fallen_rocks = 0

    def move(self):
        """Rock gets pushed by jet and then falls down one unit"""
        if not self.is_rock_falling:
            self._get_next_rock()

        # Jet pushes rock
        jet = next(self.jet)
        if jet == '<' and self.rock_x > 0 and self._is_left_free():
            self.rock_x -= 1
        elif jet == '>' and self.rock_x + self.rock_width - 1 < 6 and self._is_right_free():
            self.rock_x += 1

        # Rock falls .. or lands
        for row, rock_part in enumerate(self.rock[::-1]):
            for col, val in enumerate(rock_part):
                if val == '.':
                    continue

                if self.rock_y + row - 1 <= self.tower_height \
                        and self.tower[self.rock_y + row - 1][self.rock_x + col] == '#':
                    self._land_rock()
                    return

        self.rock_y -= 1

    def _get_next_rock(self):
        """Next falling rock gets initialized"""
        self.rock = next(self.rocks)
        self.rock_x = 2
        self.rock_y = self.tower_height + 4
        self.rock_height = len(self.rock)
        self.rock_width = len(self.rock[0])
        self.is_rock_falling = True

    def _land_rock(self):
        """Rock lands on floor or already fallen rocks,
        which means it gets added to the tower"""
        for row, rock_part in enumerate(self.rock[::-1]):  # inverse, because bottom part of rock lands first
            left_padding = '.' * self.rock_x
            right_padding = '.' * (self.cave_width - self.rock_width - self.rock_x)
            landing_row = left_padding + rock_part + right_padding

            if self.rock_y + row <= self.tower_height:
                # rock part is not landing on top, so the tower pieces need to be considered
                adjusted_tower_row = ''
                for choice in zip(self.tower[self.rock_y + row], landing_row):
                    adjusted_tower_row += '#' if '#' in choice else '.'
                self.tower[self.rock_y + row] = adjusted_tower_row
            else:
                # part of rock lands on top of tower
                self.tower_height += 1
                self.tower.append(landing_row)

        self.is_rock_falling = False
        self.fallen_rocks += 1
        if self.fallen_rocks % 100 == 0:
            print(self.fallen_rocks)

    def _is_left_free(self) -> bool:
        for row, rock_part in enumerate(self.rock[::-1]):  # inspect from bottom to top
            if self.rock_y + row > self.tower_height:
                return True

            for col, rock_piece in enumerate(rock_part):
                if rock_piece == '#' and self.tower[self.rock_y + row][self.rock_x - 1 + col] == '#':
                    return False

        return True

    def _is_right_free(self) -> bool:
        for row, rock_part in enumerate(self.rock[::-1]):  # inspect from bottom to top
            if self.rock_y + row > self.tower_height:
                return True

            for col, rock_piece in enumerate(rock_part[::-1]):  # inspect from right to left
                if rock_piece == '#' and self.tower[self.rock_y + row][self.rock_x + self.rock_width - col] == '#':
                    return False

        return True


if __name__ == '__main__':
    main()
