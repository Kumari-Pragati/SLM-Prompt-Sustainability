import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_is_nonagonal_positive(self):
        self.assertEqual(is_nonagonal(3), 6)
        self.assertEqual(is_nonagonal(5), 20)
        self.assertEqual(is_nonagonal(7), 42)
        self.assertEqual(is_nonagonal(9), 81)
        self.assertEqual(is_nonagonal(10), 120)

    def test_is_nonagonal_zero(self):
        self.assertEqual(is_nonagonal(0), 0)

    def test_is_nonagonal_negative(self):
        self.assertEqual(is_nonagonal(-1), -2)
        self.assertEqual(is_nonagonal(-2), -4)
        self.assertEqual(is_nonagonal(-3), -6)
        self.assertEqual(is_nonagonal(-4), -16)
        self.assertEqual(is_nonagonal(-5), -30)
