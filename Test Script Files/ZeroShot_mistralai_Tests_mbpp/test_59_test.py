import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_is_octagonal_positive(self):
        self.assertEqual(is_octagonal(1), 2)
        self.assertEqual(is_octagonal(2), 10)
        self.assertEqual(is_octagonal(3), 22)
        self.assertEqual(is_octagonal(4), 42)
        self.assertEqual(is_octagonal(5), 66)

    def test_is_octagonal_zero(self):
        self.assertEqual(is_octagonal(0), 0)

    def test_is_octagonal_negative(self):
        self.assertEqual(is_octagonal(-1), -2)
        self.assertEqual(is_octagonal(-2), -10)
        self.assertEqual(is_octagonal(-3), -22)
        self.assertEqual(is_octagonal(-4), -42)
        self.assertEqual(is_octagonal(-5), -66)
