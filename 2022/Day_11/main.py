import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    print(part_one(aoc_input))
    print(part_two(aoc_input))


def part_one(aoc_input) -> int:
    monkeys = []
    slinging_round = 0
    for i_monkey in map(str.strip, aoc_input.split('\n\n')):
        start = operation = test = t_true = t_false = None
        for line in map(str.strip, i_monkey.split('\n')):
            if 'Monkey' in line:
                pass
            elif 'items' in line:
                start = list(map(int, line.split(':')[1].split(',')))
            elif 'Operation' in line:
                operation = line.split('=')[1].strip()
            elif 'Test' in line:
                test = int(line.split()[-1])
            elif 'true' in line:
                t_true = int(line.split()[-1])
            elif 'false' in line:
                t_false = int(line.split()[-1])
            else:
                raise Exception('Unexpected monkey line.')
        monkeys.append(Monkey(start, operation, test, t_true, t_false))

    while slinging_round < 20:
        for monkey in monkeys:
            for _ in monkey.items.copy():
                target, item = monkey.inspect_1()
                monkeys[target].catch(item)
        slinging_round += 1

    inspection_counts = []
    for monkey in monkeys:
        inspection_counts.append(monkey.inspection_count)
    inspection_counts.sort()

    return inspection_counts[-1] * inspection_counts[-2]


def part_two(aoc_input) -> int:
    monkeys = []
    slinging_round = 0
    for i_monkey in map(str.strip, aoc_input.split('\n\n')):
        start = operation = test = t_true = t_false = None
        for line in map(str.strip, i_monkey.split('\n')):
            if 'Monkey' in line:
                pass
            elif 'items' in line:
                start = list(map(int, line.split(':')[1].split(',')))
            elif 'Operation' in line:
                operation = line.split('=')[1].strip()
            elif 'Test' in line:
                test = int(line.split()[-1])
            elif 'true' in line:
                t_true = int(line.split()[-1])
            elif 'false' in line:
                t_false = int(line.split()[-1])
            else:
                raise Exception('Unexpected monkey line.')
        monkeys.append(Monkey(start, operation, test, t_true, t_false))

    gcm = 1
    for monkey in monkeys:
        gcm *= monkey.test

    while slinging_round < 10000:
        for monkey in monkeys:
            for _ in monkey.items.copy():
                target, item = monkey.inspect_2()
                monkeys[target].catch(item, gcm)
        slinging_round += 1

    inspection_counts = []
    for monkey in monkeys:
        inspection_counts.append(monkey.inspection_count)
    inspection_counts.sort()

    return inspection_counts[-1] * inspection_counts[-2]


class Monkey:
    def __init__(self, start: list, operation: str, test: int, t_true: int, t_false: int):
        self.items = start
        self.operation = operation
        self.test = test
        self.target_true = t_true
        self.target_false = t_false
        self.inspection_count = 0

    def inspect_1(self) -> tuple[int, int]:
        """Monkey inspects, gets bored and throws item"""
        old = self.items.pop(0)  # old is part of the string in eval
        item = eval(self.operation) // 3
        self.inspection_count += 1
        if item % self.test == 0:
            return self.target_true, item
        else:
            return self.target_false, item

    def inspect_2(self) -> tuple[int, int]:
        """Monkey inspects, gets bored and throws item"""
        old = self.items.pop(0)  # old is part of the string in eval
        item = int(eval(self.operation))
        self.inspection_count += 1
        if item % self.test == 0:
            return self.target_true, item
        else:
            return self.target_false, item

    def catch(self, item, gcm=None):
        if gcm is None:
            self.items.append(item)
        else:
            self.items.append(item % gcm)


if __name__ == '__main__':
    main()
