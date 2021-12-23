from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


class TestPartOne(TestCase):
    def setUp(self) -> None:
        self.content = my_input_string("example.txt")
        self.content2 = my_input_string("example2.txt")

    def test_part_one(self):
        self.assertEqual(35, part_one(self.content))

    def test_part_one2(self):
        self.assertEqual(24, part_one(self.content2))


class TestPartTwo(TestCase):
    def setUp(self) -> None:
        self.content = my_input_string("example.txt")

    def test_part_two(self):
        self.assertEqual(3351, part_two(self.content))
