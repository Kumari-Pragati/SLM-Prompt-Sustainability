import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(permutation_coefficient(5, 2), 20)

    def test_boundary_conditions(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(1, 1), 1)

    def test_edge_conditions(self):
        self.assertEqual(permutation_coefficient(0, 1), 0)
        self.assertEqual(permutation_coefficient(2, 3), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            permutation_coefficient('5', 2)
        with self.assertRaises(TypeError):
            permutation_coefficient(5, '2')
        with self.assertRaises(ValueError):
            permutation_coefficient(-1, 2)
        with self.assertRaises(ValueError):
            permutation_coefficient(5, -1)
