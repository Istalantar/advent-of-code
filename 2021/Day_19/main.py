import sys
import itertools
from numpy import array

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


class Scanner:
    count = itertools.count()

    def __init__(self):
        self.id = next(self.count)
        # absolute scanner position from origin (x, y, z) = (0, 0, 0)
        # first scanner (id: 0) is at origin
        self.position = array([0, 0, 0]) if self.id == 0 else None
        self.beacons = []  # list of all beacon coordinates relative to this scanner
        self.scanners = []  # list of all scanners relative to this scanner

    def __repr__(self):
        return f'Scanner {self.id}'


class Beacon:
    def __init__(self, x, y, z):
        self.position = array([x, y, z])  # beacon position relative to corresponding scanner

    def __repr__(self):
        return f'({self.position[0]}, {self.position[1]}, {self.position[2]})'


def main():
    content = my_input_string("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    content = content.strip().split('\n\n')
    scanners = []
    for scan in content:
        scanner = Scanner()
        scanners.append(scanner)
        for beacon in scan.split('\n')[1:]:
            scanner.beacons.append(Beacon(*beacon.split(',')))

    # ToDo: find all unique beacons

    return len(scanners[0].beacons)


def part_two(content) -> int:
    return 0


if __name__ == '__main__':
    main()
