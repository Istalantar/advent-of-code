from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.content = my_input_list("example.txt")

    def test_part_one(self):
        self.assertEqual(part_one(self.content), -1)

    def test_part_two(self):
        self.assertEqual(part_two(self.content), -1)
