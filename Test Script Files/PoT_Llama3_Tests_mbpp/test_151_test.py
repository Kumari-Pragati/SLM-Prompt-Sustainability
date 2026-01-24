import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_coprime(self):
        self.assertTrue(is_coprime(2, 3))
        self.assertTrue(is_coprime(5, 7))
        self.assertTrue(is_coprime(11, 13))

    def test_non_coprime(self):
        self.assertFalse(is_coprime(2, 4))
        self.assertFalse(is_coprime(3, 6))
        self.assertFalse(is_coprime(4, 8))

    def test_edge_cases(self):
        self.assertTrue(is_coprime(1, 1))
        self.assertTrue(is_coprime(1, 2))
        self.assertTrue(is_coprime(2, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_coprime('a', 3)
        with self.assertRaises(TypeError):
            is_coprime(2, 'b')
