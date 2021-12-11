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

    def increase_step(self) -> int:
        """

        :return: 0 if none ore some octopi flashed, 1 if all octopi flashed at once
        """
        ret = 0
        self.step_count += 1
        self.octopi = list(list(map(lambda x: x + 1, row)) for row in self.octopi)
        while self.__check_flash():
            pass

        if self.__do_all_flash():
            ret = 1

        return ret

    def __check_flash(self) -> bool:
        """
        Checks if the octopusses flashed.
        :return: Returns True if flash happened, False if no octpus flashed
        """
        has_flashed = False

        for y, row in enumerate(self.octopi):
            for x in range(self.max_x):
                if self.octopi[y][x] > 9:
                    has_flashed = True
                    self.octopi[y][x] = 0
                    self.flash_count += 1
                    self.__increase_adjacent(x, y)

        return has_flashed

    def __do_all_flash(self) -> bool:
        return bool(sum(sum(self.octopi, [])))

    def __increase_adjacent(self, x, y):
        # upper left
        if (y - 1) >= 0 and (x - 1) >= 0 and self.octopi[y - 1][x - 1] != 0:
            self.octopi[y - 1][x - 1] += 1
        # upper
        if (y - 1) >= 0 and self.octopi[y - 1][x] != 0:
            self.octopi[y - 1][x] += 1
        # upper right
        if (y - 1) >= 0 and (x + 1) < self.max_x and self.octopi[y - 1][x + 1] != 0:
            self.octopi[y - 1][x + 1] += 1
        # left
        if (x - 1) >= 0 and self.octopi[y][x - 1] != 0:
            self.octopi[y][x - 1] += 1
        # right
        if (x + 1) < self.max_x and self.octopi[y][x + 1] != 0:
            self.octopi[y][x + 1] += 1
        # lower left
        if (y + 1) < self.max_y and (x - 1) >= 0 and self.octopi[y + 1][x - 1] != 0:
            self.octopi[y + 1][x - 1] += 1
        # lower
        if (y + 1) < self.max_y and self.octopi[y + 1][x] != 0:
            self.octopi[y + 1][x] += 1
        # lower left
        if (y + 1) < self.max_y and (x + 1) < self.max_x and self.octopi[y + 1][x + 1] != 0:
            self.octopi[y + 1][x + 1] += 1


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    my_octopuses = Octopuses(content)
    for i in range(100):
        my_octopuses.increase_step()

    return my_octopuses.flash_count


def part_two(content) -> int:
    my_octopuses = Octopuses(content)
    while my_octopuses.increase_step():
        pass

    return my_octopuses.step_count


if __name__ == '__main__':
    main()
