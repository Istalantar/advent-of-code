from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.content = my_input_string("example.txt")

    def test_part_one(self):
        self.assertEqual(45, part_one(self.content))

    def test_part_two(self):
        self.assertEqual(112, part_two(self.content))
