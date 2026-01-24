import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(permutation_coefficient(3, 1), 1)
        self.assertEqual(permutation_coefficient(3, 2), 3)
        self.assertEqual(permutation_coefficient(3, 3), 6)
        self.assertEqual(permutation_coefficient(4, 2), 6)
        self.assertEqual(permutation_coefficient(4, 3), 12)
        self.assertEqual(permutation_coefficient(4, 4), 24)

    def test_edge_cases(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(0, 1), 0)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(2, 0), 0)
        self.assertEqual(permutation_coefficient(2, 2), 2)
        self.assertEqual(permutation_coefficient(3, 0), 0)
        self.assertEqual(permutation_coefficient(3, 4), 0)

    def test_boundary_cases(self):
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(2, 1), 2)
        self.assertEqual(permutation_coefficient(2, 2), 2)
        self.assertEqual(permutation_coefficient(3, 1), 3)
        self.assertEqual(permutation_coefficient(3, 2), 6)
        self.assertEqual(permutation_coefficient(3, 3), 6)
