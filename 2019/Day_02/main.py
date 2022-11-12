import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = list(map(int, my_input_string("input.txt").split(',')))

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    aoc_input[1] = 12
    aoc_input[2] = 2

    for i, value in enumerate(aoc_input):
        if i % 4 == 0:  # every fourth number is opcode
            if value == 1:
                aoc_input[aoc_input[i+3]] = aoc_input[aoc_input[i+1]] + aoc_input[aoc_input[i+2]]
            elif value == 2:
                aoc_input[aoc_input[i+3]] = aoc_input[aoc_input[i+1]] * aoc_input[aoc_input[i+2]]
            elif value == 99:
                break
            else:
                raise 'Invalid Opcode'

    return aoc_input[0]


def part_two(aoc_input) -> int:
    aoc_input_temp = aoc_input.copy()
    out = 19690720

    for n in range(100):
        for v in range(100):
            aoc_input_temp[1] = n
            aoc_input_temp[2] = v

            for i, value in enumerate(aoc_input_temp):
                if i % 4 == 0:  # every fourth number is opcode
                    if value == 1:
                        aoc_input_temp[aoc_input_temp[i+3]] = aoc_input_temp[aoc_input_temp[i+1]]\
                                                              + aoc_input_temp[aoc_input_temp[i+2]]
                    elif value == 2:
                        aoc_input_temp[aoc_input_temp[i+3]] = aoc_input_temp[aoc_input_temp[i+1]]\
                                                              * aoc_input_temp[aoc_input_temp[i+2]]
                    elif value == 99:
                        if aoc_input_temp[0] == out:
                            return 100 * n + v
                        else:
                            aoc_input_temp = aoc_input.copy()
                            break
                    else:
                        raise Exception('Invalid Opcode')

    return -1


if __name__ == '__main__':
    main()
