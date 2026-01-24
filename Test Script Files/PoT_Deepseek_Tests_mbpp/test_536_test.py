import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9], 2), [1, 3, 5, 7, 9])

    def test_edge_case_with_empty_list(self):
        self.assertEqual(nth_items([], 2), [])

    def test_boundary_case_with_n_equal_to_1(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])

    def test_boundary_case_with_n_equal_to_0(self):
        with self.assertRaises(IndexError):
            nth_items([1, 2, 3, 4, 5], 0)

    def test_corner_case_with_large_n(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 10), [])
