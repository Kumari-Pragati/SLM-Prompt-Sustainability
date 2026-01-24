import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_coprime(3, 4))

    def test_typical_case_2(self):
        self.assertTrue(is_coprime(5, 6))

    def test_edge_case_1(self):
        self.assertTrue(is_coprime(1, 1))

    def test_edge_case_2(self):
        self.assertFalse(is_coprime(2, 2))

    def test_boundary_case_1(self):
        self.assertTrue(is_coprime(0, 1))

    def test_boundary_case_2(self):
        self.assertTrue(is_coprime(1, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_coprime("a", 1)

        with self.assertRaises(TypeError):
            is_coprime(1, "b")

        with self.assertRaises(TypeError):
            is_coprime("a", "b")
