import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(is_nonagonal(5), 15)
        self.assertEqual(is_nonagonal(10), 65)

    def test_edge_cases(self):
        self.assertEqual(is_nonagonal(1), 0)
        self.assertEqual(is_nonagonal(2), 6)
        self.assertEqual(is_nonagonal(3), 21)
        self.assertEqual(is_nonagonal(4), 42)
        self.assertEqual(is_nonagonal(6), 102)
        self.assertEqual(is_nonagonal(7), 147)
        self.assertEqual(is_nonagonal(8), 182)
        self.assertEqual(is_nonagonal(9), 213)

    def test_negative_input(self):
        self.assertRaises(ValueError, is_nonagonal, -1)

    def test_zero_input(self):
        self.assertRaises(ValueError, is_nonagonal, 0)

    def test_fractional_input(self):
        self.assertRaises(TypeError, is_nonagonal, 3.14)
