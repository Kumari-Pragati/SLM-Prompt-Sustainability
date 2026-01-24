import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)

    def test_edge_case_min(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 4), 5)

    def test_edge_case_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)

    def test_edge_case_min_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)

    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 5), 0)

    def test_list_outside_range(self):
        self.assertEqual(count_range_in_list([6, 7, 8], 2, 4), 0)

    def test_list_with_negative_numbers(self):
        self.assertEqual(count_range_in_list([-1, 0, 1], -1, 1), 3)
