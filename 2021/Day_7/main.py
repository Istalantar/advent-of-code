import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    content = my_input_string("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    fuel_cost = 0
    ships = [int(i) for i in content.split(',')]
    ships.sort()
    my_median = ships[int(len(ships) / 2)]
    for fuel in ships:
        fuel_diff = abs(fuel - my_median)
        fuel_cost += fuel_diff

    return fuel_cost


def part_two(content) -> int:
    fuel_cost = [0, 0, 0]
    ships = [int(i) for i in content.split(',')]
    ships.sort()
    my_mean = sum(ships) / len(ships)
    for fuel in ships:
        fuel_diff = [0, 0, 0]
        fuel_diff[0] = abs(fuel - round(my_mean - 1))
        fuel_diff[1] = abs(fuel - round(my_mean))
        fuel_diff[2] = abs(fuel - round(my_mean + 1))
        for i in range(1, fuel_diff[0] + 1):
            fuel_cost[0] += i
        for i in range(1, fuel_diff[1] + 1):
            fuel_cost[1] += i
        for i in range(1, fuel_diff[2] + 1):
            fuel_cost[2] += i

    fuel_cost.sort()
    return fuel_cost[0]


if __name__ == '__main__':
    main()
