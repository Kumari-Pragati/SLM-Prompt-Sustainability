import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(permutation_coefficient(2, 1), 2)
        self.assertEqual(permutation_coefficient(3, 2), 6)
        self.assertEqual(permutation_coefficient(4, 3), 24)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(0, 1), 0)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(2, 0), 0)
        self.assertEqual(permutation_coefficient(2, 2), 2)
        self.assertEqual(permutation_coefficient(3, 0), 0)
        self.assertEqual(permutation_coefficient(3, 3), 6)

    def test_complex_inputs(self):
        self.assertEqual(permutation_coefficient(4, 4), 24)
        self.assertEqual(permutation_coefficient(5, 5), 120)
        self.assertEqual(permutation_coefficient(6, 6), 720)
