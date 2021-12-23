import sys
from math import ceil, floor

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class SnailNum:
    # there are four types of snail numbers
    # [list, list]
    # [list, int]
    # [int, list]
    # [int, int]
    def __init__(self, num: str):
        self.num = eval(num)
        self.do_split = True
        self.left_num = None
        self.right_num = None
        self.__reduce()

    def __add__(self, other):
        return SnailNum(str([self.num, other.num]))

    def __eq__(self, other):
        return self.num == other.num

    def __repr__(self):
        return str(self.num)

    def name(self):
        return str(self.num)

    def __reduce(self):
        is_add_done = False
        while not is_add_done:
            if self.depth() == 5:
                self.__explode(self.num)
                continue
            elif self.do_split:
                self.do_split = False
                self.__split(self.num)
                continue
            else:
                is_add_done = True

    def __explode(self, num) -> list:
        # num is int
        if isinstance(num, int):
            # ToDo: Do I need to do something here?
            pass
        # [list, list]
        elif isinstance(num[0], list) or isinstance(num[1], list):
            self.__explode(num[0])
            self.__explode(num[1])
        # [list, int]
        elif isinstance(num[0], list) and isinstance(num[1], int):
            if self.left_num is not None:
                num[1] += self.left_num
                self.left_num = None
            sub_list = self.__explode(num[0])
            if isinstance(sub_list[0], int) and isinstance(sub_list[1], int):  # -> left list of 'num' will explode
                num[0] = 0
                num[1] += sub_list[1]
                self.left_num = sub_list[0]  # remember left number of sub list
        # [int, list]
        elif isinstance(num[0], int) and isinstance(num[1], list):
            if self.right_num is not None:
                num[0] += self.right_num
                self.right_num = None
            sub_list = self.__explode(num[1])
            if isinstance(sub_list[0], int) and isinstance(sub_list[1], int):  # -> right list of 'num' will explode
                num[0] += sub_list[0]
                num[1] = 0
                self.right_num = sub_list[1]  # remember right number of sub list
        # [int, int]
        elif isinstance(num[0], int) and isinstance(num[1], int):
            return num
        else:
            raise Exception("SomeWeirdError")

    def __split(self, num):
        if isinstance(num[0], int):
            if num[0] > 9:
                num[0] = [floor(num[0] / 2), ceil(num[0] / 2)]
                self.do_split = True
        else:
            self.__split(num[0])
        if isinstance(num[1], int):
            if num[1] > 9:
                num[1] = [floor(num[1] / 2), ceil(num[1] / 2)]
                self.do_split = True
        else:  # call next list
            self.__split(num[1])

    def __depth(self, num) -> int:
        if isinstance(num, list):
            return 1 + max(self.__depth(item) for item in num)
        else:
            return 0

    def depth(self) -> int:
        return self.__depth(self.num)

    def magnitude(self) -> int:
        # ToDo: get the magnitude of the number
        return -1


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    # print(part_two(content))


def part_one(content) -> int:
    a = SnailNum('[[13, 4], 15]')
    print(a)

    return 0


def part_two(content) -> int:
    return 0


if __name__ == '__main__':
    main()
