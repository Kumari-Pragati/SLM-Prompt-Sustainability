import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 10), 0)

    def test_all_in_range(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)

    def test_all_out_of_range(self):
        self.assertEqual(count_range_in_list([10, 20, 30, 40, 50], 1, 5), 0)

    def test_mix_in_range_and_out_of_range(self):
        self.assertEqual(count_range_in_list([1, 10, 20, 3, 40, 5], 1, 5), 3)

    def test_min_max_same(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 3, 3), 1)

    def test_min_greater_than_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 5, 1), 0)
