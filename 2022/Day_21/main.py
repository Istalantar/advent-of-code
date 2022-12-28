import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    numbers = {}
    open_operations = []
    for monkey in aoc_input:
        assert isinstance(monkey, str)
        name: str
        operation: str
        name, operation = monkey.split(': ')
        if operation.isnumeric():
            numbers[name] = int(operation)
            continue

        for operator in ['+', '-', '*', '/']:
            if operator in operation:
                open_operations.append(Monkey(name, *map(str.strip, operation.split(operator)), operator))

    while 'root' not in numbers.keys():
        for monkey in open_operations.copy():
            if monkey.left in numbers and monkey.right in numbers:
                numbers[monkey.name] = monkey.do_operation(numbers[monkey.left], numbers[monkey.right])
                open_operations.remove(monkey)
    return int(numbers['root'])


def part_two(aoc_input) -> int:
    return -1


class Monkey:
    def __init__(self, name: str, left: str, right: str, operation: str):
        self.name = name
        self.left = left
        self.right = right
        self.operation = operation

    def do_operation(self, left, right):
        return eval(str(left) + self.operation + str(right))


if __name__ == '__main__':
    main()
