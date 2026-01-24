import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 1), '[(2, 3), (5, 6), (8, 9)]')

    def test_edge_case_empty_list(self):
        self.assertEqual(trim_tuple([], 0), '[]')

    def test_edge_case_single_element(self):
        self.assertEqual(trim_tuple([(1,)], 0), '[(1,)]')

    def test_edge_case_single_element_right(self):
        self.assertEqual(trim_tuple([(1,)], 1), '[]')

    def test_edge_case_odd_length(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4), (5, 6, 7)], 2), '[(3, 4), (6, 7)]')

    def test_edge_case_even_length(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4), (5, 6)], 2), '[(3, 4), (6,)]')

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: trim_tuple([(1, 2, 3), (4, 5, 6)], -1))
