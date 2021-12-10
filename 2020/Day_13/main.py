import sys
from math import ceil

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    earliest_time = int(content[0])
    in_service = {}

    for bus in content[1].split(','):
        if bus.isnumeric():
            # saves next departure after 'earliest_time' for bus number
            in_service[int(bus)] = ceil(earliest_time / int(bus)) * int(bus)

    next_departure = min([departure for bus, departure in in_service.items()], key=lambda x: abs(x - earliest_time))
    return (next_departure - earliest_time) * list(in_service.keys())[list(in_service.values()).index(next_departure)]


def part_two(content) -> int:
    return 0


if __name__ == '__main__':
    main()
