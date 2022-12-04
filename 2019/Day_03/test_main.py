from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestExample(TestCase):
    def setUp(self) -> None:
        self.ex_1 = ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
                     'U62,R66,U55,R34,D71,R55,D58,R83']
        self.ex_2 = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                     'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']

    def test_part_one(self):
        self.assertEqual(159, part_one(self.ex_1))

    def test_part_one_2(self):
        self.assertEqual(135, part_one(self.ex_2))

    def test_part_two_1(self):
        self.assertEqual(610, part_two(self.ex_1))

    def test_part_two_2(self):
        self.assertEqual(410, part_two(self.ex_2))
