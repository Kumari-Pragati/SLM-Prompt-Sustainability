import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_single_element(self):
        self.assertEqual(sum_range_list([10], 0, 0), 10)

    def test_empty_list(self):
        self.assertEqual(sum_range_list([], 0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_range_list([-1, -2, -3, -4, -5], 1, 3), -6)

    def test_out_of_range_indices(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 5, 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_range_list("not a list", 0, 0)
