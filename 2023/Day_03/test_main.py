from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.aoc_input = my_input_list("example.txt")
        self.aoc_input_2 = my_input_list("my_example.txt")

    def test_part_one(self):
        self.assertEqual(4361, part_one(self.aoc_input))

    def test_part_one_2(self):
        self.assertEqual(3747, part_one(self.aoc_input_2))

    def test_part_two(self):
        self.assertEqual(467835, part_two(self.aoc_input))
