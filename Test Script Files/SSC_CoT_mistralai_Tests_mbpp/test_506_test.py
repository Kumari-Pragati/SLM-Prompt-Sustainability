import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(permutation_coefficient(4, 2), 6)
        self.assertEqual(permutation_coefficient(5, 3), 10)
        self.assertEqual(permutation_coefficient(6, 4), 15)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(0, 1), 0)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(2, 0), 1)
        self.assertEqual(permutation_coefficient(2, 2), 2)
        self.assertEqual(permutation_coefficient(3, 0), 1)
        self.assertEqual(permutation_coefficient(3, 3), 6)
        self.assertEqual(permutation_coefficient(4, 0), 1)
        self.assertEqual(permutation_coefficient(4, 4), 24)
        self.assertEqual(permutation_coefficient(5, 0), 1)
        self.assertEqual(permutation_coefficient(5, 5), 120)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, permutation_coefficient, -1, 2)
        self.assertRaises(ValueError, permutation_coefficient, 1, -1)
