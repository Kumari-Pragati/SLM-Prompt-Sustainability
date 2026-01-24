import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(modular_inverse([2, 3, 4, 5], 4, 7), 1)

    def test_edge_case_N_zero(self):
        with self.assertRaises(IndexError):
            modular_inverse([], 0, 7)

    def test_edge_case_P_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modular_inverse([2, 3, 4, 5], 4, 0)

    def test_edge_case_N_one(self):
        self.assertEqual(modular_inverse([2], 1, 7), 1)

    def test_edge_case_P_one(self):
        self.assertEqual(modular_inverse([2], 4, 1), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            modular_inverse("hello", 4, 7)
