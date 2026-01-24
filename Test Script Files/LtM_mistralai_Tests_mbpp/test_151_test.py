import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_simple_coprime(self):
        self.assertTrue(is_coprime(5, 2))
        self.assertTrue(is_coprime(11, 3))

    def test_simple_not_coprime(self):
        self.assertFalse(is_coprime(6, 4))
        self.assertFalse(is_coprime(10, 5))

    def test_edge_cases(self):
        self.assertTrue(is_coprime(2, 1))
        self.assertTrue(is_coprime(1, 2))
        self.assertFalse(is_coprime(0, 1))
        self.assertFalse(is_coprime(-1, 1))

    def test_boundary_cases(self):
        self.assertTrue(is_coprime(2**31 - 1, 2**31 - 2))  # max int
        self.assertTrue(is_coprime(-2**31 + 1, -2**31 + 2))  # min int
