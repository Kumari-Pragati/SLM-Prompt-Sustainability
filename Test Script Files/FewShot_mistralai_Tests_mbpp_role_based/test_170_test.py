import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 5), 15)

    def test_sum_empty_list(self):
        self.assertEqual(sum_range_list([], 1, 5), 0)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum_range_list([-1, -2, -3, -4, -5], 1, 5), -15)

    def test_sum_out_of_range_list(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 6, 10), 0)

    def test_sum_range_beyond_list(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 7), 16)

    def test_sum_range_with_duplicates(self):
        self.assertEqual(sum_range_list([1, 1, 1, 2, 3, 4, 5], 1, 6), 16)
