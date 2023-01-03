import sys
from itertools import cycle

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    field = Field(aoc_input)
    for i in range(10):
        field.first_half()
        field.second_half()
    return field.get_empty_tiles()


def part_two(aoc_input) -> int:
    # ToDo: Improve runtime (Took 11 minutes like this)
    field = Field(aoc_input)
    plant_round = 0
    while field.has_elf_moved_in_round:
        field.first_half()
        field.second_half()
        plant_round += 1
    return plant_round


class Field:
    def __init__(self, aoc_input):
        self.considered_directions = cycle(['N', 'S', 'W', 'E'])
        self.directions = [next(self.considered_directions) for _ in range(4)]
        self.elves = []
        self.elf_positions = []
        self.has_elf_moved_in_round = True
        self.considered_positions = {}  # Keeps track of how many elves consider the same position
        self._init_field(aoc_input)

    def _init_field(self, aoc_input):
        """Initializes all elves on the field."""
        for y, row in enumerate(aoc_input):
            for x, col in enumerate(row):
                if col == '#':
                    self.elves.append(Elf((x, y)))
                    self.elf_positions.append((x, y))

    def first_half(self):
        """The first half of one round. All elfs consider their next move."""
        for elf in self.elves:
            elf_dir = elf.consider_direction(self.elf_positions, self.directions)
            if elf_dir == (None, None):
                continue
            if elf_dir not in self.considered_positions.keys():
                self.considered_positions[elf_dir] = 1
            else:
                self.considered_positions[elf_dir] += 1

    def second_half(self):
        """Second half of one round. All elfs move to their next position,
        unless two or more elves consider the same position."""
        self.has_elf_moved_in_round = False
        for elf in self.elves:
            if elf.next_position in self.considered_positions.keys() \
                    and self.considered_positions[elf.next_position] < 2:
                elf.move()
                self.has_elf_moved_in_round = True

        self._end_of_round()

    def _end_of_round(self):
        """Finalizes a round, by preparing the iterators for the next round, and clearing considered positions"""
        next(self.considered_directions)  # advance first consideration to next direction
        self.directions = [next(self.considered_directions) for _ in range(4)]
        self.elf_positions = [elf.position for elf in self.elves]
        self.considered_positions.clear()

    def get_empty_tiles(self) -> int:
        """Return the number of empty tiles in the smallest rectangle"""
        empty_tiles = 0
        x_vals = [x for x, y in self.elf_positions]
        min_x, max_x = min(x_vals), max(x_vals)
        y_vals = [y for x, y in self.elf_positions]
        min_y, max_y = min(y_vals), max(y_vals)
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if (x, y) not in self.elf_positions:
                    empty_tiles += 1
        return empty_tiles


class Elf:
    ADJACENTS = {'N': (0, -1), 'NE': (1, -1), 'NW': (-1, -1),
                 'S': (0, 1), 'SE': (1, 1), 'SW': (-1, 1),
                 'W': (-1, 0),
                 'E': (1, 0)}

    def __init__(self, position: tuple):
        self.position = position
        self.neighbours = self._get_neighbours()
        self.next_position = ()

    def _get_neighbours(self) -> list:
        """Returns all neighbouring coordinates from current position."""
        ret = []
        for offs in self.ADJACENTS.values():
            ret.append(self._tuple_add(offs, self.position))
        return ret

    def consider_direction(self, elf_positions: list, directions: list[str]) -> tuple:
        """Determins the next position

        :param elf_positions: List with the current position of all elves
        :param directions: List of directions in the order they should be considered
        :return: Next direction the elf will go to. (None, None) if the elf doesn't walk.
        """
        if all([neighbour not in elf_positions for neighbour in self.neighbours]):
            self.next_position = (None, None)
            return self.next_position  # no elf in neighbouring tiles

        for direction in directions:
            # check the three tiles ahead for an elf
            forward_tiles = [self._tuple_add(self.position, value) for key, value in self.ADJACENTS.items()
                             if direction in key]
            if all([forward_tile not in elf_positions for forward_tile in forward_tiles]):
                # If no elf occupies one of the three tiles, the elf can go towards "direction"
                self.next_position = self._tuple_add(self.position, self.ADJACENTS[direction])
                return self.next_position

        self.next_position = (None, None)
        return self.next_position

    def move(self):
        """Moves to the next position and updates neighbours"""
        if self.next_position == (None, None):  # elf doesn't move
            return

        self.position = self.next_position
        self.neighbours = self._get_neighbours()

    @staticmethod
    def _tuple_add(a, b):
        return a[0] + b[0], a[1] + b[1]


if __name__ == '__main__':
    main()
