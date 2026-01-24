import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 1), '[(2, 3, 4), (7, 8, 9)]')

    def test_edge_case_K_zero(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 0), '[(1, 2, 3, 4), (6, 7, 8, 9)]')

    def test_edge_case_K_equal_to_N_minus_K(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 3), '[(3, 4, 5), (8, 9, 10)]')

    def test_edge_case_K_greater_than_N_minus_K(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 5), '[(4, 5), (9, 10)]')

    def test_edge_case_N_minus_K_zero(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 3, 2), '[(3, 4), (8, 9)]')

    def test_edge_case_N_minus_K_equal_to_K(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2, 2), '[(3, 4), (8, 9)]')

    def test_edge_case_N_minus_K_greater_than_K(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2, 3), '[(3, 4), (8, 9)]')

    def test_edge_case_N_minus_K_zero_and_K_zero(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 0, 0), '[(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]')

    def test_edge_case_N_minus_K_equal_to_K_and_K_zero(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2, 2), '[(3, 4), (8, 9)]')

    def test_edge_case_N_minus_K_greater_than_K_and_K_zero(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 3, 0), '[(1, 2, 3, 4), (6, 7, 8, 9)]')
