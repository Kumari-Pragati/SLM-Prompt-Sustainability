import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):
    def test_simple_even(self):
        self.assertFalse(is_woodall(2))

    def test_simple_one(self):
        self.assertTrue(is_woodall(1))

    def test_simple_odd(self):
        self.assertTrue(is_woodall(3))

    def test_edge_zero(self):
        self.assertFalse(is_woodall(0))

    def test_edge_maximum(self):
        self.assertTrue(is_woodall(2147483647))

    def test_edge_minimum(self):
        self.assertTrue(is_woodall(-2147483648))

    def test_complex_powers_of_two(self):
        for i in range(1, 16):
            self.assertTrue(is_woodall(2**i))

    def test_complex_composite_numbers(self):
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(5))
        self.assertFalse(is_woodall(6))
        self.assertFalse(is_woodall(7))
        self.assertFalse(is_woodall(8))
        self.assertFalse(is_woodall(9))
        self.assertFalse(is_woodall(10))
        self.assertFalse(is_woodall(11))
        self.assertFalse(is_woodall(12))
        self.assertFalse(is_woodall(13))
        self.assertFalse(is_woodall(14))
        self.assertFalse(is_woodall(15))
        self.assertFalse(is_woodall(16))
        self.assertFalse(is_woodall(17))
        self.assertFalse(is_woodall(18))
        self.assertFalse(is_woodall(19))
        self.assertFalse(is_woodall(20))
