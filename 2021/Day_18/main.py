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
        self.__current_depth = 0
        self.__reduce()
        bla = [[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]

    def __add__(self, other):
        return SnailNum(str([self.num, other.num]))

    def __eq__(self, other):
        return self.num == other.num

    def __repr__(self):
        return str(self.num)

    def name(self):
        return str(self.num)

    def __reduce(self):
        """
        Snailfish numbers must always be reduced. To reduce a snailfish number,
        you must repeatedly do the first action in this list that applies to the snailfish number:
        1. If any pair is nested inside four pairs, the leftmost such pair explodes.
        2. If any regular number is 10 or greater, the leftmost such regular number splits.
        Once no action in the above list applies, the snailfish number is reduced.
        """
        is_add_done = False
        while not is_add_done:
            if self.depth() == 5:
                self.__explode(self.num)
                # ToDo: implement carry over to the left (not sure where)
                self.__left_num = None  # if number was not added, there was no matching regular number
                self.__right_num = None  # if number was not added, there was no matching regular number
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
            sub_list = self.__explode(num[0])  # process next list
            # -> left list of 'num' will explode
            if isinstance(sub_list[0], int) and isinstance(sub_list[1], int) \
                    and self.__current_depth == 4 and not self.__has_exploded:
                num[0] = 0
                # since we are in depth 4 num[1] must contain two numbers,
                # thats why I can just add the right number from the exploding pair
                num[1][0] += sub_list[1]
                self.__left_num = sub_list[0]  # remember left number of sub list
                self.__has_exploded = True
                self.__current_depth -= 1
                return num  # return required here, so that next if is not executed

            sub_list = self.__explode(num[1])  # process next list
            # -> right list of 'num' will explode
            if isinstance(sub_list[0], int) and isinstance(sub_list[1], int) \
                    and self.__current_depth == 4 and not self.__has_exploded:
                num[1] = 0
                # since we are in depth 4 num[0] must contain two numbers,
                # thats why I can just add the left number from the exploding pair
                num[0][1] += sub_list[0]
                self.__right_num = sub_list[1]  # remember right number of sub list
                self.__has_exploded = True
                self.__current_depth -= 1
                return num  # return required here, so that next if is not executed
        # [list, int]
        elif isinstance(num[0], list) and isinstance(num[1], int):
            # ToDo: Do I need to add left? Could this happen?
            sub_list = self.__explode(num[0])  # process next list
            # add right num, if one was saved
            # if self.__right_num is not None:
            #     # ToDo: Can this ever happen? (Going out only left side? / Going in only right side?)
            #     # num[0] += self.__right_num
            #     # self.__right_num = None

            # -> left list of 'num' will explode
            if isinstance(sub_list[0], int) and isinstance(sub_list[1], int) \
                    and self.__current_depth == 4 and not self.__has_exploded:
                num[0] = 0
                num[1] += sub_list[1]
                self.__left_num = sub_list[0]  # remember left number of sub list
                self.__has_exploded = True
                self.__current_depth -= 1
                return num  # return required here, so that next if is not executed
        # [int, list]
        elif isinstance(num[0], int) and isinstance(num[1], list):
            # add right num, if one was saved
            if self.__right_num is not None:
                num[0] += self.__right_num
                self.__right_num = None

            sub_list = self.__explode(num[1])  # process next list
            # add left num, if one was saved
            if self.__left_num is not None:
                num[0] += self.__left_num
                self.__left_num = None

            # -> right list of 'num' will explode
            if isinstance(sub_list[0], int) and isinstance(sub_list[1], int) \
                    and self.__current_depth == 4 and not self.__has_exploded:
                num[0] += sub_list[0]
                num[1] = 0
                self.__right_num = sub_list[1]  # remember right number of sub list
                self.__has_exploded = True
                self.__current_depth -= 1
                return num  # return required here, so that next if is not executed
        # [int, int]
        elif isinstance(num[0], int) and isinstance(num[1], int):
            # add right num, if one was saved
            if self.__right_num is not None:
                num[0] += self.__right_num
                self.__right_num = None

            self.__current_depth -= 1
            return num
        else:
            raise Exception("SomeWeirdError")

        self.__current_depth -= 1
        return [None, None]

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

    def __magnitude(self, num) -> int:
        for part in num:
            # [list, list]
            if isinstance(num[0], list) and isinstance(num[1], list):
                return 3 * self.__magnitude(num[0]) + 2 * self.__magnitude(num[1])
            # [list, int]
            elif isinstance(num[0], list) and isinstance(num[1], int):
                return 3 * self.__magnitude(num[0]) + 2 * num[1]
            # [int, list]
            elif isinstance(num[0], int) and isinstance(num[1], list):
                return 3 * num[0] + 2 * self.__magnitude(num[1])
            # [int, int]
            elif isinstance(num[0], int) and isinstance(num[1], int):
                return 3 * num[0] + 2 * num[1]
            else:
                raise Exception('SomeWeirdError')

    def magnitude(self) -> int:
        return self.__magnitude(self.num)


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
