import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_coprime(15, 17))

    def test_boundary_case(self):
        self.assertTrue(is_coprime(1, 2))

    def test_edge_case(self):
        self.assertTrue(is_coprime(1, 1))
        self.assertFalse(is_coprime(2, 2))

    def test_special_case(self):
        self.assertTrue(is_coprime(10000, 10001))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_coprime('15', 17)
        with self.assertRaises(TypeError):
            is_coprime(15, '17')
        with self.assertRaises(TypeError):
            is_coprime('15', '17')
