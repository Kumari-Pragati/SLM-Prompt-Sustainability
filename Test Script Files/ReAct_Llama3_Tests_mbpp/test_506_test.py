import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(permutation_coefficient(5, 3), 10)

    def test_edge_case_n_zero(self):
        self.assertEqual(permutation_coefficient(0, 3), 0)

    def test_edge_case_k_zero(self):
        self.assertEqual(permutation_coefficient(5, 0), 1)

    def test_edge_case_k_equal_n(self):
        self.assertEqual(permutation_coefficient(5, 5), 1)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(permutation_coefficient(5, 6), 0)

    def test_edge_case_k_negative(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(5, -1)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(-1, 3)
