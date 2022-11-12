import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    fuel = []
    for module in content:
        fuel.append(int(int(module) / 3) - 2)
    return sum(fuel)


def part_two(content) -> int:
    fuel_list = []
    for module in content:
        fuel = int(int(module) / 3) - 2
        fuel_list.append(fuel)

    for fuel in fuel_list.copy():
        temp = fuel
        while temp >= 0:
            temp = int(int(temp) / 3) - 2
            if temp > 0:
                fuel_list.append(temp)

    return sum(fuel_list)


if __name__ == '__main__':
    main()
