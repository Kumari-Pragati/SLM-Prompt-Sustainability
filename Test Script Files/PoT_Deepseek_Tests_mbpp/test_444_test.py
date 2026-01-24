import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 1), '[(2, 3, 4)]')

    def test_edge_case_K_equals_0(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 0), '[(1, 2, 3, 4, 5)]')

    def test_boundary_case_K_equals_N_minus_1(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 4), '[]')

    def test_corner_case_K_greater_than_N(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 5), '[]')

    def test_invalid_input_K_negative(self):
        with self.assertRaises(Exception):
            trim_tuple([(1, 2, 3, 4, 5)], -1)

    def test_invalid_input_K_greater_than_length_of_tuple(self):
        with self.assertRaises(Exception):
            trim_tuple([(1, 2, 3, 4, 5)], 6)
