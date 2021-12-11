import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def apply_mask(my_set):
    if my_set[0] == '1':
        return '1'
    elif my_set[0] == '0':
        return '0'
    else:
        return my_set[1]


def part_one(content) -> int:
    mask = ''
    memory = {}

    for line in content:
        if 'mask' in line:
            mask = line.split('=')[1].strip()
        elif 'mem' in line:
            mem_index = int(line[line.find('[') + 1:line.find(']')])
            mem_val = format(int(line.split('=')[1].strip()), '036b')  # value as 36-bit binary
            mem_val = ''.join(list(map(apply_mask, list(zip(mask, mem_val)))))
            memory[mem_index] = int(mem_val, 2)
    return sum(memory.values())


def part_two(content) -> int:

    return 0


if __name__ == '__main__':
    main()
