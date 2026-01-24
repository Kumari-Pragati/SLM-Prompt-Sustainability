import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 2, 4), [3, 4])

    def test_empty_input(self):
        self.assertEqual(remove_list_range([], 2, 4), [])

    def test_single_element_input(self):
        self.assertEqual(remove_list_range([5], 2, 4), [])

    def test_left_range_edge(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 1, 4), [1, 2, 3, 4])

    def test_right_range_edge(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 2, 5), [2, 3, 4, 5])

    def test_left_range_inside(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 2, 4), [2, 3, 4])

    def test_right_range_inside(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 2, 4), [2, 3, 4])

    def test_left_range_outside(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 6, 4), [])

    def test_right_range_outside(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 2, 6), [2, 3, 4, 5])

    def test_left_and_right_range_edges(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 1, 5), [1, 2, 3, 4, 5])

    def test_left_and_right_range_inside(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 2, 4), [2, 3, 4])

    def test_left_and_right_range_outside(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 6, 6), [])
