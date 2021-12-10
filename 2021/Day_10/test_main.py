from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.content = my_input_list("example.txt")

    def test_part_one(self):
        self.assertEqual(26397, part_one(self.content))

    def test_part_two(self):
        self.assertEqual(288957, part_two(self.content))
