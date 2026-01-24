import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_simple_odd_numbers(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))

    def test_simple_even_numbers(self):
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(6))

    def test_boundary_conditions(self):
        self.assertFalse(is_odd(0))
        self.assertTrue(is_odd(-1))
        self.assertFalse(is_odd(-2))

    def test_large_numbers(self):
        self.assertTrue(is_odd(997))
        self.assertFalse(is_odd(1000))

    def test_negative_large_numbers(self):
        self.assertTrue(is_odd(-997))
        self.assertFalse(is_odd(-1000))
