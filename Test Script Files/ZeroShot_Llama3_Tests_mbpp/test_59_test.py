import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_is_octagonal_positive(self):
        self.assertTrue(is_octagonal(1))
        self.assertTrue(is_octagonal(2))
        self.assertTrue(is_octagonal(3))
        self.assertTrue(is_octagonal(4))
        self.assertTrue(is_octagonal(5))

    def test_is_octagonal_negative(self):
        self.assertFalse(is_octagonal(-1))
        self.assertFalse(is_octagonal(-2))
        self.assertFalse(is_octagonal(-3))
        self.assertFalse(is_octagonal(-4))
        self.assertFalse(is_octagonal(-5))

    def test_is_octagonal_zero(self):
        self.assertFalse(is_octagonal(0))

    def test_is_octagonal_non_integer(self):
        self.assertFalse(is_octagonal(1.5))
