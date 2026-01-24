import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)

    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 10), 0)

    def test_single_value_in_range(self):
        self.assertEqual(count_range_in_list([5], 1, 10), 1)

    def test_single_value_out_of_range(self):
        self.assertEqual(count_range_in_list([15], 1, 10), 0)

    def test_multiple_values_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 8), 8)

    def test_multiple_values_mixed_range(self):
        self.assertEqual(count_range_in_list([1, 15, 3, 4, 5, 10, 7, 8, 9, 11], 2, 8), 4)

    def test_min_greater_than_max(self):
        with self.assertRaises(ValueError):
            count_range_in_list([1, 2, 3], 4, 3)

    def test_negative_numbers(self):
        self.assertEqual(count_range_in_list([-5, -4, -3, -2, -1], -4, -2), 3)

    def test_zero_in_range(self):
        self.assertEqual(count_range_in_list([0], 0, 10), 1)

    def test_float_numbers(self):
        self.assertEqual(count_range_in_list([1.5, 2.5, 3.5], 2, 4), 2)
