import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):
    def test_coprime_numbers(self):
        self.assertTrue(is_coprime(1, 1))
        self.assertTrue(is_coprime(2, 3))
        self.assertTrue(is_coprime(5, 7))

    def test_non_coprime_numbers(self):
        self.assertFalse(is_coprime(4, 2))
        self.assertFalse(is_coprime(6, 3))
        self.assertFalse(is_coprime(8, 4))

    def test_edge_cases(self):
        self.assertTrue(is_coprime(0, 0))
        self.assertFalse(is_coprime(0, 1))
        self.assertFalse(is_coprime(1, 0))

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            is_coprime('a', 2)
