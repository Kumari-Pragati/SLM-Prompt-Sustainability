import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(is_coprime(2, 3))

    def test_boundary_condition(self):
        self.assertTrue(is_coprime(1, 1))

    def test_edge_condition(self):
        self.assertFalse(is_coprime(4, 8))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_coprime("2", 3)
