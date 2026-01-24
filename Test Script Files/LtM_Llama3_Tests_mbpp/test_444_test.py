import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 1), '[(2, 3), (5, 6)]')

    def test_empty_input(self):
        self.assertEqual(trim_tuple([], 1), '[]')

    def test_single_element(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 1), '[(1, 2, 3)]')

    def test_k_out_of_range(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 4), '[]')

    def test_k_equal_to_zero(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 0), '[(1, 2, 3)]')

    def test_k_equal_to_length(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 2), '[(2, 3)]')

    def test_k_greater_than_length(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 4), '[]')
