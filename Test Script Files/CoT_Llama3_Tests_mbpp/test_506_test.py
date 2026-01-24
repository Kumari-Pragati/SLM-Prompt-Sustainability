import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_permutation_coefficient_typical(self):
        self.assertEqual(permutation_coefficient(3, 2), 3)

    def test_permutation_coefficient_edge(self):
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(2, 1), 2)
        self.assertEqual(permutation_coefficient(2, 2), 1)

    def test_permutation_coefficient_invalid_input(self):
        with self.assertRaises(TypeError):
            permutation_coefficient('a', 2)
        with self.assertRaises(TypeError):
            permutation_coefficient(3, 'b')

    def test_permutation_coefficient_negative_input(self):
        with self.assertRaises(ValueError):
            permutation_coefficient(-1, 2)
        with self.assertRaises(ValueError):
            permutation_coefficient(3, -2)
