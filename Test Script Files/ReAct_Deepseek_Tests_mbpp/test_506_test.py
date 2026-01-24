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

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            permutation_coefficient("3", 2)
        with self.assertRaises(TypeError):
            permutation_coefficient(3, "2")
        with self.assertRaises(ValueError):
            permutation_coefficient(-1, 2)
        with self.assertRaises(ValueError):
            permutation_coefficient(3, -1)
        with self.assertRaises(ValueError):
            permutation_coefficient(3, 4)
