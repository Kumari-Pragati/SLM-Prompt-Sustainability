import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9], 2), [1, 3, 5, 7, 9])

    def test_boundary_case_n_equals_1(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9], 1), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_boundary_case_n_equals_0(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9], 0), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(nth_items([], 2), [])

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            nth_items("not a list", 2)
        with self.assertRaises(TypeError):
            nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9], "not an integer")
