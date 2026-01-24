import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(permutation_coefficient(3, 2), 2)
        self.assertEqual(permutation_coefficient(4, 2), 6)
        self.assertEqual(permutation_coefficient(5, 3), 20)

    def test_edge_cases(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(2, 1), 2)

    def test_boundary_cases(self):
        self.assertEqual(permutation_coefficient(10, 10), 3628800)
        self.assertEqual(permutation_coefficient(10, 9), 362880)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            permutation_coefficient(-1, 2)
        with self.assertRaises(Exception):
            permutation_coefficient(2, -1)
        with self.assertRaises(Exception):
            permutation_coefficient(2, 3)
