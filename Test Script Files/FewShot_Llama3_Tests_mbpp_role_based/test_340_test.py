import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)

    def test_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, -4, -5]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, -2, 3, -4, 5]), 6)

    def test_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_single_positive_number(self):
        self.assertEqual(sum_three_smallest_nums([1]), 1)

    def test_single_negative_number(self):
        self.assertEqual(sum_three_smallest_nums([-1]), 0)

    def test_single_zero(self):
        self.assertEqual(sum_three_smallest_nums([0]), 0)
