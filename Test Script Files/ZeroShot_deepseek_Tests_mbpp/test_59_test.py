import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_octagonal(1))
        self.assertTrue(is_octagonal(2))
        self.assertTrue(is_octagonal(3))
        self.assertTrue(is_octagonal(4))
        self.assertTrue(is_octagonal(5))
        self.assertTrue(is_octagonal(6))
        self.assertTrue(is_octagonal(7))
        self.assertTrue(is_octagonal(8))
        self.assertTrue(is_octagonal(9))
        self.assertTrue(is_octagonal(10))

    def test_negative_numbers(self):
        self.assertFalse(is_octagonal(-1))
        self.assertFalse(is_octagonal(-2))
        self.assertFalse(is_octagonal(-3))
        self.assertFalse(is_octagonal(-4))
        self.assertFalse(is_octagonal(-5))
        self.assertFalse(is_octagonal(-6))
        self.assertFalse(is_octagonal(-7))
        self.assertFalse(is_octagonal(-8))
        self.assertFalse(is_octagonal(-9))
        self.assertFalse(is_octagonal(-10))

    def test_zero(self):
        self.assertTrue(is_octagonal(0))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_octagonal(1.5)

    def test_large_numbers(self):
        self.assertTrue(is_octagonal(10000))
        self.assertFalse(is_octagonal(10001))
