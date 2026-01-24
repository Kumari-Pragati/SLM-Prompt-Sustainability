import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 10), 0)

    def test_list_with_no_numbers_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12], 10, 20), 0)

    def test_list_with_numbers_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1, 12), 11)

    def test_list_with_numbers_out_of_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 30], 15, 25), 0)

    def test_list_with_numbers_in_range_and_out_of_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 30], 1, 20), 11)
