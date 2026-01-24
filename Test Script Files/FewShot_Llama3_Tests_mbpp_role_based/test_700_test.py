import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 10), 0)

    def test_no_numbers_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12], 10, 11), 0)

    def test_numbers_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1, 12), 11)

    def test_numbers_in_range_with_duplicates(self):
        self.assertEqual(count_range_in_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12], 1, 12), 11)

    def test_min_greater_than_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12, 1), 0)

    def test_min_equal_to_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12, 12), 1)
