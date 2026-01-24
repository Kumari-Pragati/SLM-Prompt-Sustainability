import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_permutation_coefficient_basic(self):
        self.assertEqual(permutation_coefficient(4, 2), 12)
        self.assertEqual(permutation_coefficient(5, 3), 20)
        self.assertEqual(permutation_coefficient(6, 4), 30)
        self.assertEqual(permutation_coefficient(7, 5), 42)
        self.assertEqual(permutation_coefficient(8, 6), 56)
        self.assertEqual(permutation_coefficient(9, 7), 72)
        self.assertEqual(permutation_coefficient(10, 8), 90)
        self.assertEqual(permutation_coefficient(10, 9), 45)
        self.assertEqual(permutation_coefficient(10, 10), 1)

    def test_permutation_coefficient_edge_cases(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(0, 1), 0)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(2, 2), 2)
        self.assertEqual(permutation_coefficient(2, 1), 1)
        self.assertEqual(permutation_coefficient(2, 0), 1)
