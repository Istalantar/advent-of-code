from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.content = my_input_list("example.txt")
        self.content2 = my_input_list("example_discord.txt")

    def test_part_one(self):
        self.assertEqual(40, part_one(self.content))

    def test_part_one2(self):
        self.assertEqual(29, part_one(self.content2))

    def test_part_two(self):
        self.assertEqual(315, part_two(self.content))
