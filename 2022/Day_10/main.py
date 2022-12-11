import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    handheld = CPU()
    signal_strength = []
    for instruction in aoc_input:
        signal_strength.append(handheld.execute_instruction(instruction))
    return sum(signal_strength)


def part_two(aoc_input) -> int:
    return -1


class CPU:
    def __init__(self):
        self.register = 1
        self.cycle = 0
        self.temp_register = 0
        self.is_adding = False

    def execute_instruction(self, instruction: str) -> int:
        ret = 0
        self.register += self.temp_register
        if 'addx' in instruction:
            _, val = instruction.split(' ')
            self.temp_register = int(val)
            for _ in range(2):
                self.cycle += 1
                if self.cycle == 20 or (self.cycle - 20) % 40 == 0:
                    ret = self.get_signal_strength()
        elif 'noop' in instruction:
            self.temp_register = 0
            self.cycle += 1
            if self.cycle == 20 or (self.cycle - 20) % 40 == 0:
                ret = self.get_signal_strength()
        return ret

    def get_signal_strength(self) -> int:
        return self.cycle * self.register

    def run_cycle(self):
        if self.is_adding:
            pass


if __name__ == '__main__':
    main()
