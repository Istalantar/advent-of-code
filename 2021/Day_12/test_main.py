from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestPartOne(TestCase):
    def setUp(self) -> None:
        self.content = my_input_list("example.txt")
        self.content_2 = my_input_list("example2.txt")
        self.content_3 = my_input_list("example3.txt")

    def test_part_one1(self):
        self.assertEqual(10, part_one(self.content))

    def test_part_one2(self):
        self.assertEqual(19, part_one(self.content_2))

    def test_part_one3(self):
        self.assertEqual(226, part_one(self.content_3))


class TestPartTwo(TestCase):
    def setUp(self) -> None:
        self.content = my_input_list("example.txt")
        self.content_2 = my_input_list("example2.txt")
        self.content_3 = my_input_list("example3.txt")

    def test_part_two(self):
        self.assertEqual(36, part_two(self.content))

    def test_part_two2(self):
        self.assertEqual(103, part_two(self.content_2))

    def test_part_two3(self):
        self.assertEqual(3509, part_two(self.content_3))
