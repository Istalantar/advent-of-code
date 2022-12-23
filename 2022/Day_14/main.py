import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    cave = Cave(aoc_input)
    while not cave.has_reached_void:
        cave.sand_fall()
    return cave.sand_units


def part_two(aoc_input) -> int:
    cave = Cave(aoc_input)
    cave.max_y += 2
    while not cave.has_reached_void:
        cave.sand_fall()
    return cave.sand_units


class Cave:
    def __init__(self, aoc_input):
        self.sand_x = 500
        self.sand_y = 0
        self.sand_units = 0
        self.cave = {}
        self.has_reached_void = False
        self._build_walls(aoc_input)
        self.max_y = max([y for _, y in self.cave.keys()])  # end of cave

    def sand_fall(self):
        """Lets sand fall down one unit, and checks for walls to know where the sand can fall."""
        if self.sand_y > self.max_y:
            self.has_reached_void = True
            return

        # sand falls straight
        if self.cave.get((self.sand_x, self.sand_y + 1)) is None:
            self.sand_y += 1
            return

        # sand falls down-left
        if self.cave.get((self.sand_x - 1, self.sand_y + 1)) is None:
            self.sand_x -= 1
            self.sand_y += 1
            return

        # sand falls down-right
        if self.cave.get((self.sand_x + 1, self.sand_y + 1)) is None:
            self.sand_x += 1
            self.sand_y += 1
            return

        # if sand does not fall, it landed
        self.cave[(self.sand_x, self.sand_y)] = '#'
        self.sand_units += 1
        self._get_next_sand()
        return

    def _get_next_sand(self):
        """Initializes the next falling pebble of sand"""
        self.sand_x = 500
        self.sand_y = 0

    def _build_walls(self, aoc_input):
        """Builds the wall of the cave from the input coordinates"""
        for wall in aoc_input:
            assert isinstance(wall, str)
            points = list(map(str.strip, wall.split('->')))
            wall_points = []
            for point in points:
                x, y = map(int, point.split(','))
                # collect all points of one wall
                wall_points.append((x, y))

            # build wall from collected points
            for a, b in zip(wall_points, wall_points[1:]):
                if a[0] == b[0]:  # vertical piece of wall
                    for y in range(min(a[1], b[1]), max(a[1], b[1] + 1)):
                        self.cave[(a[0], y)] = '#'
                elif a[1] == b[1]:  # horizontal piece of wall
                    for x in range(min(a[0], b[0]), max(a[0], b[0] + 1)):
                        self.cave[(x, a[1])] = '#'
                else:
                    raise Exception(f'WallError: Expected horizontal/vertical wall, got diagonal wall. ({a=}, {b=})')


if __name__ == '__main__':
    main()
