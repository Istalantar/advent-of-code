import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class Vents:
    vent_count = {}  # {(x, y): vent_count}

    def __init__(self, line: str, part: int):
        self.is_horizontal = False
        self.is_vertical = False
        self.v_start: (int(), int())
        self.v_end: (int(), int())
        self.part = part
        self.__get_coordinates(line)
        self.__get_vent_count()

    def __get_coordinates(self, line):
        temp = line.split("->")
        self.v_start = tuple(int(val) for val in temp[0].split(','))
        self.v_end = tuple(int(val) for val in temp[1].split(','))
        self.is_vertical = True if self.v_start[0] == self.v_end[0] else False
        self.is_horizontal = True if self.v_start[1] == self.v_end[1] else False

    def __get_vent_count(self):
        x1, y1, x2, y2 = self.v_start[0], self.v_start[1], self.v_end[0], self.v_end[1]

        if self.is_vertical:
            y = y1 if y1 < y2 else y2
            for i in range(abs(y2 - y1) + 1):
                if self.vent_count.get((x1, y + i)) is None:
                    self.vent_count[(x1, y + i)] = 1
                else:
                    self.vent_count[(x1, y + i)] += 1
        elif self.is_horizontal:
            x = x1 if x1 < x2 else x2
            for i in range(abs(x2 - x1) + 1):
                if self.vent_count.get((x + i, y1)) is None:
                    self.vent_count[(x + i, y1)] = 1
                else:
                    self.vent_count[(x + i, y1)] += 1
        else:
            if self.part == 2:
                x = x1
                y = y1

                for i in range(abs(x2 - x1) + 1):
                    if y2 > y1 and x2 > x1:
                        if self.vent_count.get((x + i, y + i)) is None:
                            self.vent_count[(x + i, y + i)] = 1
                        else:
                            self.vent_count[(x + i, y + i)] += 1
                    elif y2 < y1 and x2 < x1:
                        if self.vent_count.get((x - i, y - i)) is None:
                            self.vent_count[(x - i, y - i)] = 1
                        else:
                            self.vent_count[(x - i, y - i)] += 1
                    elif y2 > y1 and x2 < x1:
                        if self.vent_count.get((x - i, y + i)) is None:
                            self.vent_count[(x - i, y + i)] = 1
                        else:
                            self.vent_count[(x - i, y + i)] += 1
                    elif y2 < y1 and x2 > x1:
                        if self.vent_count.get((x + i, y - i)) is None:
                            self.vent_count[(x + i, y - i)] = 1
                        else:
                            self.vent_count[(x + i, y - i)] += 1


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    vents = [Vents]
    for line in content:
        vents.append(Vents(line, 1))

    more_than_one = 0
    for index, value in Vents.vent_count.items():
        more_than_one += 1 if value > 1 else 0

    return more_than_one


def part_two(content) -> int:
    Vents.vent_count.clear()
    vents = [Vents]
    for line in content:
        vents.append(Vents(line, 2))

    more_than_one = 0
    for index, value in Vents.vent_count.items():
        more_than_one += 1 if value > 1 else 0

    return more_than_one


if __name__ == '__main__':
    main()
