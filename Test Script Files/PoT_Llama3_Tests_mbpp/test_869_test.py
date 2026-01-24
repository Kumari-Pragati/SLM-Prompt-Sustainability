import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7), [4, 5, 6, 7])

    def test_edge_case_left(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 7), [1, 2, 3, 4, 5, 6, 7])

    def test_edge_case_right(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 9), [3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_left_and_right(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_empty_list(self):
        self.assertEqual(remove_list_range([], 1, 9), [])

    def test_single_element_list(self):
        self.assertEqual(remove_list_range([5], 1, 9), [5])

    def test_single_element_list_out_of_range(self):
        self.assertEqual(remove_list_range([10], 1, 9), [])

    def test_list_out_of_range(self):
        self.assertEqual(remove_list_range([10, 11, 12], 1, 9), [])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_list_range([1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9], 2, 7), [2, 3, 4, 5, 6, 7])
