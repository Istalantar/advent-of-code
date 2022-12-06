from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.aoc_input = my_input_list("example.txt")
        self.ex_1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.ex_2 = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.ex_3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.ex_4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

    def test_part_one_1(self):
        self.assertEqual(5, part_one(self.ex_1))

    def test_part_one_2(self):
        self.assertEqual(6, part_one(self.ex_2))

    def test_part_one_3(self):
        self.assertEqual(10, part_one(self.ex_3))

    def test_part_one_4(self):
        self.assertEqual(11, part_one(self.ex_4))

    def test_part_two_1(self):
        self.assertEqual(23, part_two(self.ex_1))

    def test_part_two_2(self):
        self.assertEqual(23, part_two(self.ex_2))

    def test_part_two_3(self):
        self.assertEqual(29, part_two(self.ex_3))

    def test_part_two_4(self):
        self.assertEqual(26, part_two(self.ex_4))
