import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2), '[(3, 4), (8, 9)]')

    def test_edge_case_short_list(self):
        self.assertEqual(trim_tuple([(1, 2), (3, 4)], 1), '[(2)]')

    def test_edge_case_empty_list(self):
        self.assertEqual(trim_tuple([], 2), '[]')

    def test_edge_case_single_element(self):
        self.assertEqual(trim_tuple([(1,)], 0), '[]')
        self.assertEqual(trim_tuple([(1,)], 1), '[(1)]')

    def test_corner_case_negative_k(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], -1), '[]')

    def test_corner_case_k_greater_than_length(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 4), '[(3)]')
