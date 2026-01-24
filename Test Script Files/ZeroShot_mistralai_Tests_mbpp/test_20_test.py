import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_even_numbers(self):
        for num in range(2, 10):
            self.assertFalse(is_woodall(num))

    def test_one(self):
        self.assertTrue(is_woodall(1))

    def test_odd_numbers(self):
        for num in range(3, 100):
            self.assertTrue(is_woodall(num))

    def test_large_numbers(self):
        for num in range(100, 1000):
            self.assertTrue(is_woodall(num))

    def test_edge_cases(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(3))
        self.assertTrue(is_woodall(5))
        self.assertTrue(is_woodall(7))
