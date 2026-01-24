import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 5), 2)

    def test_edge_case_with_single_element(self):
        self.assertEqual(modular_inverse([2], 1, 5), 0)

    def test_edge_case_with_zero_elements(self):
        self.assertEqual(modular_inverse([], 0, 5), 0)

    def test_edge_case_with_large_elements(self):
        self.assertEqual(modular_inverse([1000, 2000, 3000], 3, 5000), 2)

    def test_edge_case_with_small_elements(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 2), 0)

    def test_corner_case_with_duplicate_elements(self):
        self.assertEqual(modular_inverse([1, 1, 2], 3, 5), 1)

    def test_invalid_input_case_with_negative_elements(self):
        with self.assertRaises(Exception):
            modular_inverse([-1, -2, -3], 3, 5)

    def test_invalid_input_case_with_zero_modulus(self):
        with self.assertRaises(Exception):
            modular_inverse([1, 2, 3], 3, 0)
