from myFunctions import my_input_list


def main():
    content = my_input_list("input.txt")

    part_one(content)
    part_two(content)


def part_one(content):
    pos_x = 0
    pos_y = 0  # number increases with depth

    for command in content:
        direction = command.split()

        if direction[0] == 'forward':
            pos_x += int(direction[1])
        elif direction[0] == 'down':
            pos_y += int(direction[1])
        elif direction[0] == 'up':
            pos_y -= int(direction[1])
        else:
            print(f'Unexpected command: {direction[0]}')

    print(pos_x * pos_y)


def part_two(content):
    aim = 0
    pos_x = 0
    pos_y = 0  # number increases with depth

    for command in content:
        direction = command.split()

        if direction[0] == 'forward':
            pos_x += int(direction[1])
            pos_y += aim * int(direction[1])
        elif direction[0] == 'down':
            aim += int(direction[1])
        elif direction[0] == 'up':
            aim -= int(direction[1])
        else:
            print(f'Unexpected command: {direction[0]}')

    print(pos_x * pos_y)


if __name__ == '__main__':
    main()
