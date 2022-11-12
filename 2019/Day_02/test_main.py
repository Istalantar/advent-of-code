from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.aoc_input = list(map(int, my_input_string("example.txt").split(',')))

    def test_part_one(self):
        self.assertEqual(30, part_one(self.aoc_input.copy()))

    def test_part_two(self):
        self.assertEqual(-1, part_two(self.aoc_input.copy()))
