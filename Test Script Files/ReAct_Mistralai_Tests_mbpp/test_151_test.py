import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_coprime(25, 13))

    def test_edge_case_1(self):
        self.assertTrue(is_coprime(1, 1))

    def test_edge_case_2(self):
        self.assertFalse(is_coprime(2, 0))

    def test_edge_case_3(self):
        self.assertFalse(is_coprime(2, 2))

    def test_large_numbers(self):
        self.assertTrue(is_coprime(123456789, 987654321))
