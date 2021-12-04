from myFunctions import my_input


def main():
    content = my_input("input.txt")

    part_one(content)
    part_two(content)


def part_one(content):
    increases = 0
    for i in range(len(content)):
        try:
            if int(content[i + 1]) > int(content[i]):
                increases += 1
        except IndexError:
            break

    print(increases)


def part_two(content):
    increases = 0

    for i in range(len(content)):
        try:
            first_window = int(content[i]) + int(content[i+1]) + int(content[i+2])
            second_window = int(content[i+1]) + int(content[i+2]) + int(content[i+3])
        except IndexError:
            break

        if second_window > first_window:
            increases += 1

    print(increases)


if __name__ == '__main__':
    main()
