import unittest
from700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)
        self.assertEqual(count_range_in_list([-1, 0, 1, 2, 3], -1, 3), 4)
        self.assertEqual(count_range_in_list([0, 0, 1, 0, 0], 0, 1), 2)

    def test_edge_case_min_equal_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3], 3, 3), 1)
        self.assertEqual(count_range_in_list([-1, 0, 1], -1, -1), 1)

    def test_edge_case_min_greater_max(self):
        self.assertEqual(count_range_in_list([1, 2, 3], 4, 3), 0)
        self.assertEqual(count_range_in_list([-1, 0, 1], 2, -1), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 5), 0)

    def test_corner_case_min_equal_first_element(self):
        self.assertEqual(count_range_in_list([1, 1, 2, 3], 1, 3), 3)

    def test_corner_case_min_equal_last_element(self):
        self.assertEqual(count_range_in_list([1, 2, 2], 2, 3), 2)

    def test_corner_case_min_greater_first_and_last_element(self):
        self.assertEqual(count_range_in_list([1, 2, 3], 4, 3), 0)
