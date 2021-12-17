import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    content = my_input_string("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    x_range, y_range = content.split(':')[1].split(',')
    x_range = x_range.split('=')[1]
    y_range = y_range.split('=')[1]
    xmin, xmax = x_range.strip().split('..')
    ymin, ymax = y_range.strip().split('..')
    xmin = int(xmin)
    xmax = int(xmax)
    ymin = int(ymin)
    ymax = int(ymax)

    probe_x = 0
    probe_y = 0
    max_height = 0

    for i in range(200, 0, -1):
        for j in range(0, 300):
            vel_y = i
            vel_x = j
            current_max_height = 0

            while probe_x <= xmax and probe_y >= ymin:
                probe_x, probe_y, vel_x, vel_y = go_step(probe_x, probe_y, vel_x, vel_y)
                if probe_y > current_max_height:
                    current_max_height = probe_y
                if is_in_range(probe_x, probe_y, xmin, xmax, ymin, ymax):
                    max_height = current_max_height if current_max_height > max_height else max_height
            probe_x = 0
            probe_y = 0
    return max_height


def part_two(content) -> int:
    x_range, y_range = content.split(':')[1].split(',')
    x_range = x_range.split('=')[1]
    y_range = y_range.split('=')[1]
    xmin, xmax = x_range.strip().split('..')
    ymin, ymax = y_range.strip().split('..')
    xmin = int(xmin)
    xmax = int(xmax)
    ymin = int(ymin)
    ymax = int(ymax)

    probe_x = 0
    probe_y = 0
    hit_list = set()

    for i in range(500, -120, -1):
        for j in range(0, 300):
            vel_y = i
            vel_x = j

            while probe_x <= xmax and probe_y >= ymin:
                probe_x, probe_y, vel_x, vel_y = go_step(probe_x, probe_y, vel_x, vel_y)
                if is_in_range(probe_x, probe_y, xmin, xmax, ymin, ymax):
                    hit_list.add((j, i))
            probe_x = 0
            probe_y = 0
    return len(hit_list)


def go_step(x, y, vel_x, vel_y):
    x += vel_x
    y += vel_y

    # reduce velocity due to drag / gravity
    if vel_x > 0:
        vel_x -= 1
    elif vel_x < 0:
        vel_x += 1

    vel_y -= 1
    return x, y, vel_x, vel_y


def is_in_range(x, y, xmin, xmax, ymin, ymax) -> bool:
    return xmin <= x <= xmax and ymin <= y <= ymax


if __name__ == '__main__':
    main()
