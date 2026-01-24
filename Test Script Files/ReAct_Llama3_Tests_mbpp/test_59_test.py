import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_octagonal(1))
        self.assertTrue(is_octagonal(2))
        self.assertTrue(is_octagonal(3))

    def test_negative_numbers(self):
        self.assertFalse(is_octagonal(-1))
        self.assertFalse(is_octagonal(-2))
        self.assertFalse(is_octagonal(-3))

    def test_zero(self):
        self.assertFalse(is_octagonal(0))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            is_octagonal(1.5)

    def test_edge_cases(self):
        self.assertTrue(is_octagonal(4))
        self.assertFalse(is_octagonal(5))
