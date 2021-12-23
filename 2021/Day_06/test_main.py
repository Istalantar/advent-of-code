from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.content = my_input_string("example.txt")

    def test_part_one(self):
        self.assertEqual(5934, part_one(self.content, 80))

    def test_part_two(self):
        self.assertEqual(26984457539, part_two(self.content, 256))
