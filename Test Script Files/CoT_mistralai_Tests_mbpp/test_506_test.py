import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(permutation_coefficient(4, 2), 6)
        self.assertEqual(permutation_coefficient(5, 3), 10)
        self.assertEqual(permutation_coefficient(6, 4), 15)

    def test_edge_case_small_n(self):
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(0, 0), 1)

    def test_edge_case_small_k(self):
        self.assertEqual(permutation_coefficient(4, 0), 1)
        self.assertEqual(permutation_coefficient(4, 1), 4)
        self.assertEqual(permutation_coefficient(4, 4), 24)

    def test_edge_case_large_k(self):
        self.assertEqual(permutation_coefficient(4, 5), 0)
        self.assertEqual(permutation_coefficient(5, 6), 0)

    def test_invalid_input_negative_n(self):
        self.assertRaises(ValueError, permutation_coefficient, -1, 2)

    def test_invalid_input_negative_k(self):
        self.assertRaises(ValueError, permutation_coefficient, 4, -2)
