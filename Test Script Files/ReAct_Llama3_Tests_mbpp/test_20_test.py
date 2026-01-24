import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_even_numbers(self):
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(6))

    def test_odd_numbers(self):
        self.assertTrue(is_woodall(1))
        self.assertFalse(is_woodall(3))
        self.assertFalse(is_woodall(5))

    def test_prime_numbers(self):
        self.assertTrue(is_woodall(2))
        self.assertTrue(is_woodall(3))
        self.assertFalse(is_woodall(5))

    def test_power_of_two(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(2))
        self.assertFalse(is_woodall(4))

    def test_edge_cases(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(8))
