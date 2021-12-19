from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestPartOne(TestCase):
    def setUp(self) -> None:
        self.content = my_input_list("example.txt")

    def test_part_one1(self):
        self.assertEqual(16, part_one(self.content[0]))

    def test_part_one2(self):
        self.assertEqual(12, part_one(self.content[1]))

    def test_part_one3(self):
        self.assertEqual(23, part_one(self.content[2]))

    def test_part_one4(self):
        self.assertEqual(31, part_one(self.content[3]))


class TestPartTwo(TestCase):
    def setUp(self) -> None:
        self.content = my_input_list("example.txt")

    def test_part_two(self):
        self.assertEqual(-1, part_two(self.content))
