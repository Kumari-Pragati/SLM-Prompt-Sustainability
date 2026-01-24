import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, -1, 4, -2, 5]), 6)
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3]), 0)
        self.assertEqual(sum_three_smallest_nums([0, 1, 2]), 3)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3]), 6)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4]), 7)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 9)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, 6]), 11)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, 6, 7]), 13)

    def test_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_three_smallest_nums([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, 0]), -3)
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, 0, 1]), 0)
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, 0, 1, 2]), 1)
