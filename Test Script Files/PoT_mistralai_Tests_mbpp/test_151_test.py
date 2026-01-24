import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_coprime(2, 3))
        self.assertTrue(is_coprime(5, 7))
        self.assertTrue(is_coprime(11, 13))

    def test_edge_cases(self):
        self.assertFalse(is_coprime(0, 2))
        self.assertFalse(is_coprime(2, 0))
        self.assertFalse(is_coprime(1, 1))
        self.assertTrue(is_coprime(2, 4))

    def test_boundary_cases(self):
        self.assertTrue(is_coprime(-2, 3))
        self.assertTrue(is_coprime(2, -3))
        self.assertTrue(is_coprime(-2, -3))
