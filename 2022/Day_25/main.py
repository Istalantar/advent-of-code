import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402

SNAFU_DIGITS = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> str:
    dec = []
    for snafu in aoc_input:
        dec.append(snafu_to_dec(snafu))

    return dec_to_snafu(sum(dec))


def part_two(aoc_input) -> int:
    return -1


def dec_to_snafu(i: int) -> str:
    res = []
    while i:
        rest = i % 5
        res.append(str(rest).replace('4', '-').replace('3', '='))
        if rest in [0, 1, 2]:
            i //= 5
        else:
            i = i // 5 + 1

    return ''.join(reversed(res))


def snafu_to_dec(val: str) -> int:
    ret = 0
    for index, value in enumerate(val):
        ret += SNAFU_DIGITS[value] * 5 ** (len(val) - index - 1)
    return ret


if __name__ == '__main__':
    main()
