import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class Alu:
    def __init__(self):
        self.alu = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def instruction(self, instr, a, b):
        if instr == 'inp':
            self.alu[a] = int(b)
        elif instr == 'add':
            self.__add(a, b)
        elif instr == 'mul':
            self.__mul(a, b)
        elif instr == 'div':
            self.__div(a, b)
        elif instr == 'mod':
            self.__mod(a, b)
        elif instr == 'eql':
            self.__eql(a, b)

    def __inp(self, a: str, b: int):
        self.alu[a] = b

    def __add(self, a: str, b: str):
        if b.isalpha():
            self.alu[a] += self.alu[b]
        else:
            self.alu[a] += int(b)

    def __mul(self, a: str, b: str):
        if b.isalpha():
            self.alu[a] *= self.alu[b]
        else:
            self.alu[a] *= int(b)

    def __div(self, a: str, b: str):
        if b.isalpha() and self.alu[b] != 0:
            self.alu[a] = int(self.alu[a] / self.alu[b])
        elif int(b) != 0:
            self.alu[a] = int(self.alu[a] / int(b))

    def __mod(self, a: str, b: str):
        if b.isalpha() and self.alu[b] != 0:
            self.alu[a] %= self.alu[b]
        elif int(b) != 0:
            self.alu[a] %= int(b)

    def __eql(self, a: str, b: str):
        if b.isalpha():
            self.alu[a] = 1 if self.alu[a] == self.alu[b] else 0
        else:
            self.alu[a] = 1 if self.alu[a] == int(b) else 0


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content):
    mod_nums = ['992989999']
    my_alu = Alu()
    res = 0
    for num in mod_nums:
        mod_num = list(num)
        for line in content:
            temp = line.strip().split()
            if len(temp) == 2:
                instr, a = temp
                if not mod_num:  # break for if mod_num is empty
                    break
                b = mod_num.pop(0)
            else:
                instr, a, b = temp

            my_alu.instruction(instr, a, b)
            print(f"{instr} {a} {b} -> w: {my_alu.alu['w']}, x: {my_alu.alu['x']},"
                  f" y: {my_alu.alu['y']}, z: {my_alu.alu['z']}")

    # ToDo: figure out the misterious restrictions
    # only in following seven steps the value of z can decrease
    # for that to happen the previous value of z needs to be a specific value
    # 1 <= z%26 - subtractor >= 9
    subtractors = {4: -6, 6: -12, 10: -2, 11: -5, 12: -4, 13: -4, 14: -12}


def part_two(content) -> int:
    return 0


if __name__ == '__main__':
    main()
