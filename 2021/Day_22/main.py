import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    cube = {}
    for step in content:
        state = step.split()[0]
        x, y, z = step.split(',')
        x_min, x_max = map(int, x.split('=')[1].split('..'))
        y_min, y_max = map(int, y.split('=')[1].split('..'))
        z_min, z_max = map(int, z.split('=')[1].split('..'))

        for z in range(max(z_min, -50), min(z_max, 50) + 1):
            for y in range(max(y_min, -50), min(y_max, 50) + 1):
                for x in range(max(x_min, -50), min(x_max, 50) + 1):
                    cube[(x, y, z)] = state

    return sum([True if c == 'on' else False for c in cube.values()])


def part_two(content) -> int:
    return 0


if __name__ == '__main__':
    main()
