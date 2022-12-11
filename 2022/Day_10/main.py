import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    part_two(aoc_input.copy())


def part_one(aoc_input) -> int:
    handheld = CPU()
    signal_strength = []
    for instruction in aoc_input:
        handheld.instruction = instruction
        cycles = 2 if 'addx' in instruction else 1
        for i in range(cycles):
            handheld.run_cycle()
            if handheld.cycle == 20 or (handheld.cycle - 20) % 40 == 0:
                signal_strength.append(handheld.get_signal_strength())
            if i == 1:  # end of second cycle
                handheld.finish_calc()
    return sum(signal_strength)


def part_two(aoc_input):
    handheld = CPU()
    for instruction in aoc_input:
        handheld.instruction = instruction
        cycles = 2 if 'addx' in instruction else 1
        for i in range(cycles):
            handheld.run_cycle()
            if i == 1:  # end of second cycle
                handheld.finish_calc()
    for line in handheld.screen:
        print(''.join(line))


class CPU:
    def __init__(self):
        self.register = 1
        self.cycle = 0
        self.temp_register = 0
        self.instruction = ''
        self.is_adding = False
        self.screen = [['.' for _ in range(40)] for _ in range(6)]
        self.pixel = 0

    def get_signal_strength(self) -> int:
        return self.cycle * self.register

    def run_cycle(self):
        self.cycle += 1
        if 'addx' in self.instruction:
            _, val = self.instruction.split(' ')
            self.temp_register = int(val)
            self.is_adding = True
        elif 'noop' in self.instruction:
            pass
        self.draw_pixel()

    def finish_calc(self):
        if self.is_adding:
            self.register += self.temp_register
            self.temp_register = 0
            self.is_adding = False

    def draw_pixel(self):
        line = self.cycle // 40
        sprite = [self.register - 1, self.register, self.register + 1]
        if self.pixel in sprite:
            self.screen[line][self.pixel] = '#'
        if self.pixel < 39:
            self.pixel += 1
        else:
            self.pixel = 0


if __name__ == '__main__':
    main()
