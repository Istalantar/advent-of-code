from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def test_part_one(self):
        self.assertEqual(739785, part_one(4, 8))

    def test_part_two(self):
        self.assertEqual(-1, part_two())
