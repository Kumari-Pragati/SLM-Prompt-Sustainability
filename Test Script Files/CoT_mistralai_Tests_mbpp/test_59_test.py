import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(is_octagonal(1), 3)
        self.assertEqual(is_octagonal(2), 8)
        self.assertEqual(is_octagonal(3), 13)
        self.assertEqual(is_octagonal(4), 24)
        self.assertEqual(is_octagonal(5), 35)
        self.assertEqual(is_octagonal(6), 48)
        self.assertEqual(is_octagonal(7), 63)
        self.assertEqual(is_octagonal(8), 80)
        self.assertEqual(is_octagonal(9), 99)

    def test_zero(self):
        self.assertEqual(is_octagonal(0), -2)

    def test_negative_integer(self):
        self.assertEqual(is_octagonal(-1), -5)
        self.assertEqual(is_octagonal(-2), -12)
        self.assertEqual(is_octagonal(-3), -21)
        self.assertEqual(is_octagonal(-4), -34)
        self.assertEqual(is_octagonal(-5), -49)
        self.assertEqual(is_octagonal(-6), -68)
        self.assertEqual(is_octagonal(-7), -87)
        self.assertEqual(is_octagonal(-8), -108)
        self.assertEqual(is_octagonal(-9), -131)
