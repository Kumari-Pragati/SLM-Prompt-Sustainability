import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_range_list([], 1, 1), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_range_list([1], 1, 1), 1)
        self.assertEqual(sum_range_list([1], 1, 2), 1)

    def test_negative_numbers(self):
        self.assertEqual(sum_range_list([-1, -2, -3], 1, 3), -6)

    def test_positive_numbers(self):
        self.assertEqual(sum_range_list([1, 2, 3], 1, 3), 6)

    def test_out_of_range_index(self):
        self.assertEqual(sum_range_list([1, 2, 3], 4, 3), 0)
        self.assertEqual(sum_range_list([1, 2, 3], 1, 4), 6)

    def test_large_range(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 9), 45)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 19), 171)
