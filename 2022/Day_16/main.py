import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    valves = []
    for valve in aoc_input:
        assert isinstance(valve, str)
        name = valve.split()[1].strip()
        rate = int(valve.split()[4].split('=')[1][:-1])
        linked_valves = valve.split('valves')[-1].strip()
        valves.append(Valve(name, rate, linked_valves))
    valves.sort(reverse=True)
    # Todo: breadth first search?
    return -1


def part_two(aoc_input) -> int:
    return -1


class Valve:
    def __init__(self, name: str, rate: int, linked_valves: str):
        self.name = name
        self.rate = rate
        self.linked_valves = list(map(str.strip, linked_valves.split(',')))
        self.is_closed = True

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.rate < other.rate


if __name__ == '__main__':
    main()
