import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_simple_odd_numbers(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))

    def test_simple_even_numbers(self):
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))

    def test_edge_cases(self):
        self.assertTrue(is_odd(-1))
        self.assertTrue(is_odd(2**31 - 1))  # Python's largest int
        self.assertFalse(is_odd(2**31))  # Python's largest int + 1

    def test_complex_cases(self):
        self.assertTrue(is_odd(2**15 + 1))  # 2^15 + 1 is an odd number
        self.assertFalse(is_odd(-(2**15 + 1)))  # negative of an odd number
