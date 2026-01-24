import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 7), [4, 5, 6, 7])

    def test_edge_case_left(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 7), [1, 2, 3, 4, 5, 6, 7])

    def test_edge_case_right(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 10), [3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case_left_and_right(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_empty_list(self):
        self.assertEqual(remove_list_range([], 1, 10), [])

    def test_single_element_list(self):
        self.assertEqual(remove_list_range([5], 1, 10), [5])

    def test_list_outside_range(self):
        self.assertEqual(remove_list_range([11, 12, 13], 1, 10), [])

    def test_list_outside_range_left(self):
        self.assertEqual(remove_list_range([11, 12, 13], 15, 20), [])

    def test_list_outside_range_right(self):
        self.assertEqual(remove_list_range([11, 12, 13], 1, 20), [])
