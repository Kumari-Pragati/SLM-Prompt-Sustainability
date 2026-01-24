import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(is_octagonal(1), 3)
        self.assertEqual(is_octagonal(2), 12)
        self.assertEqual(is_octagonal(3), 39)
        self.assertEqual(is_octagonal(4), 100)
        self.assertEqual(is_octagonal(5), 165)

    def test_zero(self):
        self.assertEqual(is_octagonal(0), -2)

    def test_negative_integer(self):
        self.assertEqual(is_octagonal(-1), -3)
        self.assertEqual(is_octagonal(-2), -12)
        self.assertEqual(is_octagonal(-3), -39)
        self.assertEqual(is_octagonal(-4), -100)
        self.assertEqual(is_octagonal(-5), -165)
