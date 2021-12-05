import sys
import copy

sys.path.append('../..')
from myFunctions import my_input_list, my_input_string  # noqa E402


class WaitingArea:
    def __init__(self, content):
        self.num_rows = 0
        self.num_cols = 0
        self.layout = []
        self.__get_layout(content)

    def __get_layout(self, content):
        self.num_rows = len(content)
        self.num_cols = len(content[0])

        for y, row in enumerate(content):
            self.layout.append([])
            for x, val in enumerate(row):
                self.layout[y].append(val)

    def run_rules(self) -> bool:
        """
        Performs the rules on the seating area
        :return: Returns False if nothing has changed
        """
        has_seat_changed = False
        new_layout = copy.deepcopy(self.layout)
        for y, row in enumerate(self.layout):
            for x, val in enumerate(row):
                # seat becomes occupied
                if val == 'L' and self.__is_adj_empty(x, y):
                    new_layout[y][x] = '#'
                    has_seat_changed = True
                # seat becomes empty
                elif val == '#' and self.__is_adj_occ(x, y):
                    new_layout[y][x] = 'L'
                    has_seat_changed = True

        self.layout = new_layout.copy()
        return has_seat_changed

    def count_occ_seats(self) -> int:
        occ_seats = 0

        for row in self.layout:
            for val in row:
                if val in '#':
                    occ_seats += 1

        return occ_seats

    def __is_adj_empty(self, x, y) -> bool:
        """
        :param x: Seat column
        :param y: Seat row
        :return: Returns True if all adjacent seats are empty
        """
        ret_val = True
        max_x = len(self.layout[0]) - 1
        max_y = len(self.layout) - 1
        try:
            # upper left
            if (y - 1) >= 0 and (x - 1) >= 0 and self.layout[y - 1][x - 1] not in ('L', '.'):
                return False
            # upper
            if (y - 1) >= 0 and self.layout[y - 1][x] not in ('L', '.'):
                return False
            # upper right
            if (y - 1) >= 0 and (x + 1) <= max_x and self.layout[y - 1][x + 1] not in ('L', '.'):
                return False
            # left
            if (x - 1) >= 0 and self.layout[y][x-1] not in ('L', '.'):
                return False
            # right
            if (x + 1) <= max_x and self.layout[y][x + 1] not in ('L', '.'):
                return False
            # lower left
            if (y + 1) <= max_y and (x - 1) >= 0 and self.layout[y + 1][x - 1] not in ('L', '.'):
                return False
            # lower
            if (y + 1) <= max_y and self.layout[y + 1][x] not in ('L', '.'):
                return False
            # lower right
            if (y + 1) <= max_y and (x + 1) <= max_x and self.layout[y + 1][x + 1] not in ('L', '.'):
                return False
        except IndexError:
            print("Index Error")
        return ret_val

    def __is_adj_occ(self, x, y) -> bool:
        """
        :param x: Seat column
        :param y: Seat row
        :return: Returns True if four or more adjacent seats are occupied
        """
        seats_occ = 0
        max_x = len(self.layout[0]) - 1
        max_y = len(self.layout) - 1
        try:
            # upper left
            if (y - 1) >= 0 and (x - 1) >= 0 and self.layout[y - 1][x - 1] in '#':
                seats_occ += 1
            # upper
            if (y - 1) >= 0 and self.layout[y - 1][x] in '#':
                seats_occ += 1
            # upper right
            if (y - 1) >= 0 and (x + 1) <= max_x and self.layout[y - 1][x + 1] in '#':
                seats_occ += 1
            # left
            if (x - 1) >= 0 and self.layout[y][x - 1] in '#':
                seats_occ += 1
            # right
            if (x + 1) <= max_x and self.layout[y][x + 1] in '#':
                seats_occ += 1
            # lower left
            if (y + 1) <= max_y and (x - 1) >= 0 and self.layout[y + 1][x - 1] in '#':
                seats_occ += 1
            # lower
            if (y + 1) <= max_y and self.layout[y + 1][x] in '#':
                seats_occ += 1
            # lower right
            if (y + 1) <= max_y and (x + 1) <= max_x and self.layout[y + 1][x + 1] in '#':
                seats_occ += 1
        except IndexError:
            print("Index Error")
        return True if seats_occ >= 4 else False


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    executed_rules = 0
    my_area = WaitingArea(content)
    while my_area.run_rules():
        executed_rules += 1
    return my_area.count_occ_seats()


def part_two(content) -> int:
    res = 0
    return res


if __name__ == '__main__':
    main()
