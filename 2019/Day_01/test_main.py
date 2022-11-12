from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        # self.content = my_input_list("example.txt")
        pass

    def test_part_one(self):
        self.assertEqual(654, part_one([1969]))

    def test_part_one_2(self):
        self.assertEqual(33583, part_one([100756]))

    def test_part_two(self):
        self.assertEqual(966, part_two([1969]))

    def test_part_two_2(self):
        self.assertEqual(50346, part_two([100756]))
