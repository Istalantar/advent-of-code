import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class Octopuses:
    def __init__(self, cave):
        self.octopi = [[int(octo) for octo in row] for row in cave]
        self.max_y = len(self.octopi)
        self.max_x = len(self.octopi[0])
        self.flash_count = 0
        self.step_count = 0

    def increase_step(self):
        self.step_count += 1
        self.octopi = list(list(map(lambda x: x + 1, row)) for row in self.octopi)
        self.__check_flash()

    def __check_flash(self):
        for y, row in enumerate(self.octopi):
            for x in range(self.max_x):
                # upper left
                if (y - 1) >= 0 and (x - 1) >= 0 and self.octopi[y][x] > 9:
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)
                # upper
                if (y - 1) >= 0:
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)
                # upper right
                if (y - 1) >= 0 and (x + 1) <= self.max_x:
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)
                # left
                if (x - 1) >= 0:
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)
                # right
                if (x + 1) <= self.max_x:
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)
                # lower left
                if (y + 1) <= self.max_y and (x - 1) >= 0:
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)
                # lower
                if (y + 1) <= self.max_y:
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)
                # lower right
                if (y + 1) <= self.max_y and (x + 1) <= self.max_x:
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)
                pass

    def __increase_adjacent(self, x, y):
        has_increased = False

        # upper left
        if (y - 1) >= 0 and (x - 1) >= 0 and self.octopi[y - 1][x - 1] != 0:
            self.octopi[y][x] += 1
            has_increased = True
        # upper
        if (y - 1) >= 0 and self.octopi[y - 1][x] != 0:
            self.octopi[y - 1][x] += 1
            has_increased = True
        # upper right
        if (y - 1) >= 0 and (x + 1) <= self.max_x and self.octopi[y - 1][x + 1] != 0:
            self.octopi[y - 1][x + 1] += 1
            has_increased = True
        # left
        if (x - 1) >= 0 and self.octopi[y][x - 1] != 0:
            self.octopi[y][x - 1] += 1
            has_increased = True
        # right
        if (x + 1) < self.max_x and self.octopi[y][x + 1] != 0:
            self.octopi[y][x + 1] += 1
            has_increased = True
        # lower left
        if (y + 1) <= self.max_y and (x - 1) >= 0 and self.octopi[y + 1][x - 1] != 0:
            self.octopi[y + 1][x - 1] += 1
            has_increased = True
        # lower
        if (y + 1) < self.max_y and self.octopi[y + 1][x] != 0:
            self.octopi[y + 1][x] += 1
            has_increased = True
        # lower left
        if (y + 1) <= self.max_y and (x + 1) <= self.max_x and self.octopi[y + 1][x + 1] != 0:
            self.octopi[y + 1][x + 1] += 1
            has_increased = True

        if has_increased:
            self.__check_flash()


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    my_octopuses = Octopuses(content)
    for i in range(100):
        my_octopuses.increase_step()

    return 0


def part_two(content) -> int:
    return 0


if __name__ == '__main__':
    main()
