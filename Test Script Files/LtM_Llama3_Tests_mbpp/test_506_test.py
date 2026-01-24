import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(2, 1), 2)
        self.assertEqual(permutation_coefficient(3, 1), 6)
        self.assertEqual(permutation_coefficient(4, 2), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(permutation_coefficient(0, 1), 0)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(1, 2), 1)
        self.assertEqual(permutation_coefficient(2, 0), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            permutation_coefficient('a', 1)
        with self.assertRaises(TypeError):
            permutation_coefficient(1, 'b')
