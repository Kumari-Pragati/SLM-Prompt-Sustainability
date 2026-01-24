import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(is_octagonal(1), 2)
        self.assertEqual(is_octagonal(2), 8)
        self.assertEqual(is_octagonal(3), 18)
        self.assertEqual(is_octagonal(4), 34)
        self.assertEqual(is_octagonal(5), 54)

    def test_zero(self):
        self.assertEqual(is_octagonal(0), -2)

    def test_negative_integer(self):
        self.assertEqual(is_octagonal(-1), -2)
        self.assertEqual(is_octagonal(-2), -8)
        self.assertEqual(is_octagonal(-3), -18)
        self.assertEqual(is_octagonal(-4), -34)
        self.assertEqual(is_octagonal(-5), -54)

    def test_large_integer(self):
        self.assertEqual(is_octagonal(100), 30002)
        self.assertEqual(is_octagonal(-100), -30002)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            is_octagonal(3.14)
