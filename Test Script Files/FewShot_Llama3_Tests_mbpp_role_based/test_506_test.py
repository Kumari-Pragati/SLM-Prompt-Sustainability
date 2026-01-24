import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(permutation_coefficient(5, 2), 10)

    def test_edge_case_n_zero(self):
        self.assertEqual(permutation_coefficient(0, 2), 1)

    def test_edge_case_k_zero(self):
        self.assertEqual(permutation_coefficient(5, 0), 1)

    def test_edge_case_n_and_k_zero(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(-1, 2)

    def test_invalid_input_k_negative(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(5, -2)

    def test_invalid_input_n_and_k_negative(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(-1, -2)
