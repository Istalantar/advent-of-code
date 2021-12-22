import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class SnailNum:
    def __init__(self, num: str):
        self.num = eval(num)

    def __add__(self, other):
        res = [self.num, other.num]
        if self.depth() == 5:
            self.__explode()
        return res

    def __repr__(self):
        return str(self.num)

    def __explode(self):
        pass

    def __split(self):
        pass

    def depth(self) -> int:
        return self.__depth(self.num)

    def __depth(self, num) -> int:
        if isinstance(num, list):
            return 1 + max(self.__depth(item) for item in num)
        else:
            return 0


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    # print(part_two(content))


def part_one(content) -> int:
    a = SnailNum('[1, 2]')
    b = SnailNum('[[3, 4], 5]')
    c = a + b
    d = SnailNum('[[[[[9,8],1],2],3],4]')
    e = d.depth()

    return 0


def part_two(content) -> int:

    return 0


if __name__ == '__main__':
    main()
