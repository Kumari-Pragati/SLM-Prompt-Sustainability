import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(permutation_coefficient(4, 2), 6)
        self.assertEqual(permutation_coefficient(5, 3), 10)
        self.assertEqual(permutation_coefficient(6, 4), 15)

    def test_zero_and_one(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(1, 1), 1)
        self.assertEqual(permutation_coefficient(1, 0), 1)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, permutation_coefficient, -1, 2)
        self.assertRaises(ValueError, permutation_coefficient, 2, -1)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, permutation_coefficient, 0, 0)
        self.assertRaises(ValueError, permutation_coefficient, 0, 1)
        self.assertRaises(ValueError, permutation_coefficient, 1, 0)
        self.assertRaises(ValueError, permutation_coefficient, 1, 2)
