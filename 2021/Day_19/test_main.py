from unittest import TestCase
from main import part_one, part_two, Scanner, Beacon
import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.content = my_input_string("example.txt")

    def test_part_one(self):
        content = self.content.strip().split('\n\n')
        scanners = []
        for scan in content:
            scanner = Scanner()
            scanners.append(scanner)
            for beacon in scan.split('\n')[1:]:
                scanner.beacons.append(Beacon(*beacon.split(',')))
            self.assertEqual(79, part_one(self.content))

    def test_part_two(self):
        self.assertEqual(-1, part_two(self.content))
