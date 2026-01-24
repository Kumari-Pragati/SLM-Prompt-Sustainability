import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(permutation_coefficient(5, 2), 20)

    def test_edge_case_zero_k(self):
        self.assertEqual(permutation_coefficient(5, 0), 1)

    def test_edge_case_zero_n(self):
        self.assertEqual(permutation_coefficient(0, 2), 0)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(permutation_coefficient(5, 10), 0)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(Exception):
            permutation_coefficient(-5, 2)

    def test_invalid_input_negative_k(self):
        with self.assertRaises(Exception):
            permutation_coefficient(5, -2)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(Exception):
            permutation_coefficient(5.5, 2)

    def test_invalid_input_non_integer_k(self):
        with self.assertRaises(Exception):
            permutation_coefficient(5, 2.2)
