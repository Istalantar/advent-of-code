from dataclasses import dataclass
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    sensors = []
    min_x = min_y = float('inf')
    max_x = max_y = 0
    for sensor in aoc_input:
        assert isinstance(sensor, str)
        s_coords = list(map(str.strip, sensor[sensor.index('x'):sensor.index(':')].split(',')))
        s_coords = tuple(map(lambda l: int(l.split('=')[1]), s_coords))
        b_coords = list(map(str.strip, sensor.split('at')[-1].split(',')))
        b_coords = tuple(map(lambda l: int(l.split('=')[1]), b_coords))
        min_x = min(s_coords[0], b_coords[0], min_x)
        max_x = max(s_coords[0], b_coords[0], max_x)
        min_y = min(s_coords[1], b_coords[1], min_y)
        max_y = max(s_coords[1], b_coords[1], max_y)
        sensors.append(Sensor(s_coords, b_coords))
    
    no_beacon = set()
    # ToDo: Fix runtime issue
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            for sensor in sensors:
                if sensor.is_no_beacon_area(x, y):
                    no_beacon.add((x, y))
    return sum([True if y == 10 else False for _, y in no_beacon])


def part_two(aoc_input) -> int:
    return -1


class Sensor:
    def __init__(self, s_coords, b_coords):
        self.x, self.y = s_coords
        self.coords = s_coords
        self.beacon = Beacon(*b_coords)
        self.beacon_distance = abs(self.x - self.beacon.x) + abs(self.y - self.beacon.y)

    def __repr__(self):
        return f'Sensor: ({self.x}, {self.y}), Beacon: ({self.beacon.x}, {self.beacon.y})'

    def is_no_beacon_area(self, x, y) -> bool:
        dx = abs(self.x - x)
        dy = abs(self.y - y)

        if (x, y) == (self.beacon.x, self.beacon.y):
            return False

        if dx + dy > self.beacon_distance:
            return False

        return True


@dataclass
class Beacon:
    x: int
    y: int

    def coords(self):
        return self.x, self.y


if __name__ == '__main__':
    main()
