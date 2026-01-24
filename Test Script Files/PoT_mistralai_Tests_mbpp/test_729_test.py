import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edge_case_empty_lists(self):
        self.assertEqual(add_list([], []), [])

    def test_edge_case_single_element(self):
        self.assertEqual(add_list([1], [2]), [3])
        self.assertEqual(add_list([2], [1]), [3])

    def test_edge_case_different_lengths(self):
        self.assertEqual(add_list([1, 2], [3]), [4, 2])
        self.assertEqual(add_list([1, 2], [3, 4]), [4, 6])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(add_list([-1, 2], [-3, 4]), [1, 6])
