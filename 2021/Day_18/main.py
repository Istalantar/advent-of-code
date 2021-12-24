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
        self.__do_split = True
        self.__has_exploded = False
        self.__left_num = None
        self.__right_num = None
        self.__inward = True  # False is outward
        self.__current_depth = 0
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
                # self.__add_saved_num(self.num)
                self.__has_exploded = False
                continue
            elif self.__do_split:
                self.__do_split = False
                self.__split(self.num)
                continue
            else:
                is_add_done = True

    def __explode(self, num) -> list:
        self.__current_depth += 1

        # [list, list]
        if isinstance(num[0], list) and isinstance(num[1], list):
            self.__explode(num[0])
            self.__explode(num[1])
        # [list, int]
        elif isinstance(num[0], list) and isinstance(num[1], int):
            sub_list = self.__explode(num[0])
            # -> left list of 'num' will explode
            if isinstance(sub_list[0], int) and isinstance(sub_list[1], int) and not self.__has_exploded:
                num[0] = 0
                num[1] += sub_list[1]
                self.__left_num = sub_list[0]  # remember left number of sub list
                self.__has_exploded = True
                self.__current_depth -= 1
                return num  # return required here, so that next if is not executed
        # [int, list]
        elif isinstance(num[0], int) and isinstance(num[1], list):
            sub_list = self.__explode(num[1])
            # -> right list of 'num' will explode
            if isinstance(sub_list[0], int) and isinstance(sub_list[1], int) and not self.__has_exploded:
                num[0] += sub_list[0]
                num[1] = 0
                self.__right_num = sub_list[1]  # remember right number of sub list
                self.__has_exploded = True
                self.__current_depth -= 1
                return num  # return required here, so that next if is not executed
        # [int, int]
        elif isinstance(num[0], int) and isinstance(num[1], int) and self.__current_depth == 5:
            self.__current_depth -= 1
            return num
        elif isinstance(num[0], int) and isinstance(num[1], int) and self.__current_depth < 5:
            # nothing to do here, just needed for the condition to pass through, in ordner to not raise the exception
            pass
        else:
            raise Exception("SomeWeirdError")

        # when leaving tree, add remembered number to first left/right number
        # ToDo: get carry over working
        if self.__right_num is not None and not self.__inward and isinstance(num[1], int):
            num[1] += self.__right_num
            self.__right_num = None
        if self.__left_num is not None and not self.__inward and isinstance(num[0], int):
            num[1] += self.__left_num
            self.__left_num = None

        self.__current_depth -= 1
        return [None, None]

    def __add_saved_num(self, num):
        self.__current_depth += 1

        if self.__right_num is not None and isinstance(num[1], int) and self.__current_depth == 1:
            # only on depth one can a right number be the first regular number on the right
            num[1] += self.__right_num
            self.__right_num = None
        elif self.__right_num is not None and isinstance(num[0], int) and self.__current_depth != 1:
            num[0] += self.__right_num
            self.__right_num = None
        elif self.__right_num is not None and isinstance(num[1], list):
            self.__add_saved_num(num[1])
        elif self.__left_num is not None and isinstance(num[0], int) and self.__current_depth == 1:
            # only on depth one can a left number be the first regular number on the left
            num[0] += self.__left_num
            self.__left_num = None
        elif self.__left_num is not None and isinstance(num[1], int) and self.__current_depth != 1:
            num[1] += self.__left_num
            self.__left_num = None
        elif self.__left_num is not None and isinstance(num[0], list):
            self.__add_saved_num(num[0])
        else:
            raise Exception('SomeWeirdError')

        self.__current_depth -= 1

    def __split(self, num):
        if isinstance(num[0], int):
            if num[0] > 9:
                num[0] = [floor(num[0] / 2), ceil(num[0] / 2)]
                self.__do_split = True
        else:
            self.__split(num[0])
        if isinstance(num[1], int):
            if num[1] > 9:
                num[1] = [floor(num[1] / 2), ceil(num[1] / 2)]
                self.__do_split = True
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
