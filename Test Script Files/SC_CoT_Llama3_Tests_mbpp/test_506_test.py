import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(permutation_coefficient(5, 3), 10)

    def test_edge_cases(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(2, 0), 1)
        self.assertEqual(permutation_coefficient(2, 1), 2)
        self.assertEqual(permutation_coefficient(2, 2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            permutation_coefficient('a', 3)
        with self.assertRaises(TypeError):
            permutation_coefficient(5, 'b')

    def test_special_cases(self):
        self.assertEqual(permutation_coefficient(3, 1), 3)
        self.assertEqual(permutation_coefficient(4, 2), 6)
        self.assertEqual(permutation_coefficient(5, 5), 1)
