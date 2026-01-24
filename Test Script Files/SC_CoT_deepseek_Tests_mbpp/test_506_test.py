import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(permutation_coefficient(5, 2), 20)
        self.assertEqual(permutation_coefficient(3, 1), 3)

    def test_boundary_conditions(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(2, 1), 2)

    def test_edge_cases(self):
        self.assertEqual(permutation_coefficient(0, 1), 0)
        self.assertEqual(permutation_coefficient(1, 2), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            permutation_coefficient(-1, 2)
        with self.assertRaises(Exception):
            permutation_coefficient(2, -1)
        with self.assertRaises(Exception):
            permutation_coefficient(2.5, 1)
        with self.assertRaises(Exception):
            permutation_coefficient(1, 1.5)
