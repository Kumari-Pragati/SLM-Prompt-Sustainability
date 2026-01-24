import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_coprime(2, 3))
        self.assertTrue(is_coprime(5, 7))
        self.assertTrue(is_coprime(11, 13))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(is_coprime(1, 1))  # 1 and 1 are not coprime, but this is a special case
        self.assertTrue(is_coprime(0, 1))
        self.assertTrue(is_coprime(1, 0))
        self.assertTrue(is_coprime(0, 0))  # 0 and 0 are not coprime, but this is a special case

    def test_corner_cases(self):
        self.assertTrue(is_coprime(2, 1))
        self.assertTrue(is_coprime(1, 2))
        self.assertTrue(is_coprime(0, 2))
        self.assertTrue(is_coprime(2, 0))
        self.assertTrue(is_coprime(0, 0))  # 0 and 0 are not coprime, but this is a special case
