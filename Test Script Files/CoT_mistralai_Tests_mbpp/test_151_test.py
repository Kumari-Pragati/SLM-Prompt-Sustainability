import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_coprime(3, 5))
        self.assertTrue(is_coprime(29, 41))

    def test_edge_case_1(self):
        self.assertTrue(is_coprime(2, 3))
        self.assertTrue(is_coprime(3, 2))

    def test_edge_case_2(self):
        self.assertFalse(is_coprime(4, 3))
        self.assertFalse(is_coprime(3, 4))

    def test_edge_case_3(self):
        self.assertTrue(is_coprime(1, 3))
        self.assertTrue(is_coprime(3, 1))

    def test_edge_case_4(self):
        self.assertFalse(is_coprime(0, 3))
        self.assertFalse(is_coprime(3, 0))

    def test_invalid_input(self):
        self.assertRaises(TypeError, is_coprime, "a", 3)
        self.assertRaises(TypeError, is_coprime, 3, "a")
