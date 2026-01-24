import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_sum_range_list_positive(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)
        self.assertEqual(sum_range_list([10, 20, 30, 40, 50], 2, 4), 110)
        self.assertEqual(sum_range_list([-10, -5, 0, 5, 10], 2, 4), 25)

    def test_sum_range_list_empty_list(self):
        self.assertEqual(sum_range_list([], 1, 1), 0)

    def test_sum_range_list_single_element(self):
        self.assertEqual(sum_range_list([1], 1, 1), 1)

    def test_sum_range_list_single_element_end(self):
        self.assertEqual(sum_range_list([1], 0, 0), 0)

    def test_sum_range_list_out_of_range(self):
        self.assertEqual(sum_range_list([1, 2, 3], 4, 5), 0)
        self.assertEqual(sum_range_list([1, 2, 3], 0, -1), 0)

    def test_sum_range_list_negative_numbers(self):
        self.assertEqual(sum_range_list([-1, -2, -3], 1, 2), 4)

    def test_sum_range_list_negative_start(self):
        self.assertEqual(sum_range_list([-1, -2, -3], 2, 1), -4)

    def test_sum_range_list_negative_end(self):
        self.assertEqual(sum_range_list([-1, -2, -3], 2, 0), -2)
