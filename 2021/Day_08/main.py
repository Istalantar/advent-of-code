import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class Entry:
    def __init__(self, entry):
        self.pattern = []
        self.output = ''
        self.__parse_entry(entry)
        self.new_output = self.output
        self.__rearrange()

    def __parse_entry(self, entry):
        digits = entry.split('|')[0]
        for digit in digits.split():
            self.pattern.append(digit)

        self.output = entry.split('|')[1]

    def __rearrange(self):
        a = b = c = d = e = f = g = ''
        one = four = seven = ''
        len_five = []
        len_six = []
        letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        for digit in self.pattern:
            for letter in digit:
                letters[letter] += 1

            if len(digit) == 2:
                one = digit
            elif len(digit) == 4:
                four = digit
            elif len(digit) == 3:
                seven = digit
            elif len(digit) == 5:
                len_five.append(digit)
            elif len(digit) == 6:
                len_six.append(digit)

        # find e (letter with occurence = 4)
        for key, value in letters.items():
            if value == 4:
                e = key
            elif value == 6:
                b = key
            elif value == 9:
                f = key

        # find a (in seven but not in one)
        for letter in seven:
            if letter not in one:
                a = letter

        # find c (in one but not letter f)
        for letter in one:
            if letter not in f:
                c = letter

        # find g (ocurrence g = 7 and not in 4)
        for key, value in letters.items():
            if value == 7 and key not in four:
                g = key

        # find d (last letter)
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            if letter not in [a, b, c, e, f, g]:
                d = letter

        # replace letters
        self.new_output = self.new_output.replace(a, '1')
        self.new_output = self.new_output.replace(b, '2')
        self.new_output = self.new_output.replace(c, '3')
        self.new_output = self.new_output.replace(d, '4')
        self.new_output = self.new_output.replace(e, '5')
        self.new_output = self.new_output.replace(f, '6')
        self.new_output = self.new_output.replace(g, '7')

        self.new_output = self.new_output.replace('1', 'a')
        self.new_output = self.new_output.replace('2', 'b')
        self.new_output = self.new_output.replace('3', 'c')
        self.new_output = self.new_output.replace('4', 'd')
        self.new_output = self.new_output.replace('5', 'e')
        self.new_output = self.new_output.replace('6', 'f')
        self.new_output = self.new_output.replace('7', 'g')

    @staticmethod
    def __get_digit(digit) -> str:
        zero = 'abcefg'
        two = 'acdeg'
        three = 'acdfg'
        five = 'abdfg'
        six = 'abdefg'
        nine = 'abcdfg'

        if len(digit) == 2:
            return '1'
        elif len(digit) == 4:
            return '4'
        elif len(digit) == 3:
            return '7'
        elif len(digit) == 7:
            return '8'
        elif sorted(digit) == list(zero):
            return '0'
        elif sorted(digit) == list(two):
            return '2'
        elif sorted(digit) == list(three):
            return '3'
        elif sorted(digit) == list(five):
            return '5'
        elif sorted(digit) == list(six):
            return '6'
        elif sorted(digit) == list(nine):
            return '9'
        else:
            raise Exception("Something weird happened")

    def get_output(self) -> int:
        output = ''
        for digit in self.new_output.split():
            output += self.__get_digit(digit)

        return int(output)


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    one = 0
    four = 0
    seven = 0
    eight = 0

    for line in content:
        digits = line.split('|')[1]
        for digit in digits.split():
            one += 1 if len(digit) == 2 else 0
            four += 1 if len(digit) == 4 else 0
            seven += 1 if len(digit) == 3 else 0
            eight += 1 if len(digit) == 7 else 0

    return sum([one, four, seven, eight])


def part_two(content) -> int:
    entries = []

    for line in content:
        entries.append(Entry(line))

    return sum([entry.get_output() for entry in entries])


if __name__ == '__main__':
    main()
