import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7), [4, 5, 6, 7])

    def test_edge_case_left_range(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 7), [1, 2, 3, 4, 5, 6, 7])

    def test_edge_case_right_range(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 9), [3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_left_and_right_range(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_empty_list(self):
        self.assertEqual(remove_list_range([], 1, 9), [])

    def test_single_element_list(self):
        self.assertEqual(remove_list_range([5], 1, 9), [5])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_list_range("abc", 1, 9)

    def test_invalid_input_range_type(self):
        with self.assertRaises(TypeError):
            remove_list_range([1, 2, 3], "abc", 9)
