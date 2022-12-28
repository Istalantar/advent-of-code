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

        if name == 'root':
            open_operations.append(Monkey(name, *map(str.strip, operation.split('+')), '=='))
            continue

        for operator in ['+', '-', '*', '/']:
            if operator in operation:
                open_operations.append(Monkey(name, *map(str.strip, operation.split(operator)), operator))

    # ToDo: try to solve as equation (substitute strings maybe)
    for humn in range(1001, 10001):
        temp_numbers = numbers.copy()
        temp_open_ops = open_operations.copy()
        temp_numbers['humn'] = humn
        while 'root' not in temp_numbers.keys():
            for monkey in temp_open_ops.copy():
                if monkey.left in temp_numbers and monkey.right in temp_numbers:
                    if monkey.name == 'root' and monkey.do_operation(temp_numbers[monkey.left],
                                                                     temp_numbers[monkey.right]) is True:
                        return humn
                    temp_numbers[monkey.name] = monkey.do_operation(temp_numbers[monkey.left],
                                                                    temp_numbers[monkey.right])
                    temp_open_ops.remove(monkey)
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
