import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):
    def test_positive_range_in_list(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)

    def test_empty_list(self):
        self.assertEqual(count_range_in_list([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_range_in_list([-1, -2, -3, -4, -5], -2, -4), 4)

    def test_min_greater_than_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 6, 2), 0)

    def test_min_equal_to_max(self):
        self.assertEqual(count_range_in_list([1, 1, 3, 4, 5], 1, 1), 1)

    def test_min_equal_to_list_min(self):
        self.assertEqual(count_range_in_list([-1, -1, -3, -4, -5], -1, -1), 1)

    def test_min_equal_to_list_max(self):
        self.assertEqual(count_range_in_list([1, 1, 3, 4, 5], 1, 5), 5)

    def test_list_contains_non_numeric_value(self):
        self.assertRaises(TypeError, count_range_in_list, [1, 'a', 3, 4, 5], 2, 4)
