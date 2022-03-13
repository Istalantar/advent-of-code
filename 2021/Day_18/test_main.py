from unittest import TestCase
from main import SnailNum
import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class TestSum(TestCase):
    def setUp(self) -> None:
        self.content = my_input_list('sum_example.txt')

    def test_sum1(self):
        a = SnailNum('[1,1]')
        b = SnailNum('[2,2]')
        c = SnailNum('[3,3]')
        d = SnailNum('[4,4]')
        my_sum = a + b + c + d

        final_sum = '[[[[1, 1], [2, 2]], [3, 3]], [4, 4]]'
        self.assertEqual(final_sum, my_sum.name())

    def test_sum2(self):
        a = SnailNum('[[[[1, 1], [2, 2]], [3, 3]], [4, 4]]')
        b = SnailNum('[5,5]')
        my_sum = a + b

        final_sum = '[[[[3, 0], [5, 3]], [4, 4]], [5, 5]]'
        self.assertEqual(final_sum, my_sum.name())

    def test_sum3(self):
        a = SnailNum('[1,1]')
        b = SnailNum('[2,2]')
        c = SnailNum('[3,3]')
        d = SnailNum('[4,4]')
        e = SnailNum('[5,5]')
        f = SnailNum('[6,6]')
        my_sum = a + b + c + d + e + f

        final_sum = '[[[[5, 0], [7, 4]], [5, 5]], [6, 6]]'
        self.assertEqual(final_sum, my_sum.name())

    def test_sum4_1(self):
        a = SnailNum('[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]]')
        b = SnailNum('[7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]')
        my_sum = a + b

        final_sum = '[[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]'
        self.assertEqual(final_sum, my_sum.name())

    def test_sum4_all(self):
        nums = []
        for num in self.content:
            nums.append(SnailNum(num))

        my_sum = nums[0]
        for num in nums[1:]:
            my_sum += num
            print(my_sum)

        final_sum = '[[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]'
        self.assertEqual(final_sum, my_sum.name())


class TestExplosion(TestCase):
    def test_explosion1(self):
        num_in = SnailNum('[[[[[9, 8], 1], 2], 3], 4]')
        num_out = '[[[[0, 9], 2], 3], 4]'
        self.assertEqual(num_out, num_in.name())

    def test_explosion1_1(self):
        num_in = SnailNum('[[[[[1, 1], [2, 2]], [3, 3]], [4, 4]], [5, 5]]')
        num_out = '[[[[3, 0], [5, 3]], [4, 4]], [5, 5]]'
        self.assertEqual(num_out, num_in.name())

    def test_explosion2(self):
        num_in = SnailNum('[7, [6, [5, [4, [3, 2]]]]]')
        num_out = '[7, [6, [5, [7, 0]]]]'
        self.assertEqual(num_out, num_in.name())

    def test_explosion3(self):
        num_in = SnailNum('[[6, [5, [[4, 3], [3, 2]]]], [1, 1]]')
        num_out = '[[6, [9, [6, 0]]], [3, 1]]'
        self.assertEqual(num_out, num_in.name())

    def test_explosion4(self):
        num_in = SnailNum('[[6, [5, [4, [3, 2]]]], [1, 1]]')
        num_out = '[[6, [5, [7, 0]]], [3, 1]]'
        self.assertEqual(num_out, num_in.name())

    def test_explosion5(self):
        num_in = SnailNum('[[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]')
        num_out = '[[3, [2, [8, 0]]], [9, [5, [7, 0]]]]'
        self.assertEqual(num_out, num_in.name())


class TestSplit(TestCase):
    def test_split1(self):
        num_in = SnailNum('[10, 1]')
        num_out = '[[5, 5], 1]'
        self.assertEqual(num_out, num_in.name())

    def test_split2(self):
        num_in = SnailNum('[11, 1]')
        num_out = '[[5, 6], 1]'
        self.assertEqual(num_out, num_in.name())

    def test_split3(self):
        num_in = SnailNum('[12, 1]')
        num_out = '[[6, 6], 1]'
        self.assertEqual(num_out, num_in.name())


class TestMagnitude(TestCase):
    def test_magnitude1(self):
        num = SnailNum('[[1,2],[[3,4],5]]')
        self.assertEqual(143, num.magnitude())

    def test_magnitude2(self):
        num = SnailNum('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
        self.assertEqual(1384, num.magnitude())

    def test_magnitude3(self):
        num = SnailNum('[[[[1,1],[2,2]],[3,3]],[4,4]]')
        self.assertEqual(445, num.magnitude())

    def test_magnitude4(self):
        num = SnailNum('[[[[3,0],[5,3]],[4,4]],[5,5]]')
        self.assertEqual(791, num.magnitude())

    def test_magnitude5(self):
        num = SnailNum('[[[[5,0],[7,4]],[5,5]],[6,6]]')
        self.assertEqual(1137, num.magnitude())

    def test_magnitude6(self):
        num = SnailNum('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
        self.assertEqual(3488, num.magnitude())

    def test_magnitude7(self):
        num = SnailNum('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
        self.assertEqual(4140, num.magnitude())
