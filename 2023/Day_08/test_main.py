from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.aoc_input = my_input_list("example.txt")
        self.aoc_input_2 = my_input_list("example_2.txt")
        self.aoc_input_3 = my_input_list("example_3.txt")

    def test_part_one(self):
        self.assertEqual(2, part_one(self.aoc_input))

    def test_part_one_2(self):
        self.assertEqual(6, part_one(self.aoc_input_2))

    def test_part_two(self):
        self.assertEqual(6, part_two(self.aoc_input_3))
