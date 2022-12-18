from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.aoc_input = my_input_string("example.txt")

    def test_part_one(self):
        self.assertEqual(3068, part_one(self.aoc_input))

    def test_part_two(self):
        self.assertEqual(1514285714288, part_two(self.aoc_input))
