from unittest import TestCase
from main import part_one, part_two
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestPartOne(TestCase):
    def setUp(self) -> None:
        self.content1 = my_input_list("sum_example1.txt")
        self.content2 = my_input_list("sum_example2.txt")
        self.content3 = my_input_list("sum_example3.txt")
        self.content4 = my_input_list("sum_example4.txt")
        self.content5 = my_input_list("magnitude_example.txt")

    def sum1(self):
        # ToDo: do addition
        final_sum = [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]
        self.assertEqual(final_sum, part_one(self.content1))

    def sum2(self):
        final_sum = [[[[3, 0], [5, 3]], [4, 4]], [5, 5]]
        self.assertEqual(final_sum, part_one(self.content2))

    def sum3(self):
        final_sum = [[[[5, 0], [7, 4]], [5, 5]], [6, 6]]
        self.assertEqual(final_sum, part_one(self.content3))

    def sum4(self):
        final_sum = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
        self.assertEqual(final_sum, part_one(self.content4))

    def magnitude1(self):
        self.assertEqual(-1, part_one(self.content5[0]))

    def magnitude2(self):
        self.assertEqual(-1, part_one(self.content5[1]))

    def magnitude3(self):
        self.assertEqual(-1, part_one(self.content5[2]))

    def magnitude4(self):
        self.assertEqual(-1, part_one(self.content5[3]))

    def magnitude5(self):
        self.assertEqual(-1, part_one(self.content5[4]))
