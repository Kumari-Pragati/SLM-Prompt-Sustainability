import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(is_nonagonal(3), 6)
        self.assertEqual(is_nonagonal(4), 20)
        self.assertEqual(is_nonagonal(5), 35)
        self.assertEqual(is_nonagonal(6), 56)
        self.assertEqual(is_nonagonal(7), 77)
        self.assertEqual(is_nonagonal(8), 100)
        self.assertEqual(is_nonagonal(9), 125)
        self.assertEqual(is_nonagonal(10), 151)

    def test_zero(self):
        self.assertEqual(is_nonagonal(0), 0)

    def test_negative_integer(self):
        self.assertRaises(ValueError, is_nonagonal, -1)
        self.assertRaises(ValueError, is_nonagonal, -2)
        self.assertRaises(ValueError, is_nonagonal, -3)

    def test_float(self):
        self.assertRaises(TypeError, is_nonagonal, 2.5)

    def test_string(self):
        self.assertRaises(TypeError, is_nonagonal, "test")
