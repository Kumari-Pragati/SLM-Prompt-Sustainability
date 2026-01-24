import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edge_case_empty_list(self):
        self.assertEqual(add_list([], [1, 2, 3]), [])
        self.assertEqual(add_list([1, 2, 3], []), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(add_list([1], [2]), [3])
        self.assertEqual(add_list([1], []), [1])
        self.assertEqual(add_list([], [1]), [1])

    def test_edge_case_equal_length_lists(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(add_list([1, 2], [3, 4]), [4, 6])

    def test_edge_case_lists_of_different_lengths(self):
        self.assertEqual(add_list([1, 2, 3, 4], [5, 6]), [6, 8])
        self.assertEqual(add_list([1, 2], [3, 4, 5, 6]), [4, 6])
