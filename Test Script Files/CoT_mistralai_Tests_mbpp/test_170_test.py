import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_range_list([], 1, 1), 0)

    def test_single_element(self):
        self.assertEqual(sum_range_list([1], 1, 1), 1)
        self.assertEqual(sum_range_list([1], 1, 2), 1)

    def test_multiple_elements(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 5), 15)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 3, 5), 12)

    def test_out_of_range_index(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 6, 6), 0)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], -1, 0), 0)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, -1), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_range_list([-1, -2, -3, -4, -5], 1, 5), -15)
        self.assertEqual(sum_range_list([-1, -2, -3, -4, -5], 4, 5), -9)

    def test_zero(self):
        self.assertEqual(sum_range_list([0], 1, 1), 0)
        self.assertEqual(sum_range_list([0], 1, 2), 0)
