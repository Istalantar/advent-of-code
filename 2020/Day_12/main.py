import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    res = 0
    ship_direction = 90
    north = 0
    east = 0
    south = 0
    west = 0

    for instr in content:
        action = instr[:1]
        value = int(instr[1:])

        if action == "N" or (action == "F" and ship_direction in (0, 360)):
            north += value
            south -= value
        elif action == "E" or (action == "F" and ship_direction == 90):
            east += value
            west -= value
        elif action == "S" or (action == "F" and ship_direction == 180):
            south += value
            north -= value
        elif action == "W" or (action == "F" and ship_direction == 270):
            west += value
            east -= value
        elif action == "R":
            ship_direction += value
            ship_direction -= 360 if ship_direction >= 360 else 0
        elif action == "L":
            ship_direction -= value
            ship_direction += 360 if ship_direction <= 0 else 0
        else:
            print("unexpected instruction")

    res += north if north > 0 else 0
    res += east if east > 0 else 0
    res += south if south > 0 else 0
    res += west if west > 0 else 0

    return res


def part_two(content) -> int:
    res = 0
    return res


if __name__ == '__main__':
    main()
