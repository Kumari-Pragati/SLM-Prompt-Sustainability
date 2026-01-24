import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(permutation_coefficient(4, 2), 6)

    def test_edge_case_small_n(self):
        self.assertEqual(permutation_coefficient(1, 1), 1)

    def test_edge_case_small_k(self):
        self.assertEqual(permutation_coefficient(4, 0), 1)
        self.assertEqual(permutation_coefficient(4, 1), 4)

    def test_edge_case_large_k(self):
        self.assertEqual(permutation_coefficient(4, 5), 0)

    def test_error_case_negative_n(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(-1, 2)

    def test_error_case_negative_k(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(4, -2)

    def test_error_case_zero_n(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(0, 2)
