import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 5, 7), 1)

    def test_edge_case_N_zero(self):
        with self.assertRaises(IndexError):
            modular_inverse([], 0, 7)

    def test_edge_case_P_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modular_inverse([1, 2, 3, 4, 5], 5, 0)

    def test_edge_case_N_one(self):
        self.assertEqual(modular_inverse([1], 1, 7), 1)

    def test_edge_case_P_one(self):
        self.assertEqual(modular_inverse([1], 5, 1), 1)

    def test_edge_case_N_and_P_one(self):
        self.assertEqual(modular_inverse([1], 1, 1), 1)

    def test_edge_case_N_and_P_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modular_inverse([1, 2, 3, 4, 5], 0, 0)

    def test_edge_case_N_and_P_negative(self):
        with self.assertRaises(ValueError):
            modular_inverse([1, 2, 3, 4, 5], -5, -7)

    def test_edge_case_N_and_P_non_integer(self):
        with self.assertRaises(TypeError):
            modular_inverse([1, 2, 3, 4, 5], 5.5, 7.5)
