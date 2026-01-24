import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 2, 4), 10)
        self.assertEqual(sum_Range_list([10, 20, 30, 40, 50], 3, 4), 100)

    def test_empty_list(self):
        self.assertEqual(sum_Range_list([], 1, 2), 0)

    def test_single_number(self):
        self.assertEqual(sum_Range_list([1], 1, 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(sum_Range_list([-1, -2, -3], 1, 3), -6)

    def test_negative_numbers_and_positive(self):
        self.assertEqual(sum_Range_list([-1, 1, -2, 2], 1, 4), 1)

    def test_out_of_range_start(self):
        self.assertEqual(sum_Range_list([1, 2, 3], 4, 5), 0)

    def test_out_of_range_end(self):
        self.assertEqual(sum_Range_list([1, 2, 3], 1, 0), 0)
